# Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод родительского класса Animal, который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.



class Animal:
    numOfInstans = 0

    def __init__(self):
        Animal.numOfInstans += 1

    def voice(self):
        pass

#выводит кол. созданых экземпляров
    @staticmethod
    def countOfInstans():
        print(f'{Animal.numOfInstans}')


class Dog(Animal):
    def voice(self):
        print('Гаф')


class Cat(Animal):
    def voice(self):
        print('Мяу')


class Bull(Animal):
    def voice(self):
        print('Му-у')


charlie = Dog()
vaska = Cat()
teddy = Bull()

# charlie.voice()
# vaska.voice()
# teddy.voice()
# print()

Animal.countOfInstans()
