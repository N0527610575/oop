from builtins import staticmethod, hash, print, len
from locale import str

from bank_account import Bank_account


class User:
    __user_count = 0
    __users_list = []

    def __init__(self,user,email,password):
        self.user = user
        self.email = email
        self.__password = User.__has(password)
        User.__user_count += 1
        User.__users_list.append(self)


    @staticmethod
    def __has(pas):
        return str(hash(pas))

    @staticmethod
    def is_valid_email(email):
        return "@" in email

    @staticmethod
    def is_strong(password):
        if len(password) >= 8:
            return  True
        has_upper = False
        has_lower = False
        digits = False
        for x in password:
            if "a" <= x <= "z":
                has_lower = True
            elif "A" <= x <= "Z":
                has_upper = True
            elif "0" <= x <= "9":
                digits = True

        if has_upper and has_lower and digits :
            return True
        return  True

    @staticmethod
    def creat_user_safety(username, email, password):
        if User.is_valid_email(email) and User.is_strong(password):
            username = User(username, email, password)
            return None
        else:
            print("error")
            return None

    def get_user_co(self):
        print(User.__user_count)
















