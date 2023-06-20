import torch  # PyTorch library for tensor operations and deep learning
import torch.nn as nn  # PyTorch module for building neural networks
import torch.optim as optim  # PyTorch module for optimization algorithms
import torchvision  # PyTorch library for computer vision tasks
import torchvision.transforms as transforms  # PyTorch module for image transformations
import torchvision.utils as vutils  # PyTorch module for image visualization utilities
import pytorch_lightning as pl  # PyTorch Lightning library for simplifying the training process

# Define the generator network
class Generator(nn.Module):
    """Generator network of the DCGAN.
    The Generator class defines the generator network, which generates fake images from random noise.
    It consists of several transposed convolutional layers followed by batch normalization and ReLU activation functions.
    The final layer uses a Tanh activation function to produce the output fake images.

    Args:
        nz (int): Size of the input noise vector.
        ngf (int): Number of generator filters in the first layer.
        nc (int): Number of channels in the generated images.

    """
    def __init__(self, nz, ngf, nc):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            nn.ConvTranspose2d(nz, ngf * 8, 4, 1, 0, bias=False),  # Transpose convolutional layer 1
            nn.BatchNorm2d(ngf * 8),  # Batch normalization layer 1
            nn.ReLU(True),  # ReLU activation function
            nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),  # Transpose convolutional layer 2
            nn.BatchNorm2d(ngf * 4),  # Batch normalization layer 2
            nn.ReLU(True),  # ReLU activation function
            nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),  # Transpose convolutional layer 3
            nn.BatchNorm2d(ngf * 2),  # Batch normalization layer 3
            nn.ReLU(True),  # ReLU activation function
            nn.ConvTranspose2d(ngf * 2, ngf, 4, 2, 1, bias=False),  # Transpose convolutional layer 4
            nn.BatchNorm2d(ngf),  # Batch normalization layer 4
            nn.ReLU(True),  # ReLU activation function
            nn.ConvTranspose2d(ngf, nc, 4, 2, 1, bias=False),  # Transpose convolutional layer 5
            nn.Tanh()  # Tanh activation function for output
        )

    def forward(self, input):
        """Forward pass of the generator network.

        Args:
            input (torch.Tensor): Input noise vector.

        Returns:
            torch.Tensor: Generated fake images.

        """
        return self.main(input)


# Define the discriminator network
class Discriminator(nn.Module):
    """Discriminator network of the DCGAN.
    The Discriminator class defines the discriminator network, which distinguishes between real and fake images.
    It consists of several convolutional layers followed by batch normalization and LeakyReLU activation functions.
    The final layer uses a Sigmoid activation function to produce the output prediction.

    Args:
        nc (int): Number of channels in the input images.
        ndf (int): Number of discriminator filters in the first layer.

    """
    def __init__(self, nc, ndf):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),  # Convolutional layer 1
            nn.LeakyReLU(0.2, inplace=True),  # LeakyReLU activation function
            nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),  # Convolutional layer 2
            nn.BatchNorm2d(ndf * 2),  # Batch normalization layer 1
            nn.LeakyReLU(0.2, inplace=True),  # LeakyReLU activation function
            nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),  # Convolutional layer 3
            nn.BatchNorm2d(ndf * 4),  # Batch normalization layer 2
            nn.LeakyReLU(0.2, inplace=True),  # LeakyReLU activation function
            nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),  # Convolutional layer 4
            nn.BatchNorm2d(ndf * 8),  # Batch normalization layer 3
            nn.LeakyReLU(0.2, inplace=True),  # LeakyReLU activation function
            nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),  # Convolutional layer 5
            nn.Sigmoid()  # Sigmoid activation function for output
        )

    def forward(self, input):
        """Forward pass of the discriminator network.

        Args:
            input (torch.Tensor): Input images.

        Returns:
            torch.Tensor: Predictions for the input images.

        """
        return self.main(input).view(-1, 1).squeeze(1)


