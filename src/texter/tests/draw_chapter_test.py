### -*- coding: utf-8 -*- ####################################################

import unittest
import os

import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


import texter

class TestChapterDraw(unittest.TestCase):



    def test_shuffle(self):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed luctus molestie enim quis placerat. Pellentesque molestie lectus eu nisi commodo bibendum. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam tellus elit, fermentum ut scelerisque vitae, interdum vehicula mi. Quisque id nulla purus. Phasellus porttitor leo ut ipsum dapibus vel lacinia dolor semper. Quisque ante purus, volutpat id viverra et, accumsan in mi. Suspendisse potenti. Aliquam commodo, lorem at molestie consectetur, purus odio gravida quam, vel luctus sem mauris ut ante. Fusce convallis, ipsum quis placerat cursus, ligula neque iaculis metus, non lacinia neque elit et quam. Etiam et nulla in arcu consequat ornare. Nam augue augue, dictum ac mollis ut, egestas sit amet felis.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer varius massa ut urna aliquet rutrum. Nunc faucibus metus id nibh sollicitudin id vehicula arcu convallis. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed et vehicula magna. Vestibulum dui felis, euismod lacinia fermentum vitae, mattis et augue. Sed pharetra sapien quis odio lobortis convallis. Sed vel viverra erat. Donec tincidunt, magna in consequat iaculis, metus diam auctor mi, in blandit ligula purus vitae nulla. Maecenas ultrices ligula sit amet arcu fringilla pulvinar. Quisque felis urna, tempus id imperdiet a, feugiat sit amet magna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Duis lectus nibh, pulvinar dapibus tincidunt nec, feugiat interdum tortor. Sed eget risus ultrices augue aliquam volutpat.
Integer sem augue, porttitor vulputate pellentesque non, sagittis a dui. Ut ac augue eget ante accumsan pretium. Quisque vulputate cursus felis, sit amet pretium orci tristique ut. Fusce in ligula lacus. Ut lobortis tincidunt euismod. Fusce condimentum lectus tempor felis feugiat id consequat sem consectetur. Phasellus rhoncus iaculis urna, sed dapibus nisl fermentum eu. Integer tincidunt est vel dui sagittis hendrerit. Donec ut velit non eros euismod pretium. Mauris nec sem in lectus tempor ultrices. Quisque nulla quam, sagittis at viverra id, dictum id lectus. Donec aliquet augue ligula. Vivamus nisi velit, convallis a varius sit amet, sodales id ipsum. Nulla blandit tempus gravida. Vivamus erat mi, rhoncus vitae adipiscing a, dapibus eleifend lorem. Integer sem risus, fermentum eget egestas a, convallis quis urna. In eu urna a ipsum scelerisque dictum. Vivamus est sem, euismod a dignissim nec, venenatis in nibh. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi quis lorem neque.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec mollis dignissim quam et ultricies. Sed tempor urna eu nisl porta ut aliquet tortor varius. Donec sollicitudin, eros eget ornare commodo, leo erat dapibus nunc, a imperdiet purus magna ut diam. Phasellus a magna euismod lorem iaculis ultricies. In quis augue id ligula posuere dapibus. Nulla fermentum libero ut velit egestas ullamcorper. Suspendisse potenti. Etiam eget ipsum at eros commodo ullamcorper. Fusce mollis malesuada neque non accumsan.
Praesent venenatis laoreet justo, id convallis diam varius sed. In convallis tortor vel nibh dapibus ac feugiat sem pulvinar. Curabitur sapien libero, interdum a auctor quis, porttitor sed dui. Morbi pulvinar dignissim diam, a vulputate tortor commodo vitae. Nam viverra lacus eget massa gravida eu lacinia orci viverra. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque tellus tortor, tempus eget gravida non, gravida vel velit. Vestibulum neque tellus, feugiat vitae vulputate sit amet, auctor non sem. Aliquam accumsan placerat ligula faucibus consequat. Sed eget justo felis, eget euismod mi.
        """
        tt = texter.Texter(fill_color='white')
        i = 0
        dirname = os.path.join(os.path.dirname(__file__), 'output')
        for page in tt.draw_chapter(text, (300, 500)):
            page.save(os.path.join(dirname, "test_%s.png" % i), 'PNG')
            i += 1


if __name__ == '__main__':
    unittest.main()