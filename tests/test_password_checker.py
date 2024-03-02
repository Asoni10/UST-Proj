import unittest
from password_checker import check_password_validity

class TestPasswordChecker(unittest.TestCase):
    def test_valid_password(self):
        password = "aSqwr1234@1"
        self.assertEqual(check_password_validity(password), password)

    def test_invalid_password(self):
        password = "123456"
        self.assertEqual(check_password_validity(password), password)

if __name__ == "__main__":
    unittest.main()
