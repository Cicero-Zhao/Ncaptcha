# -*- coding:utf-8 -*-

__author__ = 'barycenter'

import unittest
from ncaptcha import Ncaptcha
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

class TestCaptcha(unittest.TestCase):
    def test_img1(self):
        for i in range(0, 10):
            cap = Ncaptcha(font_size=48)
            img, code = cap.create()
            out = open("test_out/img%s.png" % i, "wb")
            img.save(out)
            img.show()


