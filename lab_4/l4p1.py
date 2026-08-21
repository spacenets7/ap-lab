# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:09:08 2026

@author: maths
"""

s = input("Enter a string: ")

print("Original String:", s)
print("Length of String:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

vowels = "aeiouAEIOU"
v = c = d = sp = 0

for ch in s:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch.isspace():
        sp += 1

print("Number of Vowels:", v)
print("Number of Consonants:", c)
print("Number of Digits:", d)
print("Number of Spaces:", sp)
print("Reversed String:", s[::-1])

if s == s[::-1]:
    print("The string is a Palindrome")
else:
    print("The string is Not a Palindrome")