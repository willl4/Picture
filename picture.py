"""
picture.py
Author: Will Laycock
Credit: made by me

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
black = Color(0x000000, 1.0)
red = Color(0xff0000, 1.0)
white = Color(0xffffff, 1.0)
yellow = Color(0xffff00, 1.0)

thinline = LineStyle(1, black)

rectangle1 = RectangleAsset(300, 250, thinline, red)
rectangle2 = RectangleAsset(50,100, thinline, black)
poly = PolygonAsset([(400,200), (550,50), (700, 200)], thinline, black)
square = RectangleAsset(50,50, thinline, yellow)
ellipse = EllipseAsset(25,12.5, thinline, yellow)
circle = CircleAsset(2.5, thinline, white)

Sprite(rectangle1, (400,200))
Sprite(rectangle2, (525,350))
Sprite(rectangle2, (625,100))
Sprite(poly)
Sprite(square, (437.5,350))
Sprite(square, (437.5,250))
Sprite(square, (525,250))
Sprite(square, (612.5,350))
Sprite(square, (612.5,250))
Sprite(ellipse, (550,225))
Sprite(circle, (565,397.5))
# add your code here /\  /\  /\


myapp = App()
myapp.run()