# Define the DCGAN LightningModule
class DCGAN(pl.LightningModule):
    """DCGAN LightningModule.
    The DCGAN class is a PyTorch LightningModule that combines the generator and discriminator networks for training.
    It handles the forward pass, loss calculation, optimization, and training step implementation.
    It also configures the optimizers and provides hooks for additional functionalities.    

    Args:
        nz (int): Size of the input noise vector.
        ngf (int): Number of generator filters in the first layer.
        ndf (int): Number of discriminator filters in the first layer.
        lr (float): Learning rate for optimization.
        beta1 (float): Adam optimizer beta1 parameter.
        dataloader_kwargs (dict): Keyword arguments for the dataloader.

    """
    def __init__(self, nz, ngf, ndf, lr, beta1, dataloader_kwargs):
        super(DCGAN, self).__init__()  # Call the parent class constructor
        self.nz = nz  # Set the size of the input noise vector
        self.ngf = ngf  # Set the number of generator filters in the first layer
        self.ndf = ndf  # Set the number of discriminator filters in the first layer
        self.lr = lr  # Set the learning rate for optimization
        self.beta1 = beta1  # Set the Adam optimizer beta1 parameter
        self.dataloader_kwargs = dataloader_kwargs  # Set the keyword arguments for the dataloader

        self.generator = Generator(nz, ngf, nc=3)  # Initialize the generator network
        self.discriminator = Discriminator(nc=3, ndf=ndf)  # Initialize the discriminator network

        self.criterion = nn.BCELoss()  # Initialize the binary cross-entropy loss function

    def forward(self, input):
        """Forward pass of the generator network.
        The forward() method in the Generator class takes an input noise vector and generates fake images using the generator network.

        Args:
            input (torch.Tensor): Input noise vector.

        Returns:
            torch.Tensor: Generated fake images.

        """
        return self.generator(input)  # Pass the input noise vector through the generator network and return the generated fake images

    def adversarial_loss(self, y_pred, y_true):
        """Computes the adversarial loss.
        The adversarial_loss() method in the DCGAN class computes the adversarial loss using binary cross-entropy loss (BCELoss).
        It measures the difference between the discriminator's predictions and the ground truth labels.

        Args:
            y_pred (torch.Tensor): Predictions.
            y_true (torch.Tensor): Ground truth.

        Returns:
            torch.Tensor: Adversarial loss value.

        """
        return self.criterion(y_pred, y_true)  # Compute the adversarial loss using the binary cross-entropy loss function

    def configure_optimizers(self):
        """Configures the optimizer(s) for training.
        The configure_optimizers() method in the DCGAN class sets up the optimizers for training.
        It returns a list of optimizers (one for the generator and one for the discriminator) and an empty scheduler list.

        Returns:
            Tuple[List[torch.optim.Optimizer], List[torch.optim.lr_scheduler]]: Optimizers and schedulers.

        """
        opt_g = optim.Adam(self.generator.parameters(), lr=self.lr, betas=(self.beta1, 0.999))  # Generator optimizer
        opt_d = optim.Adam(self.discriminator.parameters(), lr=self.lr, betas=(self.beta1, 0.999))  # Discriminator optimizer
        return [opt_g, opt_d], []  # Return optimizers and empty scheduler list

    def training_step(self, batch, batch_idx, optimizer_idx):
        """Training step for the DCGAN.
        The training_step() method in the DCGAN class defines the training logic for each batch of real images.
        It alternates between training the generator and discriminator based on the optimizer index.
        It calculates the generator loss and discriminator loss separately.

        Args:
            batch (torch.Tensor): Batch of real images.
            batch_idx (int): Batch index.
            optimizer_idx (int): Index of the current optimizer.

        Returns:
            dict: Dictionary containing the loss value.

        """
        real_images, _ = batch  # Extract the real images from the batch

        # Adversarial ground truths
        valid = torch.ones(real_images.size(0))  # Create a tensor of ones representing real images
        fake = torch.zeros(real_images.size(0))  # Create a tensor of zeros representing fake images

        if optimizer_idx == 0:
            # Train generator
            z = torch.randn(real_images.size(0), self.nz, 1, 1)  # Generate random noise vector
            fake_images = self.generator(z)  # Generate fake images using the generator
            g_loss = self.adversarial_loss(self.discriminator(fake_images), valid)  # Compute the generator loss
            return {'loss': g_loss}

        if optimizer_idx == 1:
            # Train discriminator
            real_loss = self.adversarial_loss(self.discriminator(real_images), valid)  # Compute the real loss
            z = torch.randn(real_images.size(0), self.nz, 1, 1)  # Generate random noise vector
            fake_images = self.generator(z)  # Generate fake images using the generator
            fake_loss = self.adversarial_loss(self.discriminator(fake_images.detach()), fake)  # Compute the fake loss
            d_loss = (real_loss + fake_loss) / 2  # Compute the overall discriminator loss
            return {'loss': d_loss}

    def on_epoch_end(self):
        """Generates and logs a grid of generated images to TensorBoard at the end of each epoch.
        The on_epoch_end() method in the DCGAN class is a callback that generates a grid of generated images at the end of each epoch.
        It uses the generator to create fake images and visualizes them using torchvision's make_grid() function.
        The grid of images is then logged to the TensorBoard for visualization.
        """
        z = torch.randn(64, self.nz, 1, 1)  # Generate random noise vector for generating images
        fake_images = self.generator(z)  # Generate fake images using the generator
        grid = vutils.make_grid(fake_images, normalize=True)  # Create a grid of the generated images
        self.logger.experiment.add_image('generated_images', grid, self.current_epoch)  # Log the generated images to TensorBoard

