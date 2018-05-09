"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string S.

"""

def swap_case(s):
  mod_str = ''
  for i in s:
    if i.isupper():
      #print("upper===",i)    
      i = i.lower()
      mod_str += i 
    elif i.islower():
      #print("lower===",i)
      i = i.upper()
      mod_str += i
    else:
      #print("=======",i)
      mod_str += i
  
  #print(mod_str)           
  return mod_str
