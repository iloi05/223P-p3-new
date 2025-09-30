# Name: Ivy Loi
# Date: 9/21/25
# Purpose of file: Create contact list functions that will be used in main file
           
def is_int(id):
    try:
        int(id)
        return True
    except ValueError:
        return False

def is_string_first(first_name):
    try:
        int(first_name)
        return True
    except ValueError:
        return False
    
def is_string_last(last_name):
    try:
        int(last_name)
        return True
    except ValueError:
        return False

def add_contact(contact_dict, /, *, id, first_name, last_name):
    """Adds contact to dictionary"""
    if id in contact_dict:
        print("This contact already exists in the system, please enter a new contact.")
        return "error"
    contact_dict[id] = {"first" : first_name, "last" : last_name}
    return contact_dict[id]

def modify_contact(contact_dict, *, id, first_name, last_name):
    """Gets contact and modifies it"""
    if id not in contact_dict:
        print("Please input a valid phone number that is in the dictionary.")
        return "error"
    else:
        contact_dict[id] = {"first" : first_name, "last" : last_name}
        return contact_dict[id]

def delete_contact(contact_dict, *, id):
    """Deletes contact from dictionary"""
    if id not in contact_dict:
        return "error"
    rem_contact = contact_dict.pop(id)
    print("Contact deleted...")
    return rem_contact

def sort_contact(contact_dict, /):
    """Sorts contacts by last name"""
    return {k: v for k, v in sorted(contact_dict.items(), key = lambda item: item[1].get("last", ""))}
    
def print_contact(contact_dict):
    """Prints contact list"""
    if not contact_dict:
        print("The list is empty, put a name in first")
    else:
        print("================== CONTACT LIST ==================")
        print("Last Name           First Name           Phone    ")
        print("==================  ===================  =========")
        for id, info in sort_contact(contact_dict).items():
            first = info.get("first", "id")
            last = info.get("last", "id")
            print(f"{last:<20}{first:<21}{id:<9}")

def find_contact(contact_dict, /, *, find):
    """Finds contacts by last name"""
    empty_contact = {}
    if not find.isnumeric() and find not in contact_dict:
        print("No contacts found, returning to main menu")
        return "error"
    if find.isnumeric() and find in contact_dict:
        empty_contact[find] = contact_dict[find]
    elif not find.isnumeric() and find in contact_dict:
        for id, info in contact_dict.items():
            last = info.get("last", "").lower()
            if find.lower() == last:
                empty_contact[id] = contact_dict[id]
    
    print("================== FOUND CONTACT(S) ==================")
    print("Last Name             First Name           Phone    ")
    print("==================    ===================  ===========")
    for id, info in sort_contact(empty_contact).items():
        first = info.get("first", "")
        last = info.get("last", "")
        print(f"{last:<22}{first:<21}{id:<16}")
    return empty_contact