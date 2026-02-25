import re
if re.search(r"^07\d{9}$", input("Enter a phone number: ")):
    print("valid")
else:
    print("invalid")
    