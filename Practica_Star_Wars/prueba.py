import pandas as pd
from IPython.core.display_functions import display

'''
s1 = pd.Series([4, 9, 10], index=('b', 1, 'c', ), name='precios')
print(s1)
print (s1['b'])
print (s1.array)
print (s1.to_numpy())

df = pd.DataFrame([{'col1': 1, 'col2': 2},  {'col1': 3, 'col3': 5}], index=['row1', 'row2'])
#print(df.columns[2])
#display(df)
#print (df)

df = pd.DataFrame({'peras':{'enero':10, 'febrero':20, 'marzo':7},
                'manzanas':{'enero':4, 'febrero':9, 'marzo':3},
                'uvas':{'enero':5, 'febrero':12, 'marzo':6}})
display(df)

df = pd.DataFrame({'peras':[10,20,7], 'manzanas':[4,9,3], 'uvas':[5,12,6]}, index=('enero', 'febrero', 'marzo'))
display(df)


df = pd.DataFrame({'enero':[10,4,5], 'febrero':[20,9,12], 'marzo':[7,3,6]}, columns=('peras', 'manzanas', 'uvas'))
display(df)
'''

from colorama import Fore, Style, init
init()

print(Fore.RED + Style.BRIGHT+ "Error" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + Style.BRIGHT+ "Error" + Style.RESET_ALL)
print("hola")
print(Fore.GREEN + "Correcto" + Style.RESET_ALL)

df = pd.DataFrame({"Nombre": "helena", "Edad": 20})
df.query()
print(df)
print(df)

