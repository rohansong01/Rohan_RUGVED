from abc import ABC, abstractmethod


class Shape(ABC):

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self):
        pass


class Square(Shape):
    def set_values(self, c, side):
        self.set_color(c)
        self.side = side

    def get_area(self):
        return self.side * self.side


sq = Square()
color = input("Enter the color: ")
side = int(input("Enter the length of side: "))
sq.set_values(color, side)
print("Color of square:", sq.get_color())
print("Area of square:", sq.get_area())