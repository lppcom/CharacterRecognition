#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 22:33
# @User    : zhunishengrikuaile
# @File    : receipt.py
# @Email   : binary@shujian.org
# @MyBlog  : WWW.SHUJIAN.ORG
# @NetName : 書劍
# @Software: MeBlog

'''
通用票据识别
'''

import os
import base64
import requests
from shitu_api.bin.CharacterRecognition.general import ORC_Images


class Receipt(ORC_Images):
    def __init__(self, IMG, API_KEY, SECRET_KEY, URLS, recognize_granularity='big', probability=True, accuracy='normal',
                 detect_direction=True):
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.img = IMG
        self.urls = URLS
        self.recognize_granularity = recognize_granularity
        self.probability = probability
        self.accuracy = accuracy
        self.detect_direction = detect_direction

    def postOrcImg(self):
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        url = "{}?access_token={}".format(self.urls, self.get_token())
        if os.path.isfile(self.img):
            with open(self.img, 'rb') as img_file:
                imgs = base64.b64encode(img_file.read())
        else:
            return '文件路径不正确'
        data = {'image': imgs, 'recognize_granularity': self.recognize_granularity, 'probability': self.probability,
                'accuracy': self.accuracy, 'detect_direction': self.detect_direction}
        result = requests.post(url, headers=header, data=data)
        return result
