"""
This Python class, TrafficDataset, is designed to handle loading and processing of traffic data for graph neural networks (GNNs). It's designed to be used with PyTorch Geometric, a library for deep learning on graphs using PyTorch. The class inherits from the InMemoryDataset base class provided by PyTorch Geometric, which is a dataset class designed to store pre-processed data in memory.

Let's break down the main parts of the class:

__init__ method: This method initializes the dataset. It sets configuration, adjacency matrix W, and then calls the superclass constructor. It also loads the processed dataset into memory.
raw_file_names and processed_file_names properties: These properties define the names of the raw and processed data files.
download method: This method copies the raw dataset from the default location to the raw_dir directory.
process method: This is where the raw data is processed and saved in a format that's ready for use with GNNs. The raw data is loaded and normalized, then the adjacency matrix is used to create the edge index and edge attribute tensors for the graph. For each time window, a graph is created with the corresponding time-series data, and these are collated into a PyTorch Geometric Data list.
z_score: This function normalizes the data using the z-score normalization. It's not defined in the code you provided but it's likely a function that takes data, its mean, and its standard deviation, and returns the normalized data.
"""

# Define a class named 'TrafficDataset' which inherits from the 'InMemoryDataset' class.
class TrafficDataset(InMemoryDataset):
    """
    Dataset for Graph Neural Networks.
    """

    # Define the constructor for the TrafficDataset class.
    def __init__(self, config, W, root='', transform=None, pre_transform=None):
        # Set up the configuration parameters and adjacency matrix
        self.config = config
        self.W = W

        # Call the constructor of the superclass 'InMemoryDataset' and set up the transformation functions.
        super().__init__(root, transform, pre_transform)

        # Load processed data, slices, number of nodes, mean, and standard deviation from a torch file.
        self.data, self.slices, self.n_node, self.mean, self.std_dev = torch.load(self.processed_paths[0])

    # Property that returns the name of the raw data file. 
    @property
    def raw_file_names(self):
        return [os.path.join(self.raw_dir, 'PeMSD7_V_228.csv')]

    # Property that returns the name of the processed data file.
    @property
    def processed_file_names(self):
        return ['./data.pt']

    # Method for copying the raw data file to the 'raw_dir' directory.
    def download(self):
        copyfile('./dataset/PeMSD7_V_228.csv', os.path.join(self.raw_dir, 'PeMSD7_V_228.csv'))

    # Method for processing the raw data and saving it in a processed format.
    def process(self):
        # Load the raw data into a pandas DataFrame and convert it to numpy array.
        data = pd.read_csv(self.raw_file_names[0], header=None).values

        # Calculate the mean and standard deviation of the data.
        mean = np.mean(data)
        std_dev = np.std(data)

        # Normalize the data using z-score normalization.
        data = z_score(data, np.mean(data), np.std(data))

        # Get the number of nodes from the data shape.
        _, n_node = data.shape

        # Calculate the window size.
        n_window = self.config['N_PRED'] + self.config['N_HIST']

        # Initialize tensors for storing edge index and edge attributes.
        edge_index = torch.zeros((2, n_node**2), dtype=torch.long)
        edge_attr = torch.zeros((n_node**2, 1))

        # Fill the edge index and edge attributes tensors.
        num_edges = 0
        for i in range(n_node):
            for j in range(n_node):
                if self.W[i, j] != 0.:
                    edge_index[0, num_edges] = i
                    edge_index[1, num_edges] = j
                    edge_attr[num_edges] = self.W[i, j]
                    num_edges += 1

        # Resize the edge index and edge attributes tensors to keep only the first 'num_edges' entries.
        edge_index = edge_index.resize_(2, num_edges)
        edge_attr = edge_attr.resize_(num_edges, 1)

        # Initialize a list for storing sequences of graph data.
        sequences = []

        # Construct the sequences of graph data.
        for i in range(self.config['N_DAYS']):
            for j in range(self.config['N_SLOT']):
                g = Data()
                g.__num_nodes__ = n_node

                g.edge_index = edge_index
                g.edge_attr = edge_attr

                # Set the start and end indices for slicing the data window.
                sta = i * self.config['N_DAY_SLOT'] + j
                end = sta + n_window

                # Slice the data window and swap the axes.
                full_window = np.swapaxes(data[sta:end, :], 0, 1)

                # Assign the input and target data for the graph.
                g.x = torch.FloatTensor(full_window[:, 0:self.config['N_HIST']])
                g.y = torch.FloatTensor(full_window[:, self.config['N_HIST']::])

                # Append the graph to the sequences list.
                sequences += [g]

        # Collate the sequences into a single data object and slice dictionary.
        data, slices = self.collate(sequences)

        # Save the processed data, slices, number of nodes, mean, and standard deviation to a torch file.
        torch.save((data, slices, n_node, mean, std_dev), self.processed_paths[0])
