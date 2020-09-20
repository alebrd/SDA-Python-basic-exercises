class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.area_(length, width)
        self.equal = self.equal_(length, width)

    def area_(self, length, width):
        return f'The area of the rectangle is {length * width}'

    def equal_(self, length, width):
        if length == width:
            return f'The Length: {length}, and the Width: {width}, are equal'


measures = Rectangle(19, 19)

print(measures.area)
print(measures.equal)
