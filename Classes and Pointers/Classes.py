# A class is a blueprint of Objects. A class can consist of a constructor.
# Constructor in python are defined by __init__ method.
# Every method within a class always has a 'self' parameter
# This 'self' parameter is nothing but an instance of the class (object)
# Every class name in python starts with capital letter 
class Cookie:
    def __init__(self,color):
        self.color = color

cookie_one = Cookie("green") 
'''
By passing green as a color. This particular object 'cookie_one' will have the color of green
'''

