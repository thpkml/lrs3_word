''''
train:val:test = 24888:9600:1067 
for the new small version of lrs3 dataset
'''

import os

from tqdm import tqdm

import files

# SETTINGS START
# split = 'small' 
split = 'same_size'
# SETTINGS END

if split == 'small':
    from files import small as size
    parts = {
        'test': 1067,
        'train': 24888,
        'val': 9600
    }
elif split == 'same_size':
    from files import same_size as size
    parts = {
        'test': 3555,
        'train': 82961, 
        'val': 32000
    }
    

def count_samples(partition):
    total = 0
    for root, dirs, files in os.walk(partition):
        total += len(files)
    return int(total/2)  # coz one sample has 2 files mp4 and txt 

# num_pretrain_old = count_samples(files.lrs3_pretrain)  # 118516
# num_trainval_old = count_samples(files.lrs3_trainval)  # 31982
# num_test_old = count_samples(files.lrs3_test)  # 1321
# print(num_pretrain_old)

def count_lines(f):
    with open(f) as f1:
        for i, _ in enumerate(f1):
            pass
    print(i+1)


def list_all_pretrain():
    with open(files.lrs3_pretrain_list, 'w') as f:
        for root, dirs, filenames in os.walk(files.lrs3_pretrain):
            fs = [x.split('.')[0] for x in filenames if x[-1]=='4']  # meaning mp4 files
            # f.write(root+' '+dirs+' '+filenames)
            for x in fs:
                path = os.path.abspath(os.path.join(root, x))
                f.write(path+'\n')

def list_test_set():
    with open(files.lrs3_pretrain_list, 'r') as f:
        with open(size['lrs3_new_test_list'], 'w') as f1:
            for i in range(parts['test']):
                line = f.readline()
                f1.write(line)

def list_train_set():
    with open(files.lrs3_pretrain_list, 'r') as f:
        with open(size['lrs3_new_train_list'], 'w') as f1:
            for i, line in enumerate(f):  
                if split == 'small':
                # start from 2000, leave a wide margin to 1067 test samples 
                    if i < 2000:
                        pass
                    elif i > 2000+24887:  # for 24888 samples
                        break
                    else:
                        f1.write(line)
                elif split == 'same_size':
                    if i < parts['test']:
                        pass
                    elif i >= parts['test'] + parts['train']:
                        break
                    else:
                        f1.write(line)

def list_val_set():
    with open(files.lrs3_pretrain_list, 'r') as f:
        with open(size['lrs3_new_val_list'], 'w') as f1:
            for i, line in enumerate(f): 
                if split == 'small':
                    # start from 30000, leave a wide margin to 24800 train samples 
                    if i < 30000:
                        pass
                    elif i > 30000+9599:  # for 9600 samples
                        break
                    else:
                        f1.write(line)
                if split == 'same_size':
                    if i < parts['test'] + parts['train']:
                        continue
                    elif i >= parts['test'] + parts['train'] + parts['val']:
                        break
                    else: 
                        f1.write(line)

def list_all_sets():
    with open(size['lrs3_new_list'], 'w') as f:
        with open(size['lrs3_new_test_list'], 'r') as f1:
            for line in f1.readlines():
                f.write(line)
        with open(size['lrs3_new_train_list'], 'r') as f2:
            for line in f2.readlines():
                f.write(line)
        with open(size['lrs3_new_val_list'], 'r') as f3:
            for line in f3.readlines():
                f.write(line)

# Run these in order for the first time
# list_all_pretrain()
# list_test_set()
# list_train_set()
# list_val_set()
list_all_sets()

# count_lines(files.lrs3_pretrain_list)
# count_lines(size['lrs3_new_test_list'])
# count_lines(size['lrs3_new_train_list'])
# count_lines(size['lrs3_new_val_list'])
count_lines(size['lrs3_new_list'])

