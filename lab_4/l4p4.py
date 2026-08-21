# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:14:32 2026

@author: maths
"""

p = input("Enter a password: ")

conditions = []

if len(p) < 8:
    conditions.append("Password must contain at least 8 characters.")

if not any(ch.isupper() for ch in p):
    conditions.append("Password must contain at least one uppercase letter.")

if not any(ch.islower() for ch in p):
    conditions.append("Password must contain at least one lowercase letter.")

if not any(ch.isdigit() for ch in p):
    conditions.append("Password must contain at least one digit.")

if not any(not ch.isalnum() and not ch.isspace() for ch in p):
    conditions.append("Password must contain at least one special character.")

if any(ch.isspace() for ch in p):
    conditions.append("Password must not contain spaces.")

if conditions:
    print("Password is Invalid")
    print("Conditions not satisfied:")
    for condition in conditions:
        print("-", condition)
else:
    print("Password is Valid")