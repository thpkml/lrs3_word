import os
import files

# SETTINGS START
# split = 'small' 
split = 'same_size'
# SETTINGS END

if split == 'small':
    from files import small as size
elif split == 'same_size':
    from files import same_size as size

with open(size['lrs3_word_shortlist'], 'r') as f:
    word_dirs = []
    words = []
    for line in f.readlines()[1:]:
        line = line.split(' ')
        word_dirs.append(line[-1].strip())
        words.append(line[0])

with open(size['lrs3_500_detected_face'], 'w') as f1:
    for word_dir in word_dirs:
        for path, subdirs, files in os.walk(word_dir):
            path = path.split(os.path.sep)
            for name in files:
                name = name[:-4]+',0\n'
                f1.write(os.path.join(path[-2], path[-1], name))
                print(os.path.join(path[-2], path[-1], name))

