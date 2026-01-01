'''
Escribe un programa en Python para convertir
una cadena a datetime.
'''
from datetime import datetime
date_string = 'Jan 1 2014 2:43PM'
date_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(date_object)
#INPUT: Jan 1 2014 2:43PM
#OUTPUT: 2014-07-01 14:43:00