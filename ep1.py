Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('helloworld')
helloworld
>>> name = 'aod'
>>> lastname = 'aed aed'
>>> fullname = name + ' ' + lastname
>>> print(fullname)
aod aed aed
>>> print('my name is {}' .format(fullname))
my name is aod aed aed
>>> print(f'mu name is' {fullname})
SyntaxError: invalid syntax
>>> print(f'my name is {fullname}')
my name is aod aed aed
>>> money = 1234
>>> print(f'i have money: {money:,d}')
i have money: 1,234
>>> print(f'i have money: {money}')
i have money: 1234
>>> 
