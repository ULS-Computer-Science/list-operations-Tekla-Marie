#ALL OF lIELESSSXMDSLcelcndkcdncekn

#---------- .append() ----------

dogs = ['Corgi', 'Retriever', 'Border Collie']
dogs.append('Pekines')

#---------- .insert() ----------

cats = ['Maine Coon', 'Chartreux', 'Norwegian Forest']
cats.insert(2, 'Selkirk Rex')

#---------- .remove() ----------
#---------- .count() -----------

what = ['Mouse', 'Heart', 'Pit of fire', 'Mouse']
print(what.count('Mouse'))
what.remove('Mouse')

#--------- .extend() -----------

author = ['book', 'map', 'scroll']
writing_utensils = ['pen', 'pencil', 'quill']
author.extend(writing_utensils)

#--------- .pop() --------------

import sys
import time
import random

def write(text, delay = 0.03): #delay text appearances by 0.05 seconds
    for char in text:
        sys.stdout.write( char)
        sys.stdout.flush()
        time.sleep(delay)

VIP_Guests = ['Zlata', 'Liam', 'Angel', 'Pan', 'Hunter', 'Terry', 'Donovan',
              'Eli', 'Wyatt', 'Talson', 'Mrs. Peterson']

write(f'These are the people in the room:\n')
print(VIP_Guests)
time.sleep(3)
write(f'A random person will now be removed!\n')
time.sleep(1)
person = random.randint(0, len(VIP_Guests),)
kicked_out = VIP_Guests.pop(person)
write(f"{kicked_out} was removed from the party\n")
write(f'As seen in the list below:\n')
print(VIP_Guests)

#--------- .del() --------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del numbers [0:4]

#-------- .index() -------------

shakes = ['strawberry', 'vanilla', 'chocolate', 'mango', 'vanilla']
x = shakes.index('vanilla')
print(x)

#-------- .copy() --------------

hats = ['Fedora', 'Sombrero', 'straw hat']
backuphats = hats.copy()

#-------- random.choice() ------
import random

kids = ['Albinoe', 'Orchid', 'Nembrotha', 'Equinox', 'Borealis']
most_evil = random.choice(kids)
print('Most evil kid: ' + most_evil)

#-------- nesting -------------

nest = [[kids], [shakes]]

#-------- .sort() -------------
#-------- .reverse() ----------
#-------- list on line 54 -----

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)






