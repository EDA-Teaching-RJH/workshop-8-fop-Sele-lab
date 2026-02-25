import re
def is_valid_email(email):
    if re.search(r"^\w+@\w.+\.(ac.uk | gov.uk | nhs.net)$", email):
        return True
    return False


def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()
