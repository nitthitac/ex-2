import numpy as np
from os import listdir, makedirs
import cv2
from random import random, seed

Kaggle_PATH = 'D:/bookFiles/Cat_Dog_Kaggle/train/'
dataset_PATH = 'D:/bookFiles/cats_vs_dog/'
# create standard directory
sub_dirs= ['/train', '/test']
sub_sub_dirs = ['/cats', '/dogs']
for sub_dir in sub_dirs:
    for sub_sub_dir in sub_sub_dirs:
        makedirs(dataset_PATH+sub_dir+sub_sub_dir, exist_ok=True)

seed(1)
for file in listdir(Kaggle_PATH):
    test_radio = 0.25
    img_size = (200,200)
    rand_num = random()
    directory = '/test/'
    if rand_num >= test_ratio:
        directory = '/train/'
    img = cv2.imread(Kaggle_PATH + file)
    img = cv2.resize(img, img_size)
    if file.startswith('cat'):
        cv2.imwrite(dataset_PATH+directory+'cats/'+file, img)
    else:
        cv2.imwrite(dataset_PATH + directory + 'dogs/' + file, img)