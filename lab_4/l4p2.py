# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:13:37 2026

@author: maths
"""

s = input("Enter a sentence: ")

print("First Character:", s[0])
print("Last Character:", s[-1])
print("Total Number of Characters:", len(s))

words = s.split()
print("Number of Words:", len(words))

ch = input("Enter a character to count: ")
print("Number of occurrences of", ch, ":", s.count(ch))

old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("Sentence after replacement:", s.replace(old, new))

search = input("Enter a word to search: ")

if search.lower() in s.lower().split():
    print(search, "is present in the sentence.")
else:
    print(search, "is not present in the sentence.")

print("Words in the sentence:")
for word in words:
    print(word)