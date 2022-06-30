'''
from all the prepared videos using split_video_into_words.py:
- select videos of words that have all sets: train, test, val
    - because since each word is a class, it needs to be in all sets 
- from the selection shortlist videos of words that have maximum number of samples per word
- create a list file for the word
- also create a list file for each individual video path
'''
# NOTE: CHECK SETTINGS AT THE TOP AND UNCOMMENT THE REQUIRED FUNCTION AT THE END
import os

import files

from tqdm import tqdm

# SETTINGS START
min_train = 20
min_val = 10
min_test = 3

# split = 'small' 
split = 'same_size'
if split == 'small':
    from files import small as size
elif split == 'same_size':
    from files import same_size as size
# SETTINGS END

# make a txt file with: word train_count val_count test_count word_dir
file_header = 'WORD TRAIN_COUNT VAL_COUNT TEST_COUNT DIR\n'
def write_word_count():
    with open(size['lrs3_word_count'], 'w') as f:
        f.write(file_header)
        words_dir = size['lrs3_by_words']
        words = os.listdir(words_dir)
        num_words = len(words)
        print(num_words, ' words in total!')
        for word in tqdm(words):
            try:
                word_dir = os.path.abspath(os.path.join(words_dir, word))
                train_count = len(os.listdir(os.path.abspath(os.path.join(word_dir, 'train'))))
                val_count = len(os.listdir(os.path.abspath(os.path.join(word_dir, 'val'))))
                test_count = len(os.listdir(os.path.abspath(os.path.join(word_dir, 'test'))))
                f.write(word+' '+str(train_count)+' '+str(val_count)+' '+str(test_count)+' '+word_dir+'\n')
            except (FileNotFoundError, NotADirectoryError, OSError) as e:
                pass

def shortlist_words(min_train, min_val, min_test):
    total_train, total_val, total_test = 0,0,0
    with open(size['lrs3_word_count'], 'r') as f:
        with open(size['lrs3_word_shortlist'], 'w') as f1:
            f1.write(file_header)
            for l in tqdm(f.readlines()[1:]):
                line = l.split(' ')
                word = line[0]
                train_count = int(line[1])
                val_count = int(line[2])
                test_count = int(line[3])
                total_train += train_count
                total_val += val_count
                total_test += test_count
                if train_count >= min_train and val_count >= min_val and test_count >= min_test:
                    f1.write(l)
            print('total_train:', total_train, 'total_val:', total_val, 'total_test:', total_test)

def shortlist_500_words():
    # if there are more than 500 shortlisted words, get the 500 words with most samples in train sets
    with open(size['lrs3_word_shortlist'], 'r') as f:
        lines = f.readlines()[1:]
        if len(lines) <= 500:
            return 'Less than 500 words in the shortlist!'
        else:
            shorted = []
            for i, line in enumerate(lines):
                shorted.append((i, int(line.split(' ')[1])))
            sort = sorted(shorted, key=lambda x: x[1], reverse=True)  # sort all by sample count descending
            sort = sort[:500]  # get top 500
            sort = sorted(sort, key=lambda x: x[0])  # sort all by line number ascending i.e. alphabetical
            # print(sort)
            with open(size['lrs3_word_shortlist_500'], 'w') as f1:
                f1.write(file_header)
                for line_num, count in sort:
                    f1.write(lines[line_num])

def shortlist_500_path_to_each_sample(): # Only once the shortlist 500 is created 
    with open(size['lrs3_word_shortlist_500'], 'r') as f:
        with open(size['lrs3_word_shortlist_500_each_videopath'], 'w') as f1:
            lines = f.readlines()[1:]
            word_dirs = []
            for line in lines:
                word_dirs.append(line.split(' ')[4].strip())
            for word_dir in word_dirs:
                for path, dirs, files in os.walk(word_dir):
                    for name in files:
                        if (name.split('_')[0] == os.path.split(word_dir)[-1]):
                            vid_path = os.path.abspath(os.path.join(path, name))
                            f1.write(vid_path+'\n')            



# write_word_count()
# shortlist_words(min_train, min_val, min_test)
# shortlist_500_words()
shortlist_500_path_to_each_sample()
