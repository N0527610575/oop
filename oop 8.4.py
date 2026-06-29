class Rectangle:

    def __init__(self, width, height):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("שגיאה: רוחב שלילי")
        else:
            self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("שגיאה: גובה חייב להיות חיובי")
        else:
            self._height = value


    @property
    def area(self):
        return self._width * self._height


    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


    @property
    def is_square(self):
        return self._width == self._height


    @staticmethod
    def create_square(side):
        return Rectangle(side, side)


    @staticmethod
    def compare_areas(rect1, rect2):
        if rect1.area > rect2.area:
            return "ראשון גדול יותר"
        elif rect2.area > rect1.area:
            return "השני גדול יותר"
        else:
            return "שני המלבנים שווים"