import os
import numpy as np
import files
from PIL import Image

mouth_rois = files.small['lrs3_mouth_ROIs']
# mouth_rois = files.lrw_mouth_ROIs

too_long_clips = 0
total_long_clips = 0
total_short_clips = 0
for path, dirs, files in os.walk(mouth_rois):
        for name in files:
            npz = np.load(os.path.abspath(os.path.join(path, name)), allow_pickle=True)['data']
            print(npz.shape)
            if npz.shape[0] > 29:
                too_long_clips += 1
            if npz.shape[0] > 10:
                total_long_clips += 1
            else:
                total_short_clips += 1
print('too_long_clips: ', too_long_clips)
print('total_short_clips: ', total_short_clips)
print('total_short_clips: ', total_short_clips)

exit()

sample_lrw_landmark_npz = os.path.abspath(os.path.join(files.lrw_landmarks, 'ABOUT', 'test', 'ABOUT_00001.npz'))
sample_lrs3_landmark_npz = os.path.abspath(os.path.join(files.small['lrs3_landmarks'], 'ABOUT', 'test', 'ABOUT_00001.npz'))
sample_lrw_roi_npz = os.path.abspath(os.path.join(files.lrw_mouth_ROIs, 'ABOUT', 'test', 'ABOUT_00001.npz'))
sample_lrs3_roi_npz = os.path.abspath(os.path.join(files.small['lrs3_mouth_ROIs'], 'ABOUT', 'test', 'ABOUT_00001.npz'))

npz1 = np.load(sample_lrw_landmark_npz, allow_pickle=True)
npz2 = np.load(sample_lrs3_landmark_npz, allow_pickle=True)
npz3 = np.load(sample_lrw_roi_npz, allow_pickle=True)
npz4 = np.load(sample_lrs3_roi_npz, allow_pickle=True)
frames1 = npz1['data']
frames2 = npz2['data']

frame1 = frames1[0][0]
frame1id = frame1['id']
frame1facelm = frame1['facial_landmarks']
frame1eyelm = frame1['eye_landmarks']
# for i in range(len(npz4['data'])):
#     img = Image.fromarray(npz4['data'][i], 'L')
#     img.show()
img = Image.fromarray(npz4['data'][0], 'RGB')
img.show()

'''
Each frame has 68 landmarks given by 2 coordinates. 
LRW tends to have around 29 frames consistently.
LRS3 has less frames per video and has variable number of frames

the npz files in the two datasets are also slightly different. 
LRS3, the one we created simply has (frames, 68, 2) numpy arrays

frames1.shape = (29, 1) for 29 frames LRW
frames2.shape = (5, 68, 2) for 5 frames LRS3
frame1facelm.shape = (68,2)
frames2[0].shape = (68, 2)
'''
import pdb; pdb.set_trace()
