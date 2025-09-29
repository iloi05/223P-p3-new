# Name: Ivy Loi
# Date: 9/22/25
# Purpose: Implement functions that were created in contacts.py

from contacts import *

contacts = {}
choices = ["1", "2", "3", "4", "5", "6"]

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
    prompt = input("Enter menu choice: ")
    if prompt == "1":
        num = input("Enter phone number: ")
        if not is_int(id = num):
            print("That is not a valid phone number.")
            continue
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        add_contact(contacts, id = num, first_name  = first, last_name = last)
    elif prompt == "2":
        num = input("Enter phone number: ")
        if not is_int(id = num):
            print("That is not a valid phone number.")
            continue
        new_first = input("Enter first name: ")
        new_last = input("Enter last name: ")
        modify_contact(contacts, id = num, first_name = new_first, last_name = new_last)
        print("Modified: {} {}".format(new_first, new_last))
    elif prompt == "3":
        num = input("Enter phone number: ")
        if not is_int(id = num):
            print("That is not a valid phone number.")
            continue
        delete_contact(contacts, id = num)
    elif prompt == "4":
        print_contact(contacts)
    elif prompt == "5":
        if not contacts:
            print("The list is empty currently, no contacts found .... returning to main menu")
            continue
        search = input("Enter search string: ")
        find_contact(contacts, find = search)
    if prompt == "6":
        break
    if prompt not in choices:
        print("You've chosen an invalid option try again")
        continue