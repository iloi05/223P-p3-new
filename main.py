# Name: Ivy Loi
# Date: 9/22/25
# Purpose: Implement functions that were created in contacts.py

from contacts import *

contacts = {}

while True:
    print("     *** EMPLOYEE CONTACT MAIN MENU")
    print()
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit program")
    print()
    prompt = input("Enter menuc choice: ")
    if prompt == "1":
        num = input("Enter phone number: ")
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        add_contact(contacts, id, first_name  = first, last_name = last)
    elif prompt == "2":
        num = input("Enter phone number: ")
        new_first = input("Enter first name: ")
        new_last = input("Enter last name: ")
        modify_contact(contacts, id, first_name = new_first, last_name = new_last)
        print("Modified: {new_first}{new_last}")
    elif prompt == "3":
        num = input("Enter phone number: ")
        delete_contact(contacts, id)
    elif prompt == "4":
        