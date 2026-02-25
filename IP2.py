import re
if re.search(r"^\w{4}\d{4}$", input("Student ID: ")):
    print("valid")
else:
    print("invalid")