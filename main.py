import re
import unittest

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def read_emails_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def main():
    filename = input("Введите имя файла с email-адресами: ")
    emails = read_emails_from_file(filename)
    
    if not emails:
        print("Файл пустой или отсутствует.")
        return
    
    for email in emails:
        if is_valid_email(email):
            print(f"{email} - корректный.")
        else:
            print(f"{email} - некорректный.")

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("lazzy@test.com"))
        self.assertTrue(is_valid_email("lazzy.2wice@example.vog.uk"))
        self.assertTrue(is_valid_email("123@ass.org"))

    def test_invalid_emails(self):
        self.assertFalse(is_valid_email("lazzy.com"))
        self.assertFalse(is_valid_email("ulazzy@.com"))
        self.assertFalse(is_valid_email("lazzy@other"))

def run_tests():
    print("Запуск тестов...")
    unittest.main()

if __name__ == "__main__":
    print("What you need?\n")
    print("1 - Main")
    print("2 - Test")
    choice = input()

    if choice == "1":
        main()
    elif choice == "2":
        run_tests()
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")
