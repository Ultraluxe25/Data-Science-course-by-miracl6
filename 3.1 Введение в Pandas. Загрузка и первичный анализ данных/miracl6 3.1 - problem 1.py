"""
Импортируйте библиотеку pandas и через алиас назначьте псевдоним pd. В переменную values запишите следующие значения:

 (1, 2, 10, 'python', 'data science')

В переменную indexes запишите список из значений типа int от 0 до 5 (не включительно). Всего в списке должно быть 5 элементов.

Используя переменные values и indexes, создайте pandas.Series записав в переменную data_series, где в качестве параметра data в Series будет переменная values,
а в качестве параметра index переменная indexes.
"""

import pandas as pd

values = (1, 2, 10, 'python', 'data science')
indexes = list(range(5))
data_series = pd.Series(data=values, index=indexes)
