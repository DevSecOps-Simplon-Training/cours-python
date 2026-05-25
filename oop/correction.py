# ============================================================
# Corrections des exercices POO
# ============================================================


# ------------------------------------------------------------
# Encapsulation — User (version 1 : getters/setters manuels)
# ------------------------------------------------------------

class User:
    def __init__(self, profil):
        self.profil = profil
        self._password = ""
        self._user_name = ""
        self.__validation_code = "AB2X"

    def set_password(self, new_password):
        self._password = new_password

    def get_password(self):
        return self._password

    def get_user_name(self):
        return self._user_name

    def __check_validation_code(self, code):
        return code == self.__validation_code

    def set_user_name(self, code, user_name):
        if self.__check_validation_code(code):
            self._user_name = user_name
        else:
            print("error code")


# ------------------------------------------------------------
# Encapsulation — User (version 2 : @property)
# ------------------------------------------------------------

class UserBis:
    def __init__(self, profil, password="", code_value=("AB2X", "")):
        self.profil = profil
        self.password = password
        self.__validation_code = "AB2X"
        self.user_name = code_value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, code_value):
        code, value = code_value
        if self.__check_validation_code(code):
            self._user_name = value
        else:
            print("error code")

    def __check_validation_code(self, code):
        return code == self.__validation_code


# ------------------------------------------------------------
# Héritage & classes abstraites — Zoo
# Référence : https://github.com/OpenClassrooms-Student-Center/
#             7150626-Apprenez-la-programmation-orientee-objet-avec-Python
# ------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def manger(self):
        pass


class Felin(Animal, metaclass=ABCMeta):
    def manger(self, value):
        if value == "viande":
            print("le félin est nourri")
        else:
            print("cela ne correspond pas à un félin")


class Poisson(Animal, metaclass=ABCMeta):
    def manger(self, value):
        if value == "nourriture pour poisson":
            print("le poisson est nourri")
        else:
            print("cela ne correspond pas à un poisson")

    @abstractmethod
    def nager(self):
        pass


class Oiseau(Animal, metaclass=ABCMeta):
    def manger(self, value):
        if value == "graine":
            print("l'oiseau est nourri")
        else:
            print("cela ne correspond pas à un oiseau")

    @abstractmethod
    def piailler(self):
        pass


class Lion(Felin):
    def rugir(self):
        print("RRRRRrrrr")


class Chat(Felin):
    def miauler(self):
        print("Miaou")


class Panthere(Felin):
    pass


class Canari(Oiseau):
    def piailler(self):
        print("cuicui")


class Autruche(Oiseau):
    def piailler(self):
        print("CUICUI")


class Raie(Poisson):
    def nager(self):
        pass


class Dauphin(Poisson):
    def nager(self):
        pass
