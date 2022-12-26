# Студент
# тест свит
# Дек 26 2022

import unittest
from change_char import change_char


# test suite for change_char function using unittest
class TestChangeChar(unittest.TestCase):
    # test for change_char function
    def test_change_char(self):
        # test string
        string = "restart"
        # expected result
        result = "resta$t"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for empty string
    def test_empty_string(self):
        # test string
        string = ""
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for string with one character
    def test_one_char_string(self):
        # test string
        string = "a"
        # expected result
        result = "a"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for string with two characters
    def test_two_char_string(self):
        # test string
        string = "aa"
        # expected result
        result = "a$"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for string with two different characters
    def test_two_diff_char_string(self):
        # test string
        string = "ab"
        # expected result
        result = "ab"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for string with three characters
    def test_three_char_string(self):
        # test string
        string = "aaa"
        # expected result
        result = "a$$"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for integer put in place of string
    def test_int_string(self):
        # test string
        string = 123
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for float put in place of string
    def test_float_string(self):
        # test string
        string = 1.23
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for list put in place of string
    def test_list_string(self):
        # test string
        string = [1, 2, 3]
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for tuple put in place of string
    def test_tuple_string(self):
        # test string
        string = (1, 2, 3)
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for dictionary put in place of string
    def test_dict_string(self):
        # test string
        string = {1: 2, 3: 4}
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for set put in place of string
    def test_set_string(self):
        # test string
        string = {1, 2, 3}
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for boolean put in place of string
    def test_bool_string(self):
        # test string
        string = True
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for None put in place of string
    def test_none_string(self):
        # test string
        string = None
        # expected result
        result = ""
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for a really long sentence put for string
    def test_long_string(self):
        # test string
        string = "the quick brown fox jumps over the lazy dog"
        # expected result
        result = "the quick brown fox jumps over $he lazy dog"
        # test for equality
        self.assertEqual(change_char(string), result)
    # test for a really long sentence put for string with repeating first charater
    def test_long_string_repeat(self):
        # test string
        string = "the quick chocolate fox jumps over the lazy toad"
        # expected result
        result = "the quick chocola$e fox jumps over $he lazy $oad"
        # test for equality
        self.assertEqual(change_char(string), result)

# run tests
if __name__ == "__main__":
    unittest.main()