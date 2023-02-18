'''
Вам дан DataFrame, который записан в переменную df.

Удалите столбцы 'ID', 'Z_CostContact', запишите результат в новую переменную df_new.
Переименуйте следующие колонки в df_new на основании словаря dict_rename, 
не забудьте про параметр inplace, чтобы изменения прошли без дополнительного присваивания.

dict_rename = {
    'MntFruits': 'sum_fruits',
    'MntMeatProducts': 'sum_meat',
    'MntFishProducts': 'sum_fish'
}

'''

# import pandas as pd


# df = pd.DataFrame({'ID': {0: 5524, 1: 2174, 2: 4141},
#                    'Z_CostContact': {0: 3, 1: 3, 2: 3},
#                    'Marital_Status': {0: 'Single', 1: 'Single', 2: 'Together'},
#                    'MntFruits': {0: 88, 1: 1, 2: 49},
#                    'MntMeatProducts': {0: 546, 1: 6, 2: 127},
#                    'MntFishProducts': {0: 172, 1: 2, 2: 111}})

# dict_rename = {
#     'MntFruits': 'sum_fruits',
#     'MntMeatProducts': 'sum_meat',
#     'MntFishProducts': 'sum_fish'}


df_new = df.drop(labels=['ID', 'Z_CostContact'], axis=1)
df_new.rename(columns=dict_rename, inplace=True)