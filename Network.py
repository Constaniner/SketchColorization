import torch
import torch.nn as nn
import torch.optim as optim

import random
import time
import os

from torchvision import transforms

from PIL import Image

class TrainerNet():
    def __init__(self, *args):
        self.resultpath = './data/result'