# Name: Ivy Loi
# Date: 9/21/25
# Purpose of file: Create contact list functions that will be used in main file

def print_contact(contact_dict):
    if not contact_dict:
        print("The list is empty, put a name in first")
    else:
        print("")

def add_contact(contact_dict, /, *, id, first_name, last_name):
    if id in contact_dict:
        return "error"
    contact_dict[id] = [first_name, last_name]
    return contact_dict[id]

def modify_contact(contact_dict, *, id, first_name, last_name):
    if id not in contact_dict:
        return "error"
    contact_dict[id] = [first_name, last_name]
    return contact_dict[id]

def delete_contact(contact_dict, *, id):
    if id not in contact_dict:
        return "error"
    rem_contact = contact_dict.pop(id)
    return rem_contact

def sort_contact(contact_dict, /):
    sorts = sorted(contact_dict.items(), key = lambda item: (item[1][1], item[1][0]))
    return sorts

def find_contact(contact_dict, /, *, find):
    empty_contact = {}
    if isinstance(find, (int, str)) and find in contact_dict:
        empty_contact[find] = contact_dict[find]
    for k, v in contact_dict.items():
        first = v.get('first', '')
        last = v.get('last', '')
        if isinstance(find, str) and find in first or find in last:
            empty_contact[k] = v
    sorted(empty_contact.items(), key = lambda item: (item[1][1], item[1][0]))
    return empty_contact