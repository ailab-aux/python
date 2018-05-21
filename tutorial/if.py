#!/usr/bin/env python3

# if statement.
# if语句

x = int(input('Please enter an integer: '))
if x < 0:
  x = 0
  print('Negative changed to zero')
elif x == 0:
  print('Zeor')
elif x == 1:
  print('Single')
else:
  print('More')