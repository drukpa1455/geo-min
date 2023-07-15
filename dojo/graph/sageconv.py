import torch
from torch_geometric.nn import SAGEConv

# Define the SAGE (GraphSAGE) model as a PyTorch module
class SAGE(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super(SAGE, self).__init__()
        # Define the first GraphSAGE convolution layer
        # This corresponds to the equation:
        # AGGREGATE_pool^k = max({σ(W_pool^k * h_u^i + b), ∀u ∈ N(v)})
        # where σ is the activation function (ReLU in this case),
        # W_pool^k is the weight matrix for the k-th layer (learned during training),
        # h_u^i is the feature vector of the i-th neighbor node u,
        # N(v) is the set of neighbor nodes of node v,
        # and b is the bias term (also learned during training).
        self.conv1 = SAGEConv(in_channels, 16)

        # Define the second GraphSAGE convolution layer
        # This is another application of the same equation, but with different learned weights.
        self.conv2 = SAGEConv(16, out_channels)

    def forward(self, data):
        # Extract the node feature matrix and adjacency list from the data
        x, edge_index = data.x, data.edge_index

        # Apply the first GraphSAGE convolution
        # The input is the node feature matrix and adjacency list
        x = self.conv1(x, edge_index)
        # Apply the ReLU activation function to introduce non-linearity
        # This corresponds to the σ in the equation.
        x = torch.relu(x)
        # Apply dropout for regularization during training
        x = torch.nn.functional.dropout(x, p=0.5, training=self.training)

        # Apply the second GraphSAGE convolution
        # This is another application of the same equation, but with different learned weights.
        x = self.conv2(x, edge_index)

        # Apply the log softmax function to the output of the second convolution layer
        # This is typically done in multi-class classification problems to obtain probabilities for each class
        return torch.nn.functional.log_softmax(x, dim=1)
