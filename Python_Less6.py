# Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().



class Animal:
    def voice(self):
        pass

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

charlie.voice()
vaska.voice()
teddy.voice()
