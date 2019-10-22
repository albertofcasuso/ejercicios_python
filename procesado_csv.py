import pandas
import os
import time

while True:
    if os.path.exists('files/temps-today.csv'):
        data = pandas.read_csv('files/temps-today.csv')
        print(data.mean()['st2'])
        break
    else:
        print('No existe')
    time.sleep(5)
