#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Birthday_Dictionary = {
    "Mahnoor" : '5th Nov',
    "Faizan" : '6th Nov',
    "Gabriel" : '5th Nov',
    "Swatti" : '6th Nov',
    "Heider" : '15th Nov',
}

for x in list(Birthday_Dictionary.keys()):
  print(x)
print(Birthday_Dictionary.get(input("Who's birthday would you like to know? "),"sry not in our list"))

if input("Would you like to append the dictionary? ").lower() == 'y':
  while True:
    name = input("please enter the name ")
    bday = input("Please enter the date of birth ")
    Birthday_Dictionary[name]= bday
    x = input("Would you like to add more? ").lower()
    if x == 'n':
      break

keys = list(Birthday_Dictionary.keys())
values = list(Birthday_Dictionary.values())

Bdayfile = open("Bday_file.txt",'w')
for i in range(0,len(keys),1):
  Bdayfile.writelines(keys[i] + ':' + values[i])
  Bdayfile.write('\n')
Bdayfile.close()

months = []

for x in values:
  months.append(x.split(" ")[1])

from collections import Counter
c = Counter(months)

for i in list(c.keys()):
  print("In the month of {}, there are {} birthdays ".format(i,c[i]))

from bokeh.plotting import figure, show, output_file
from bokeh.io import output_notebook
output_notebook()

x = list(c.keys())
y = list(c.values())
p=figure(x_range = x)
p.vbar(x = x,top = y,width = 0.5)
show(p)

