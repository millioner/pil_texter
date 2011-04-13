Small module for drawing text with PIL
======================================

It is created for two purposes:

* drawing text in a rectangle area with auto font size
* drawing large texts with page creating and paragraph support

Usage
-----

Module provides a class named Texter. When you create this class you can set a lot of params in it:

* `text_align` - text align, at the moment can have one of three predefined values - `texter.DRAW_ALIGN_LEFT`(default), `texter.DRAW_ALIGN_CENTER` and `texter.DRAW_ALIGN_RIGHT`

* `font_color` - a tuple with three elements in it. For color definition according to RGB. By default it equals `(0, 0, 0)`

* `font_size` - an integer font size value. By default it equals `15`

* `fill_color` - color for page background. It is a tuple with three elements in it. For color definition according to RGB. By default it is `False`

* `paragraph_indent` - count of spaces which will be prepended to each paragraph for simulating first line indent. Default value - `6`

* `font_file` - full path to font file, that will be used for drawing. By default it is 'arial.ttf', included to the module.

* `padding` - a dictionary with page padding values. By default it equals `{ 'left': 50, 'right': 50, 'top': 50, 'bottom': 50 }`

* `paragraph_margin` - an integer value defines free space between paragraphs. Default value - `5`

* `use_shadow` - a boolean value indicates using shadow effect for text. Default value - `False`

* `shadow_color` - color of the text shadow. It is a tuple with three elements in it. For color definition according to RGB. By default it equals `(72, 72, 72)`

* `shadow_offsets` - an offsets used for shadow drawing. Default - `(-2, 2)`

### Function `texter.Texter.rect_text(image, rect, text)`

Provides drawing small text string in a rectangle area.

* image - an Image instance
* rect - the 4-tuple that defines a region, where coordinates are (left, upper, right, lower)
* text - a string to draw it in the box

You can see usage example in file texter/tests/draw_rect_text_test.py This file also can be executed and generated image will appear at the tests/output folder

### Function `texter.Texter.draw_chapter(text, canvas_size)`

Provides drawing large text chapter with pages generating.

Returns a list of Image instances.

* canvas_size - a tuple with two integer elements (width, height) which defines a page size

You can see usage example in file texter/tests/draw_chapter_test.py This file also can be executed and all generated images will appear at the tests/output folder