"""
Определите класс Person, в котором определите свойства (динамические переменные) name и birth_date, а также метод get_year. 

name - это имя, тип str
birth_date - это дата рождения, тип str
метод get_year на основании даты рождения получает год рождения, возвращаемое значение типа int
После определения класса, определите объект класса (экземпляра класса), закрепив за ним название переменной person,
в качестве аргументов подайте следующие значения:

name='Fedor'
birth_date='01-01-2002'
Переменной year присвойте вызов метода get_year экземпляра класса  person.

 

Примечание:

Для того, чтобы получить год из строки с датой, воспользуйтесь методом в уроке "Переменные и типы данных" на 2 шаге.
Полученное значение года рождения должно быть по итогу типа int. 
"""

class Person:
    def __init__(self, name: str, birth_date: str):
        self.name = name
        self.birth_date = birth_date
        
    def get_year(self) -> int:
        return int(self.birth_date[6:])
        
    
name = 'Fedor'
birth_date = '01-01-2002'

person = Person(name, birth_date)
year = person.get_year()
