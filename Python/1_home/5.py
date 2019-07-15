# -*- coding: utf-8 -*-

__author__ = 'gkitg'


# Описать класс,  который  хранит список всех своих экземпляров,
# доступ к которому можно получить с помощью метода  getInstance().


class Singleton:
    """
    Здесь сохраняется экземпляр
    """
    __instance = []

    @staticmethod
    def getInstance():
        if Singleton.__instance == []:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != []:
            raise Exception('Этот класс singleton')
        else:
            Singleton.__instance = self


A = Singleton()
print(A)

# Singleton() # будет вызывать исключение

B = Singleton.getInstance()
print(B)

C = Singleton.getInstance()
print(C)