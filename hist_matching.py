#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""hist matching."""

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
        target_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])
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
            comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])
            ret = cv2.compareHist(target_hist, comparing_hist, 0)
            d[file] = ret
        except cv2.error:
            print(file)
            continue

    # sort and print
    i = 0
    for k, v in sorted(d.items(), reverse=True, key=lambda x: x[1]):
        print('%s: %f' % (k, v))
        i += 1
        if i >= MAX_DISP:
            break
