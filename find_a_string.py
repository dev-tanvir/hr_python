"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.
 
Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

"""

def count_substring(string, sub_string):
  counter=0
  i=0
  while i < len(string):
    if string.find(sub_string,i) >= 0:
      i=string.find(sub_string,i)+1
      counter+=1
    else: 
      break
  return counter
