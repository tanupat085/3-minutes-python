Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> car = []
>>> car.append('Honda')
>>> car.append('Toyota')
>>> car.append('Mizzu')
>>> print(car)
['Honda', 'Toyota', 'Mizzu']
>>> car.remove('Honda')
>>> print(car)
['Toyota', 'Mizzu']
>>> print(car[0])
Toyota
>>> del car[0]
>>> print(car)
['Mizzu']
>>> car[0] = 'aoddod'
>>> print(car)
['aoddod']
>>> 
