import random
class Animal:
    def __init__(self,legs,color,digsys,suns,race,colortail ):
        self.legs = legs
        self.color = color
        self.digsys = digsys
        self.suns = suns
        self.race = race
        self.colortail = colortail

        self.tail = None

    def add_tail(self,tail):
        self.tail =tail


animal = Animal(legs=4,digsys="good",color = "red",suns=6,race="italian",colortail="black",)
class Tail:
    def __init__(self,length, thickness, speed):
        self.length = length
        self.thickness = thickness
        self.speed =speed

class Cat(Animal):
    def __init__(self,color,length_wih):



        super().__init__(legs=4,color=color,digsys="good",suns=6,race="italian",colortail="black")
        self.length_wih = length_wih
        self.mice_counter = 0

    def mice_hunted_get (self):
        return self.mice_counter
    def  mouse_hunt (self):
        self.mice_counter += 1
        print("החתול צד עכבר")
cat_a = Cat(color="White",length_wih=10)
cat_b = Cat( color="Black",length_wih= 15)

print(cat_a.legs)
print(cat_a.color)
print(cat_b.color)











