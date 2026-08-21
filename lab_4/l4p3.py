# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:14:04 2026

@author: maths
"""

p = input("Enter a paragraph: ").lower()
words = p.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

while True:
    print("\n----- WORD ANALYZER -----")
    print("1. Display Total Number of Words")
    print("2. Display Unique Words")
    print("3. Display Frequency of Each Word")
    print("4. Display Most Frequent Word")
    print("5. Search for a Word")
    print("6. Display Repeated Words")
    print("7. Display Words in Alphabetical Order")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Total Number of Words:", len(words))

    elif choice == 2:
        print("Unique Words:")
        for word in freq:
            print(word)

    elif choice == 3:
        print("Word Frequency:")
        for word in freq:
            print(word, ":", freq[word])

    elif choice == 4:
        word = max(freq, key=freq.get)
        print("Most Frequently Occurring Word:", word)
        print("Frequency:", freq[word])

    elif choice == 5:
        word = input("Enter a word to search: ").lower()
        print(word, "occurs", freq.get(word, 0), "time(s)")

    elif choice == 6:
        print("Words Occurring More Than Once:")
        for word in freq:
            if freq[word] > 1:
                print(word, ":", freq[word])

    elif choice == 7:
        print("Words in Alphabetical Order:")
        for word in sorted(freq):
            print(word)

    elif choice == 8:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice")