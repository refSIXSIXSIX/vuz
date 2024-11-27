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
    import unittest
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