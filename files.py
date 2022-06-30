import os

_location = os.path.abspath(os.getcwd())
data_disk = os.path.abspath(os.path.join('D:'))
tcn_model_zoo = os.path.abspath(os.path.join(data_disk, 'tcn_model_zoo_pantic_etal'))

lrw = os.path.abspath(os.path.join(data_disk, 'lrw_dataset'))
lrw_videos = os.path.abspath(os.path.join(lrw, 'liread_mp4'))
lrw_landmarks = os.path.abspath(os.path.join(lrw, 'LRW_landmarks'))
lrw_mouth_ROIs = os.path.abspath(os.path.join(lrw, 'mouth_ROIs'))

lrs3 = os.path.abspath(os.path.join(data_disk, 'lrs3_dataset'))
lrs3_pretrain = os.path.abspath(os.path.join(lrs3, 'pretrain'))
lrs3_test = os.path.abspath(os.path.join(lrs3, 'test'))
lrs3_trainval = os.path.abspath(os.path.join(lrs3, 'trainval'))
lrs3_mouth_ROIs = os.path.abspath(os.path.join(lrs3, 'mouth_ROIs'))
lrs3_text = os.path.abspath(os.path.join(lrs3, 'text'))
lrs3_text_pretrain = os.path.abspath(os.path.join(lrs3, 'text', 'pretrain'))
lrs3_text_test = os.path.abspath(os.path.join(lrs3, 'text', 'test'))
lrs3_text_trainval = os.path.abspath(os.path.join(lrs3, 'text', 'trainval'))
lrs3_pretrain_list = os.path.abspath(os.path.join(lrs3, 'pretrain.txt'))

lrs3_new_small_split = os.path.abspath(os.path.join(data_disk, 'lrs3_dataset', 'new_smaller_split'))
lrs3_new_same_size_split = os.path.abspath(os.path.join(data_disk, 'lrs3_dataset', 'new_same_size_split'))

small = {
    'dataset': lrs3_new_small_split,
    'videos': os.path.abspath(os.path.join(lrs3_new_small_split, 'lrs3_by_words')),
    'mouth_rois': os.path.abspath(os.path.join(lrs3_new_small_split, 'mouth_ROIs')),
    'landmarks': os.path.abspath(os.path.join(lrs3_new_small_split, 'lrs3_landmarks')),
    'text_all': os.path.abspath(os.path.join(lrs3_new_small_split, 'all.txt')),
    'text_test': os.path.abspath(os.path.join(lrs3_new_small_split, 'test.txt')),
    'text_train': os.path.abspath(os.path.join(lrs3_new_small_split, 'train.txt')),
    'text_val': os.path.abspath(os.path.join(lrs3_new_small_split, 'val.txt')),

    'word_count': os.path.abspath(os.path.join(lrs3_new_small_split, 'word_count.txt')),
    'word_shortlist': os.path.abspath(os.path.join(lrs3_new_small_split, 'word_shortlist.txt')),
    'word_shortlist_500': os.path.abspath(os.path.join(lrs3_new_small_split, 'word_shortlist_500.txt')),
    'word_shortlist_500_each_videopath': os.path.abspath(os.path.join(lrs3_new_small_split, 'word_shortlist_500_each_videopath.txt')),
    '500_detected_face': os.path.abspath(os.path.join(lrs3_new_small_split, 'lrs3_500_detected_face.csv')),
    'labels': os.path.abspath(os.path.join(lrs3_new_small_split, 'labels.txt'))
}

same_size = {
    'dataset': lrs3_new_same_size_split,
    'videos': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'lrs3_by_words')),
    'mouth_rois': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'mouth_ROIs')),
    'landmarks': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'lrs3_landmarks')),
    'text_all': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'all.txt')),
    'text_test': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'test.txt')),
    'text_train': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'train.txt')),
    'text_val': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'val.txt')),

    'word_count': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'word_count.txt')),
    'word_shortlist': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'word_shortlist.txt')),
    'word_shortlist_500': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'word_shortlist_500.txt')),
    'word_shortlist_500_each_videopath': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'word_shortlist_500_each_videopath.txt')),
    '500_detected_face': os.path.abspath(os.path.join(lrs3_new_same_size_split, 'lrs3_500_detected_face.csv')),
    'labels': os.path.abspath(os.path.join(lrs3_new_small_split, 'labels.txt'))
}

lrw = {
    'dataset': lrw,
    'videos': lrw_videos,
    'landmarks': lrw_landmarks,
    'mouth_rois': lrw_mouth_ROIs,
    'labels': os.path.abspath(os.path.join(lrw, '500WordsSortedList.txt'))
}

def is_subset_of(subset, superset):
    sup = os.listdir(superset)
    sub = os.listdir(subset)
    dif = [x for x in sub if x not in sup]
    if len(dif) > 0:
        print(subset, 'is not a subset of ', superset)
    else:
        print(subset, 'is a subset of ', superset)

# is_subset_of(lrs3_trainval, lrs3_pretrain)
# is_subset_of(lrs3_test, lrs3_pretrain)
# is_subset_of(lrs3_test, lrs3_trainval)
# OUTPUT
# D:\lrs3_dataset\trainval is a subset of  D:\lrs3_dataset\pretrain
# D:\lrs3_dataset\test is not a subset of  D:\lrs3_dataset\pretrain
# D:\lrs3_dataset\test is not a subset of  D:\lrs3_dataset\trainval

# print(lrs3_text_trainval)
# import pdb;pdb.set_trace()