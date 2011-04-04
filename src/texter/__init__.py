### -*- coding: utf-8 -*- ####################################################

import os
import Image, ImageFont, ImageDraw

DRAW_ALIGN_LEFT = 'left'
DRAW_ALIGN_CENTER = 'center'
DRAW_ALIGN_RIGHT = 'right'

ARIAL_BOLD_FONT_FILE = os.path.join(os.path.dirname(__file__), 'fonts', 'arial_bold.ttf')
ARIAL_FONT_FILE = os.path.join(os.path.dirname(__file__), 'fonts', 'free_sans.ttf')


class Texter():

    text_align = DRAW_ALIGN_LEFT
    font_color = '000000'
    font_size = 15
    fill_color = False
    paragraph_indent = 6
    font_file = ARIAL_FONT_FILE

    padding = { 'left': 50, 'right': 50, 'top': 50, 'bottom': 50 }
    paragraph_margin = 5

    use_shadow = False
    shadow_color = (72, 72, 72)
    shadow_margins = (-2, 2)


    def __init__(self, **kwargs):
        self.set_config(**kwargs)

    def set_config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def draw_shadow(self, draw, f, string, x, y):
        draw.text((x + self.shadow_margins[0], y + self.shadow_margins[1]), string, font=f, fill=self.shadow_color)

    def draw_text_in_box(self, string, draw, box_coord, box_size, y_start=0):
        y_position = box_coord[1] + y_start
        words = []
        deffered = string.split(' ')
        deffered.reverse()
        f = ImageFont.truetype(self.font_file, self.font_size)
        while words or deffered:
            while f.getsize(' '.join(words))[0] < box_size[0] and deffered:
                words.append(deffered.pop())
            if f.getsize(' '.join(words))[0] > box_size[0] and len(words) > 1:
                deffered.append(words.pop())
            # drawing single line of text
            self.draw_text_line(' '.join(words), draw, (box_coord[0], y_position), box_size[0], f)
            y_position += f.getsize(' '.join(words))[1]
            words = []
            if y_position > box_coord[1] + box_size[1]:
                deffered.reverse()
                return ' '.join(deffered), 0

        return '', y_position < box_coord[1] + box_size[1] and y_position - box_coord[1]

    def draw_text_line(self, string, draw, coords, box_width, font):
        if font.getsize(string)[0] > box_width:
            x = coords[0] - (font.getsize(string)[0] - box_width)
        else:
            if self.text_align == DRAW_ALIGN_CENTER:
                x = coords[0] + (box_width - font.getsize(string)[0])/2
            elif self.text_align == DRAW_ALIGN_RIGHT:
                x = coords[0] + box_width - font.getsize(string)[0]
            else:
                x = coords[0]
        if self.use_shadow:
            self.draw_shadow(draw, font, string, x, coords[1])
        draw.text((x, coords[1]), string, font=font, fill=int(self.font_color, 16))

    def draw_chapter(self, text, canvas_size):
        pages = []
        paragraphs = text.splitlines()
        paragraphs.reverse()
        cur_paragraph = ''
        while paragraphs or cur_paragraph:
            page = Image.new("RGB", canvas_size)
            draw = ImageDraw.Draw(page)
            if self.fill_color:
                draw.rectangle([(0, 0), canvas_size], fill=self.fill_color)
            y_start = 1
            while y_start and (paragraphs or not paragraphs and cur_paragraph):
                cur_paragraph = cur_paragraph or ' ' * self.paragraph_indent + paragraphs.pop()
                cur_paragraph, y_start = self.draw_text_in_box(
                    cur_paragraph,
                    draw,
                    (self.padding['left'], self.padding['top']),
                    (canvas_size[0] - self.padding['right'] - self.padding['left'],
                     canvas_size[1] - self.padding['bottom'] - self.padding['top']),
                    y_start
                )
                y_start = y_start and y_start + self.paragraph_margin
            del draw
            pages.append(page)
        return pages