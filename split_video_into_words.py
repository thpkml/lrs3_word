import os
import datetime
import subprocess
from pathlib import Path

import cv2 as cv
from tqdm import tqdm

import files

# SETTINGS START
# split = 'small' 
split = 'same_size'

if split == 'small':
    from files import small as size
elif split == 'same_size':
    from files import same_size as size

lrs3_by_words = size['lrs3_by_words']

partitions = {'a': (size['lrs3_new_test_list'], 'test'), 'b': (size['lrs3_new_train_list'], 'train'), 'c': (size['lrs3_new_val_list'], 'val')}

list_file = partitions['b'][0]
partition = partitions['b'][1]
min_duration = 0.5
# SETTINGS END


# Start
with open(list_file, 'r') as f:
    lines = f.readlines()[50000:]  # TODO: remove the slicing when done
    for line in tqdm(lines, position=0, leave=True, desc=f'reading lines in list file'):  # tqdm settings 
        line = line.strip()
        vid = line+'.mp4'
        txt_file = line+'.txt'
    
        with open(txt_file, 'r') as f1:
            txt_lines = f1.readlines()
            text = txt_lines[0].split('Text:')[1]
            words = {}
            for i, l in tqdm(enumerate(txt_lines[4:]), leave=False):  # tqdm leave=False so inner loop progress bar hides after completion 
                word, start, end, score = l.split(' ')
                start = float(start)
                end = float(end)
                if word.isdigit() or list(word)[0].isdigit():  # do not include numeric words e.g. 2020
                    continue
                duration = end - start
                if duration > min_duration:
                    words[word] = start, end, line
                    hms_start = str(datetime.timedelta(seconds=start))
                    hms_end = str(datetime.timedelta(seconds=end))
                    try:
                        Path(os.path.abspath(os.path.join(lrs3_by_words, word, partition))).mkdir(parents=True, exist_ok=True)
                        # increment fname number if file exists
                        word_dir = os.path.abspath(os.path.join(lrs3_by_words, word, partition))
                        n = len(os.listdir(word_dir)) + 1
                        suffix = str(n).zfill(5)
                        filename = os.path.abspath(os.path.join(lrs3_by_words, word, partition, f'{word}_{suffix}.mp4'))
                        # if os.path.exists(filename):
                        #     n = int(filename[-9:].split('.')[0]) + 1
                        #     suffix = str(n).zfill(5)
                        #     filename = os.path.abspath(os.path.join(lrs3_by_words, word, partition, f'{word}_{suffix}.mp4'))
                        cmd = [
                        'ffmpeg', '-y',
                        '-hide_banner', 
                        '-loglevel', 'error',
                        '-i', vid,
                        '-ss', f'{hms_start}',
                        '-to', f'{hms_end}',
                        '-c', 'copy',
                        f'{filename}'
                        ]
                        subprocess.run(cmd)
                    except (FileNotFoundError, NotADirectoryError, OSError) as e:
                        pass