# Set hyperparameters
nz = 100  # Size of the input noise vector
ngf = 64  # Number of generator filters in the first layer
ndf = 64  # Number of discriminator filters in the first layer
lr = 0.0002  # Learning rate
beta1 = 0.5  # Adam optimizer beta1 parameter

# Initialize the DCGAN model
dcgan = DCGAN(nz=nz, ngf=ngf, ndf=ndf, lr=lr, beta1=beta1,
              dataloader_kwargs={'batch_size': 128, 'shuffle': True, 'num_workers': 4})  # Instantiate the DCGAN model with the specified hyperparameters and dataloader kwargs

# Initialize the Celeb-A dataset
transform = transforms.Compose([
    transforms.Resize((64, 64)),  # Resize the image to 64x64
    transforms.ToTensor(),  # Convert the image to a tensor
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalize the image
])
dataset = torchvision.datasets.CelebA(root='path/to/celeba',  # Path to the Celeb-A dataset
                                      split='train',
                                      transform=transform,
                                      download=True)

# Split dataset into train and validation sets
train_size = int(0.8 * len(dataset))  # Calculate the size of the training set (80% of the dataset)
val_size = len(dataset) - train_size  # Calculate the size of the validation set (remaining 20% of the dataset)
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])  # Randomly split the dataset into train and validation sets

# Initialize the Lightning DataModules
train_loader = torch.utils.data.DataLoader(train_dataset, **dcgan.dataloader_kwargs)  # Create a data loader for the training set
val_loader = torch.utils.data.DataLoader(val_dataset, **dcgan.dataloader_kwargs)  # Create a data loader for the validation set

# Initialize the Lightning Trainer
trainer = pl.Trainer(gpus=1, max_epochs=50, progress_bar_refresh_rate=20)  # Initialize the trainer with 1 GPU, maximum of 50 epochs, and progress bar refresh rate of 20

# Start training
trainer.fit(dcgan, train_loader, val_loader)  # Start the training process with the DCGAN model using the train and validation data loaders

"""
Remote Sensing Applications:
1. Data Augmentation: DCGANs can generate synthetic remote sensing images, which can be used to augment the training data. By training a DCGAN on existing remote sensing images, it can learn the underlying patterns and structures, and generate new images that are similar to the real data. These generated images can then be used to increase the diversity and size of the training dataset, improving the performance of remote sensing models.
2. Image Super-Resolution: DCGANs can be used to enhance the resolution of remote sensing images. By training the generator to learn the mapping from low-resolution to high-resolution images, DCGANs can generate high-resolution images from low-resolution inputs. This can be useful in applications where high-resolution images are required but only low-resolution images are available.
3. Change Detection: DCGANs can be employed to detect changes in remote sensing images over time. By training the discriminator to distinguish between images from different time periods, the generator can generate difference images that highlight the areas of change. This can aid in monitoring land cover changes, urban growth, deforestation, and other temporal variations in remote sensing data.
4. Image Translation: DCGANs can be used for cross-domain image translation in remote sensing. For example, DCGANs can learn to convert optical remote sensing images to synthetic aperture radar (SAR) images, or vice versa. This can facilitate multi-modal analysis and enable the fusion of different remote sensing data sources for improved understanding and interpretation.
5. Anomaly Detection: DCGANs can assist in anomaly detection in remote sensing data. By training the discriminator to distinguish between normal and abnormal remote sensing patterns, the generator can generate images that highlight areas of potential anomalies or outliers. This can be useful for identifying unusual or suspicious features, such as environmental hazards, infrastructure damage, or illegal activities.
"""