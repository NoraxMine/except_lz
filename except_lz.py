import pandas as pd
import os

class Dates:


    def __init__(self, filename):
        self.filename = filename

    try:
       if os.path.isfile('var7.csv'):
           print("Файл существует")
       else:
           raise Exception
    except Exception:
        print("No file")      

    try:
        df = pd.read_csv('var7.csv')
        if len(df) != 0:
            print("В датафрейме есть данные")        
    except Exception:
        print("Датафрейм пуст")



    # def sort_of_dates(self, file_name):
    #     df = pd.read_csv(file_name)
    #     df['Дата оплаты'] = pd.to_datetime(df['Дата оплаты'], format='%d-%m-%Y')
    #     df_after = df.loc[df['Дата оплаты'] >= '2014-01-01']
    #     df_after.to_csv('after_2014.csv', index=False) 
    #     df['Дата оплаты'] = pd.to_datetime(df['Дата оплаты'], format='%d-%m-%Y')
    #     df_before = df.loc[df['Дата оплаты'] < '01-01-2014']
    #     df_before.to_csv('before_2014.csv', index=False) 
    # #Делаем из строки дату и сортируем до и после 2014 года
    
    def __del__(self):
        print('del done')
    #Del Done