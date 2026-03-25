class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        return f"{self.name} | {self.phone} | {self.email}"


class FavouriteContact(Contact):
    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        self.favourite = True


# =========================
# regex_utils.py
# =========================

import re


def valid_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None


def valid_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None


def search_contacts(contacts, keyword):
    return [c for c in contacts if re.search(keyword, c.name, re.IGNORECASE)]


# =========================
# file_handler.py
# =========================

def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for c in contacts:
            f.write(f"{c.name},{c.phone},{c.email}\n")


def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append(Contact(name, phone, email))
    except FileNotFoundError:
        pass
    return contacts


# =========================
# main.py
# =========================

def menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Save")
    print("5. Load")
    print("6. Exit")


def main():
    contacts = []

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone (10 digits): ")
            email = input("Email: ")

            if not valid_phone(phone):
                print("Invalid phone number!")
                continue

            if not valid_email(email):
                print("Invalid email!")
                continue

            fav = input("Favourite? (y/n): ").lower()

            if fav == "y":
                contact = FavouriteContact(name, phone, email)
            else:
                contact = Contact(name, phone, email)

            contacts.append(contact)
            print("Contact added!")

        elif choice == "2":
            for c in contacts:
                print(c.display())

        elif choice == "3":
            keyword = input("Search name: ")
            results = search_contacts(contacts, keyword)
            for c in results:
                print(c.display())

        elif choice == "4":
            save_contacts(contacts)
            print("Saved!")

        elif choice == "5":
            contacts = load_contacts()
            print("Loaded!")

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()


# =========================
# test_contacts.py
# =========================

import unittest


class TestContacts(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(valid_email("test@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(valid_email("bademail"))

    def test_valid_phone(self):
        self.assertTrue(valid_phone("1234567890"))

    def test_invalid_phone(self):
        self.assertFalse(valid_phone("123"))


if __name__ == "__main__":
    unittest.main()
