# creating class

class Smartphone():
    Samsung = "blue"
    Iphone = "Sliver"

#method
def device(self):
    print("I love my phone")
# Object    
my_phone = Smartphone()
print(my_phone.Samsung)    

class Book():
    book1 = "Lord of the rings"
    book2 = "5 love languges"

# method
def Collection():
    print("Great book")

my_book = Book()
print(my_book.book1)

# defined class

class Superhero():
    Marvel = "Spiderman"

# method
def Ceb(self):
    print("my favourate Marvel hero")

#Obeject 
my_superhero = Superhero()
print(my_superhero.Marvel)

# construtor _init_
class Smartphone:
    def __init__(self, Samsung, Iphone):
        self.Samsung = Samsung #isntance variable
        self.Iphone = Iphone #instance varible
        self._charger = 2 # ADDED Encapulation

    def use_charger(self):
        if self._charger > 0:
            self._charger -= 1
            print("USB type c")
        else:
            print("Old charger not usable")     
#Obejects  
Phone1 = Smartphone("Blue", "Ink")
Phone2 = Smartphone("daek","Sliver")

print(Phone1.Samsung)
print(Phone2.Iphone)

usb = Smartphone(Samsung=2, Iphone=0)
usb.use_charger()

class Book:
    def __init__(self, book1, book2):
        self.book1 = book1
        self.book2 = book2
        self._PDF = 1000 # Encapulation
    def choose_PDF(self):
        if self._PDF > 10:
            self._PDF >= 2000
            print("PDF is cheaper_I will take it")
        else:
            print("collect touch copies")        

Collect = Book("1st Edition", "Last Edition")
Collect2 = Book("Singed", "not Singed")

print(Collect.book1)
print(Collect2.book2)

price = Book(book1=50, book2=50000)
price.choose_PDF()

class Superhero:
    def __init__(self, Marvel, Xman):
        self.Marvel = Marvel
        self.Xman = Xman
        self._Romantic = 2 # Movies only avalible
    def movie_By_number(self):
        if self._Romantic > 1:
            self._Romantic -=1
            print("Choose Romantic Movies")
        else:
            print("choose Superhero movies")       

Movie1 = Superhero("Ironman", "Hulk")
Movie2 = Superhero("Storm", "Professor")

print(Movie1.Marvel)
print(Movie2.Xman)

theater = Superhero(Marvel=2,Xman=1)
theater.movie_By_number()

#Ploymorphism Challenge 

class Lion:
    def move(self):
        return "four legs"
    
class Kangroo:
    def move(self):
        return "two legs"
# Polymorphism 
for animal in [Lion(), Kangroo()]:
    print(animal.move())        