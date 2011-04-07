### -*- coding: utf-8 -*- ####################################################

import unittest
import os
import Image

import sys

try:
    import texter
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    import texter


class TestRectTextDraw(unittest.TestCase):

    def test_magazine_title(self):
        result_filename = os.path.join(os.path.dirname(__file__), 'output', 'magazine_cover.png')
        tt = texter.Texter(font_color=(255, 0, 0))
        cover_tmpl = Image.open(os.path.join(os.path.dirname(__file__), 'template.png'))
        tt.rect_text(cover_tmpl, (265, 170, 395, 240), 'Lorem ipsum')
        cover_tmpl.save(result_filename, "PNG")



if __name__ == '__main__':
    unittest.main()