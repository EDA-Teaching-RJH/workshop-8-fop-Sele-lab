import re
import json

class AssignmentExample:
    def __init__ (self,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        self.email = email

    def __str__(self):
        return f"AssignmentExample(email={self.email})"
    


        
def main():
    email = get_email_input()
    print(f"AssignmentExample created with email: {email}")

def get_email_input():
    email = input("Enter an email address: ")
    return email
    


if __name__ == "__main__":
    main()