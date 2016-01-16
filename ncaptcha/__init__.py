# -*- coding: utf-8 -*-

__author__ = 'barycenter'

import random
import string
import os

from PIL import Image, ImageDraw, ImageFont

file_path = os.path.realpath(__file__)
dir_path = os.path.dirname(file_path)


class Ncaptcha(object):
    def __init__(self, random_str='', code_len=4, image_suffix="png", background=(255, 255, 255), font_size=36):
        self.background = background
        self.random_str = random_str
        self.code_len = code_len
        self.draw = None
        self.image_suffix = image_suffix

        if not self.random_str:
            self.random_str = self.rnd_char(char_num=code_len)

        self.font_size = font_size
        self.size = None
        self.image = None

    def create(self):

        self.size = (int(self.font_size * (len(self.random_str)) + 10), int(self.font_size + 10))

        self.image = Image.new("RGBA", self.size, self.background)

        self.draw = ImageDraw.Draw(self.image)

        self.draw_text()

        self.draw_line()

        self.draw_transform()

        return self.image, self.random_str

    def rnd_color(self):
        return random.randint(100, 220), random.randint(100, 220), random.randint(100, 220)

    def rnd_char(self, charset=string.ascii_letters + string.digits, char_num=4):
        chars = []
        for i in range(char_num):
            chars.append(random.choice(charset))
        return ''.join(chars)

    def draw_text(self):
        font = ImageFont.truetype(os.path.join(dir_path, 'fonts/KBZipaDeeDooDah.ttf'), self.font_size)

        font_width, font_height = font.getsize(self.random_str)

        per_font_width = font_width / len(self.random_str)

        for c in range(0, len(self.random_str)):
            self.draw.text(((self.size[0] - font_width) / 2 + per_font_width * c + random.randint(-3, 3),
                            (self.size[1] - self.font_size) / 10 + random.randint(-5, 5)),
                           text=self.random_str[c], font=font, fill=self.rnd_color())

    def draw_line(self):

        pass

    def draw_transform(self):
        # image twist

        pass
