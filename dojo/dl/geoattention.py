import torch
from torch.nn import GRU, Linear
from torch_geometric.nn import GATConv
from torch_geometric.data import Data
from torch_geometric_temporal.signal import temporal_signal_split
from sklearn.model_selection import train_test_split

# We first define a new model which is a combination of Graph Attention Network and Gated Recurrent Units
class GAT_GRU(torch.nn.Module):
    def __init__(self, num_node_features, num_nodes):
        super(GAT_GRU, self).__init__()
        # GAT layer, with 8 attention heads. Dropout is applied for regularization.
        self.gat = GATConv(num_node_features, 8, heads=8, dropout=0.6)
        # GRU layer to process the output of GAT layer in sequence
        self.gru = GRU(8 * 8, 16, batch_first=True)
        # Linear layer to produce the final output
        self.linear = Linear(16, 1)

    def forward(self, data, h=None):
        x, edge_index, edge_weight = data.x, data.edge_index, data.edge_attr
        # Pass the input through GAT layer
        x = self.gat(x, edge_index, edge_weight).relu()
        # Reshape the output for GRU layer
        x = x.view(-1, num_nodes, 8 * 8)
        # Pass the output of GAT layer through GRU layer
        if h is not None:
            x, h = self.gru(x, h)
        else:
            x, h = self.gru(x)
        # Pass the output of GRU layer through linear layer
        out = self.linear(x[:, -1, :])
        return out, h

# Load your dataset here
# edge_index, edge_weight, node_features, node_targets = ...

# Assume that node_features is of shape [num_timesteps, num_nodes, num_features]
# and node_targets is of shape [num_timesteps, num_nodes]
num_timesteps, num_nodes, num_features = node_features.shape

# Normalize the features and targets if necessary
# ...

# Split the dataset into training, validation and test sets
train_node_features, test_node_features, train_node_targets, test_node_targets = train_test_split(
    node_features, node_targets, test_size=0.2, random_state=42
)

# Create a PyTorch Geometric Data for each timestep
# This encapsulates the information of the graph at each timestep
train_data_list = [
    Data(x=torch.from_numpy(train_node_features[i]).float(), 
         y=torch.from_numpy(train_node_targets[i]).float(), 
         edge_index=edge_index, edge_attr=edge_weight) 
    for i in range(train_node_features.shape[0])
]

# Initialize the model and the optimizer
model = GAT_GRU(num_features, num_nodes)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(200):
    model.train()
    h = None
    for data in train_data_list:
        # Set gradients to zero
        optimizer.zero_grad()
        # Forward pass
        out, h = model(data, h)
        # Compute the loss
        loss = ((out - data.y)**2).mean()
        # Backward pass
        loss.backward()
        # Update the weights
        optimizer.step()
    if epoch % 10 == 0:
        # Print the loss for this epoch
        print(f'Epoch: {epoch}, Loss: {loss.item()}')
