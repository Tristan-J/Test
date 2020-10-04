import torch
from torch.utils.data import DataLoader

class TDataset(object):
    """
    Dataset of testing linear data
    """
    def __init__(self, root_dir, is_train=True, random_seed=0, augmentation_params=None):
        super(TDataset, self).__init__()
        self.arg = arg
        