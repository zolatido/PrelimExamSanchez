class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        area = self.side * self.side
        return area

    def perimeter(self):
        perimeter = self.side + self.side + self.side + self.side 
        return perimeter

    def printoutput(self):
        squareArea = self.area()
        squarePerimeter = self.perimeter()
        print("Area of the square with a side of " + str(self.side) + " is " + str(squareArea))
        print("Perimeter of the square with a side of " + str(self.side) + " is " + str(squarePerimeter))

area1 = Square(2)
area1.printoutput()




