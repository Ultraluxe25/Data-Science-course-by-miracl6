'''
Вам дан DataFrame, который записан в переменную df. Подсчитайте количество пропусков в каждом столбце,
 записав код с подсчетом в переменную count_fill в виде Series.
'''

# import pandas as pd


# df = pd.DataFrame({'ID': {0: 5524, 1: 2174, 2: 4141},
#                    'Z_CostContact': {0: 3, 1: None, 2: 3},
#                    'Marital_Status': {0: 'Single', 1: 'Single', 2: 'Together'},
#                    'MntFruits': {0: None, 1: 1, 2: None},
#                    'MntMeatProducts': {0: None, 1: 6, 2: 127},
#                    'MntFishProducts': {0: 172, 1: 2, 2: 111}})

count_fill = df.isna().sum()