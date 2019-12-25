import torch
from torch.utils.data import DataLoader
from torchvision import transforms
import GetArgs
from DataPrepare import InputData
from Network import TrainerNet

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Get arguments
parser = GetArgs.GetArgs()
args = parser.parse_args()

train_transform = transforms.ToTensor()
validate_transform = transforms.ToTensor()

# Get Data
train_data = InputData(transform=train_transform, colorhisto=True)
val_data = InputData(mode='validate', transform=validate_transform, colorhisto=True)
train_dataloader = DataLoader(dataset=train_data,batch_size=args.batch_size,shuffle=True)

# Training
Model = TrainerNet(args, train_dataloader, device)