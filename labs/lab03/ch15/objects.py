# Starting file for Lab 3 - objects.py
# James Kim, DEV 128, Lab 3, 10/24/2026

from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

# media class inherits from Product class and adds a format attribute
@dataclass
class Media(Product):
    format:str = ""

    def getDescription(self): # added format to the description of the media product
        return f"{Product.getDescription(self)} - {self.format}"

# book class inherits from Media class and adds an author attribute
@dataclass
class Book(Media):
    author:str = ""

    def getDescription(self):
        return f"{Media.getDescription(self)} by {self.author}"

# movie class inherits from Media class and adds a year attribute
@dataclass        
class Movie(Media):
    year:int = 0

    def getDescription(self):
        return f"{Media.getDescription(self)} ({self.year})"

# album class inherits from Media class and adds an artist attribute
@dataclass
class Album(Media):
    artist:str = ""

    def getDescription(self):
        return f"{Media.getDescription(self)} ({self.artist})"
