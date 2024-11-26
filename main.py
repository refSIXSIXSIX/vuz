import re
import unittest

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def main():
    email = input("Введите email: ")
    if is_valid_email(email):
        print("Email корректный.")
    else:
        print("Email некорректный.")

main()   
