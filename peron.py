class Person:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

    def introdoce(self):
        print(f"שלום אני  {self.name} בן {self.age}מהעיר{self.city}")

    def have_brithday(self):
        self.age += 1
p0 = Person("israel",23,"karmiel")
p1 = Person("yedidya",30,"bney brak")
p2 = Person("nahman",20,"safed")
p0.introdoce()
p1.introdoce()
p2.introdoce()
p1.have_brithday()
p1.introdoce()
class Mosad:
    def __init__(self,name,type,students_count,city):
        self.name= name
        self.type= type
        self.students_count = students_count
        self.city = city
    def print_details(self):
        print(f"שם המוסד{self.name} סוג{self.type}מסםר תלמידים{self.students_count}עיר{self.city}")
    def add_students(self,n):
        self.students_count += n



    def remove_students(self,n):
        if self.students_count >= n:

            self.students_count -= n
        else:
            print("אי אפשר פחות מ 0")
uiniversity = Mosad("kodkod",
                    "university",
                    250,
                    "bney brak")
talmud = Mosad("breslev",
               "talmud tora",
               75,
               "hazor")
uiniversity.print_details()
talmud.print_details()
talmud.add_students(50)
uiniversity.remove_students(20)
uiniversity.print_details()
talmud.print_details()




