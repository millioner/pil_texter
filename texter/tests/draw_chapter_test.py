### -*- coding: utf-8 -*- ####################################################

import unittest
import os

import sys

try:
    import texter
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    import texter

class TestChapterDraw(unittest.TestCase):

    def test_chapter(self):
        dirname = os.path.join(os.path.dirname(__file__), 'output')
        f = open(os.path.join(os.path.dirname(__file__), 'lorem_ipsum.txt'), 'r')
        tt = texter.Texter(fill_color='white', font_size=16)
        i = 0
        for page in tt.draw_chapter(f.read().decode('utf-8'), (300, 500)):
            page.save(os.path.join(dirname, "test_%s.png" % i), 'PNG')
            i += 1


if __name__ == '__main__':
    unittest.main()