"""
1) Определите класс Person, в котором определите свойства (динамические переменные) name и birth_date, а также метод get_year. 

name - это имя, тип str
birth_date - это дата рождения, тип str
метод get_year на основании даты рождения возвращает год рождения, возвращаемое значение типа int
2) Определите класс Student, который будет являться дочерним классом от Person и унаследует все атрибуты данного класса. Определите дополнительно в Student:

свойство subject - предмет на курсе, тип str
метод get_age - получение возраста на основании года=2022 (приблизительный подсчет), возвращаемое значение типа int
метод get_info - получение информации о студенте в виде словаря, возвращаемое значение типа dict
Вид возвращаемого словаря в методе get_info:

{'Name_student': name, 'Age': age, 'Subject': subject}

где name, age, subject - это атрибуты.

 

После определения класса Student определите объект класса (экземпляра класса), закрепив за ним название переменной student,
в качестве аргументов подайте следующие значения:

name='Fedor'
birth_date='01-01-2002'
subject='Python'
Переменной result присвойте вызов метода get_info экземпляра класса  student.

 

Пример на основании данных:

name='Katy'
birth_date='02-01-1993'
subject='Math'
Что будет храниться в result в результате выполнения программы:

{'Name_student': 'Katy', 'Age': 29, 'Subject': 'Math'}
 

Примечания:

Для того, чтобы получить год из строки с датой, воспользуйтесь методом в уроке "Переменные и типы данных" на 2 шаге.
Полученное значение года рождения должно быть по итогу типа int
Чтобы получить возраст, необходимо вычесть из 2022 год рождения
"""

class Person:
    def __init__(self, name: str, birth_date: str):
        self.name = name
        self.birth_date = birth_date 
        
    def get_year(self) -> int:
        return int(self.birth_date[6:])
    
    
class Student(Person):
    def __init__(self, name: str, birth_date: str, subject: str):
        super().__init__(name, birth_date)
        self.subject = subject
    
    def get_age(self) -> int:
        return 2022 - self.get_year()
    
    def get_info(self) -> dict:
        return {'Name_student': self.name, 'Age': self.get_age(), 'Subject': self.subject}
    

student = Student(name='Fedor', birth_date='01-01-2002', subject='Python')
result = student.get_info()
