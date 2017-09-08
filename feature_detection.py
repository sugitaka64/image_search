#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""feature detection."""

import cv2
import os
import sys

IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images_min/'
IMG_SIZE = (200, 200)
MAX_DISP = 10

if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) == 1:
        # no parameter
        sys.exit(1)

    # get parameter keys
    arguments.pop(0)
    target_img_path = ''
    for argument in arguments:
        if '--target_img_path=' in argument:
            # found target_img_path
            target_img_path = argument.split('=')[1]
            break

    if target_img_path == '':
        # not found target_img_path
        sys.exit(1)

    if not os.path.isfile(target_img_path):
        # not file
        sys.exit(1)

    try:
        target_img = cv2.imread(target_img_path)
        target_img = cv2.resize(target_img, IMG_SIZE)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        detector = cv2.AKAZE_create()
        (target_kp, target_des) = detector.detectAndCompute(target_img, None)
    except cv2.error:
        sys.exit(1)

    d = {}
    files = os.listdir(IMG_DIR)
    for file in files:
        if file == '.DS_Store' or file == 'Thumbs.db':
            continue

        try:
            comparing_img_path = IMG_DIR + file
            comparing_img = cv2.imread(comparing_img_path)
            comparing_img = cv2.resize(comparing_img, IMG_SIZE)
            (comparing_kp, comparing_des) = detector.detectAndCompute(comparing_img, None)
            matches = bf.match(target_des, comparing_des)
            dist = [m.distance for m in matches]
            ret = sum(dist) / len(dist)
            d[file] = ret
        except cv2.error:
            print(file)
            continue

    # sort and print
    i = 0
    for k, v in sorted(d.items(), reverse=False, key=lambda x: x[1]):
        print('%s: %f' % (k, v))
        i += 1
        if i >= MAX_DISP:
            break
