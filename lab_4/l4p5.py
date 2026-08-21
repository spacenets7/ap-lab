# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:14:59 2026

@author: maths
"""

feedback = input("Enter feedback: ")

positive = {"good", "excellent", "useful", "interesting", "helpful"}
negative = {"bad", "poor", "difficult", "boring", "confusing"}

words = feedback.lower().split()
pos = sum(word in positive for word in words)
neg = sum(word in negative for word in words)

print("Original Feedback:", feedback)
print("Total Number of Words:", len(words))
print("Positive Words:", pos)
print("Negative Words:", neg)

search = input("Enter a word to search: ").lower()
print("Occurrences:", words.count(search))

longest = max(words, key=len)
print("Longest Word:", longest)

old = input("Enter the word to replace: ")
new = input("Enter the new word: ")
print("Updated Feedback:", feedback.replace(old, new))

if pos > neg:
    print("Feedback Classification: Positive")
elif neg > pos:
    print("Feedback Classification: Negative")
else:
    print("Feedback Classification: Neutral")