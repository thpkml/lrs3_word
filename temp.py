# TRAIN TROUBLESHOOT SCRIPT AS DISPLAYED ON TERMINAL
import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = False
torch.backends.cudnn.allow_tf32 = True
data = torch.randn([32, 768, 1, 29], dtype=torch.float, device='cuda', requires_grad=True)
net = torch.nn.Conv2d(768, 256, kernel_size=[1, 3], padding=[0, 2], stride=[1, 1],
dilation=[1, 1], groups=1)
net = net.cuda().float()
out = net(data)
out.backward(torch.randn_like(out))
torch.cuda.synchronize()

# TORCH SAVE CHECKPOINT EXERCISE FROM: https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html 

# import files
# import os
# small_500 = files.small['lrs3_word_shortlist_500']
# same_500 = files.same_size['lrs3_word_shortlist_500']
# labels_small = os.path.abspath(os.path.join(files.lrs3_new_small_split, 'labels.txt'))
# labels_same = os.path.abspath(os.path.join(files.lrs3_new_same_size_split, 'labels.txt'))
# with open(small_500, 'r') as f:
#     with open(labels_small, 'w') as f1:
#         lines = f.readlines()[1:]
#         for line in lines:
#             f1.write(line.split(' ')[0]+'\n')

# with open(same_500, 'r') as f:
#     with open(labels_same, 'w') as f1:
#         lines = f.readlines()[1:]
#         for line in lines:
#             f1.write(line.split(' ')[0]+'\n')
# exit()

# import files
# import os
# import numpy as np
# from tqdm import tqdm
# rois = files.same_size['lrs3_mouth_ROIs']
# rois_10_frames_plus = os.path.abspath(os.path.join(files.lrs3_new_same_size_split, 'rois_10_frames_plus.txt'))
# with open(rois_10_frames_plus, 'w') as f:
#     for path, dirs, files in tqdm(os.walk(rois)):
#         for name in files:
#             roi = os.path.abspath(os.path.join(path, name))
#             npz = np.load(roi, allow_pickle=True)['data']
#             if npz.shape[0] >= 10:
#                 f.write(roi+' '+str(npz.shape[0])+'\n')
# exit()

# import torch
# import torch.nn as nn
# import torch.optim as optim

# class Net(nn.Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.conv1 = nn.Conv2d(3, 6, 5)
#         self.pool = nn.MaxPool2d(2, 2)
#         self.conv2 = nn.Conv2d(6, 16, 5)
#         self.fc1 = nn.Linear(16 * 5 * 5, 120)
#         self.fc2 = nn.Linear(120, 84)
#         self.fc3 = nn.Linear(84, 10)

#     def forward(self, x):
#         x = self.pool(F.relu(self.conv1(x)))
#         x = self.pool(F.relu(self.conv2(x)))
#         x = x.view(-1, 16 * 5 * 5)
#         x = F.relu(self.fc1(x))
#         x = F.relu(self.fc2(x))
#         x = self.fc3(x)
#         return x

# net = Net()
# print(net)

# optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# # Additional information
# EPOCH = 5
# PATH = "model.pt"
# LOSS = 0.4

# torch.save({
#             'epoch': EPOCH,
#             'model_state_dict': net.state_dict(),
#             'optimizer_state_dict': optimizer.state_dict(),
#             'loss': LOSS,
#             }, PATH)

# model = Net()
# optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# checkpoint = torch.load(PATH)
# model.load_state_dict(checkpoint['model_state_dict'])
# optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
# epoch = checkpoint['epoch']
# loss = checkpoint['loss']

# # model.eval()
# # - or -
# model.train()