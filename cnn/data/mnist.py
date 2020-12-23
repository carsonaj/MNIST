import torch
from torch.utils.data import DataSet, DataLoader
from torchvision import transforms, utils


class MNISTDataset(Dataset):
	""" MNIST dataset """
	def __init__(self, root_dir, transform = None):
		"""
		ARGS: 
			root_dir (string) : Directory of MNIST data. 
			transform : optinoal tranform to apply to data. 
		"""
		pass
	

	def __len__(self):
		pass
	
	def __getitem__(self, idx):
		pass



MNISTDataset("dah")
