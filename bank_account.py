from builtins import print


class Bank_account:
    def __init__(self,acoount_number,_account_folder,balanc):
        self.acoount_number = acoount_number
        self._account_folder = _account_folder
        self.__balanc = balanc
    def deposite(self,amount):
        self.__balanc += amount


    def wuthdrow(self,amount):
        if amount <= self.__balanc:
            self.__balanc -= amount


    def get_balanc(self):
        print( self.__balanc)

a1 = Bank_account("12","20",456)
a1.get_balanc()
class Vehicl :
    def __init__(self,color, model,speed):
        self.color = color
        self._model = model
        self.__speed = speed
    def accl (self,speed_de):
        self.__speed += speed_de
    def brea(self,speed_l):
        if self.__speed >= speed_l:
            self.__speed -= speed_l
    def get_speed (self):
        print(self.__speed)
    def get_color(self):
        print(self.color)

class Car(Vehicl):
    def __init__(self,color, model,speed,max_speed):
        super().__init__(color, model,speed)
        self.__max_speed = max_speed

    def accl(self,speed_de):
        if self.__speed + speed_de <= self.__max_speed:
            self.__speed += speed_de

    def get_max(self):
        print(self.__max_speed)


a2 = Car("red",1900,0,900)

class Digitalsaf:
    def __init__(self,saf_id,code):
        self.saf_id = saf_id
        self.__code = code
        self.__is_lock =  False
        self.__attemp_count = 0

    def reset_attem(self):
        self.__attemp_count = 0

    def try_unlock(self,code):
        if self.__attemp_count > 3:
            return False
        else:
            if code == self.__code:
                self.__is_lock = False
                self.reset_attem()
            else:
                self.__attemp_count += 1

    def lock(self):
        self.__is_lock = True
    def is_lock(self):
        return self.__is_lock


    def get_attem(self):
        print(self.__attemp_count)











