# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:15:24 2026

@author: maths
"""

summary = input("Enter the resume summary: ")

skills = ["python", "java", "sql", "html", "communication"]
text = summary.lower()
words = summary.split()

found = [skill for skill in skills if skill in text]

print("Original Resume Summary:", summary)
print("Total Number of Words:", len(words))
print("Skills Found:")

for skill in found:
    print(skill)

print("Number of Skills Found:", len(found))

search = input("Enter a skill to search: ").lower()

if search in text:
    print(search, "is present in the resume.")
else:
    print(search, "is not present in the resume.")

print("Longest Word:", max(words, key=len))

old = input("Enter the skill to replace: ")
new = input("Enter the new skill: ")
updated = summary.replace(old, new)
print("Updated Resume Summary:", updated)

if len(found) >= 4:
    print("Resume Classification: Highly Matched")
elif len(found) >= 2:
    print("Resume Classification: Partially Matched")
else:
    print("Resume Classification: Not Matched")