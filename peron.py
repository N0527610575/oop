from builtins import print
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

class Student(Person):
    def __init__(self,name,age,city,student_id,grade):
        super().__init__(name,age,city)

        self.student_id = student_id
        self.grade = grade

    def study(self):
        # print(f"שלום אני{self.name} בן {self.age }מעיר{self.city}לומד בשכבה{self.grade}")
        print(f"{self.name}לומד בשכבה{self.grade}")

    def introdoce(self):
        super(introdoce(self))

    def advanc_grade(self):
        self.grade += 1



class Teacher(Person):
    def __init__(self,name,age,city,subject,years_expiriance):
        super().__init__(name,age,city)

        self.subject = subject
        self.years_expiriance = years_expiriance



    def teach(self):
        print(f"{self.name}מלמד{self.subject}כבר{self.years_expiriance}שנים")
    def introdoce(self):
        super().introdoce()
    def gain_expiriance(self,n):
        self.years_expiriance += n



class Principal(Person):
    def __init__(self,name,age,city,years_as_principal):
        super().__init__(name,age,city)
        self.years_as_principal = years_as_principal
    def manag(self):
        print(f"{self.name}מנהל כבר{self.years_as_principal}שנים")
    def add_managment(self,n):
        self.years_as_principal += n


s1 = Student("nahman",20,"hazor",20,8,)
t1 = Teacher("yedidya",30,"bney brak","target",10)
p1 = Principal("beni",34,"bney brak",9)

s1.study()
t1.teach()
p1.manag()
s1.advanc_grade()
t1.gain_expiriance(3)
p1.add_managment(8)

s1.study()
t1.teach()
p1.manag()

