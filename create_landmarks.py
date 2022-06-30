import argparse
import os
from contextlib import contextmanager
from pathlib import Path

import cv2
import face_alignment
import numpy as np
from tqdm import tqdm

import warnings
warnings.filterwarnings('error')

import files
# SETTINGS START
# split = 'small' 
split = 'same_size'
if split == 'small':
    from files import small as size
elif split == 'same_size':
    from files import same_size as size
# SETTINGS END
lrs3_new_split = size['lrs3_new_split']
lrs3_landmarks = size['lrs3_landmarks']

sample_vid = os.path.abspath(os.path.join(size['lrs3_by_words'], 'ABOUT', 'test', 'ABOUT_00001.mp4'))
landmarks_dir = size['lrs3_landmarks']

@contextmanager
def VideoCapture(*args, **kwargs):
    cap = cv2.VideoCapture(*args, **kwargs)
    try:
        yield cap
    finally:
        cap.release()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--device', type=str, default='cuda')
    parser.add_argument('--queue-length', type=int, default=30)
    args = parser.parse_args()

    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, device=args.device, face_detector='sfd')

    # get all the videos in shortlist500 list
    with open(size['lrs3_word_shortlist_500_each_videopath'], 'r') as f:
        lines = f.readlines()
        print(len(lines), 'total lines to process!')
        with open('corrupted_word_videos.txt', 'r+') as errorlog:
            pre_listed_corrupted_videos = errorlog.readlines()[1:]
            pre_listed_corrupted_videos = [x.strip() for x in pre_listed_corrupted_videos]
            corrupted_videos = set()
            for line in tqdm(lines, position=0, leave=True):
                videopath = line.strip()
                path_split = videopath.split(os.path.sep)
                path_front = os.path.join(*path_split[:-4])
                path_end_dir = os.path.join(*path_split[-3:-1])
                path_end_file = os.path.join(*path_split[-3:]).split('.')[0]+'.npz'
                savedir = os.path.abspath(os.path.join(path_front, 'lrs3_landmarks', path_end_dir))
                savepath = os.path.abspath(os.path.join(path_front, 'lrs3_landmarks', path_end_file))                  
                if path_end_file in pre_listed_corrupted_videos:
                    continue               
                if os.path.exists(savepath):
                    continue
                video_landmarks = []
                with VideoCapture(videopath) as cap:
                    while True:
                        try:
                            ret, frame = cap.read()
                            if not ret:
                                break
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                            try:
                                all_landmarks = fa.get_landmarks(frame)
                                if all_landmarks:
                                    landmarks = all_landmarks[0]
                                    video_landmarks.append(landmarks)
                            except UserWarning:
                                corrupted_videos.add(path_end_file)
                                continue
                        except:
                            print('corrupted video: ', videopath)
                            pass
                cv2.destroyAllWindows()
                
                # write landmarks to files
                Path(savedir).mkdir(parents=True, exist_ok=True)
                np.savez(savepath, data=video_landmarks)

            if len(corrupted_videos) > 0:
                for path in corrupted_videos:
                    errorlog.write(path+'\n')


if __name__ == '__main__':
    main()