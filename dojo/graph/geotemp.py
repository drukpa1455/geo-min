# Import necessary Python libraries.
import numpy as np  # For numerical computations.
import matplotlib.pyplot as plt  # For creating plots.
import seaborn as sns  # For creating more attractive plots.
import networkx as nx  # For creating and manipulating complex networks.
import torch  # PyTorch, a deep learning library.
import torch.nn.functional as F  # For functions that don't have parameters such as relu, tanh, etc.

# PyTorch geometric (PyG) is an extension library for PyTorch dedicated to processing irregularly structured input data such as graphs, point clouds, and manifolds.
from torch_geometric.nn import GCNConv  
from torch_geometric_temporal.nn.recurrent import A3TGCN2
from torch_geometric_temporal.signal import temporal_signal_split
from torch_geometric.utils import to_networkx

# Check if CUDA (a parallel computing platform and API) is available for use.
# This line sets the device to be the first CUDA device if CUDA is available, and if not, it sets the device to be the CPU.
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

shuffle=True  # This will be used in the DataLoader.
batch_size = 32  # The size of the input data for one iteration.

# Import the traffic forecasting dataset based on Los Angeles Metropolitan traffic.
from torch_geometric_temporal.dataset import METRLADatasetLoader

# Create a loader object for the dataset.
loader = METRLADatasetLoader()

# Get the dataset using the loader object.
dataset = loader.get_dataset(num_timesteps_in=12, num_timesteps_out=12)

# Print out some details about the dataset.
print("Dataset type:  ", dataset)
print("Number of snapshots: ",  dataset.snapshot_count)
print(next(iter(dataset))) # Show first sample

# Create a plot to visualize the traffic over 24 hours for one sensor.
sensor_number = 1
hours = 24
sensor_labels = [bucket.y[sensor_number][0].item() for bucket in list(dataset)[:hours]]
plt.plot(sensor_labels)

# Split the dataset into a training set and a testing set.
train_dataset, test_dataset = temporal_signal_split(dataset, train_ratio=0.8)

# Print out the number of snapshots in the training set and the testing set.
print("Number of train buckets: ", train_dataset.snapshot_count)
print("Number of test buckets: ", test_dataset.snapshot_count)

# Convert the features and the targets in the training set and the testing set to PyTorch tensors.
# Then, load them into DataLoader objects.
train_input = np.array(train_dataset.features)
train_target = np.array(train_dataset.targets)
train_x_tensor = torch.from_numpy(train_input).type(torch.FloatTensor).to(DEVICE)
train_target_tensor = torch.from_numpy(train_target).type(torch.FloatTensor).to(DEVICE)
train_dataset_new = torch.utils.data.TensorDataset(train_x_tensor, train_target_tensor)
train_loader = torch.utils.data.DataLoader(train_dataset_new, batch_size=batch_size, shuffle=shuffle,drop_last=True)

test_input = np.array(test_dataset.features)
test_target = np.array(test_dataset.targets)
test_x_tensor = torch.from_numpy(test_input).type(torch.FloatTensor).to(DEVICE)
test_target_tensor = torch.from_numpy(test_target).type(torch.FloatTensor).to(DEVICE)
test_dataset_new = torch.utils.data.TensorDataset(test_x_tensor, test_target_tensor)
test_loader = torch.utils.data.DataLoader(test_dataset_new, batch_size=batch_size, shuffle=shuffle,drop_last=True)

# Define the TemporalGNN model, which is a graph convolutional network (GCN) specifically designed for temporal data.
class TemporalGNN(torch.nn.Module):
    def __init__(self):
        super(TemporalGNN, self).__init__()
        self.recurrent_1 = A3TGCN2(1, 32, 1)
        self.recurrent_2 = A3TGCN2(32, 32, 1)
        self.linear = torch.nn.Linear(32, 1)
    
    def forward(self, x):
        h = self.recurrent_1(x)
        h = F.relu(h)
        h = self.recurrent_2(h)
        h = F.relu(h)
        h = self.linear(h)
        return h

# Create an instance of the model and set the optimizer and the loss function.
model = TemporalGNN().to(DEVICE)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
criterion = torch.nn.MSELoss()

# Print out the parameters of the model.
print(model)

# Train the model on the training data.
for epoch in range(100):
    model.train()
    for i, data in enumerate(train_loader):
        optimizer.zero_grad()
        out = model(data[0])
        loss = criterion(out, data[1])
        loss.backward()
        optimizer.step()
        if i % 100 == 0:
            print(f'Epoch {epoch}, Step {i}, Loss {loss.item()}')

    # After each epoch, evaluate the model on the training data and print out the RMSE.
    model.eval()
    total_loss = 0
    for i, data in enumerate(train_loader):
        out = model(data[0])
        loss = criterion(out, data[1])
        total_loss += loss.item()*data[0].size(0)
    print(f'Epoch {epoch}, Train RMSE {np.sqrt(total_loss/len(train_loader.dataset)):.2f}')

# After training the model, evaluate it on the testing data and print out the MSE.
model.eval()
total_loss = 0
for i, data in enumerate(test_loader):
    out = model(data[0])
    loss = criterion(out, data[1])
    total_loss += loss.item()*data[0].size(0)
print(f'Test MSE {total_loss/len(test_loader.dataset):.2f}')

# After evaluating the model, visualize the predictions.
test_predictions = out.cpu().detach().numpy()
sns.heatmap(test_predictions[0, :, :], cmap='hot', vmin=-1, vmax=1)
plt.show()
