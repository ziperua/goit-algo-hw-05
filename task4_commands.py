def input_error(function):
    def inner(*args):
        try:
            return function(*args)
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter correct name"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed"
@input_error
def check_phone(args, contacts):
    name  = args[0]
    return contacts[name]
@input_error
def all_contacts(contacts):
    if not contacts:
        return "Contacts not found"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()