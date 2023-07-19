import unittest
from src.utils import contains_phone_number, correct_length_phone_number, count_spaces_inside_string, contains_only_letters

class TestFunctions(unittest.TestCase):
    def test_contains_phone_number(self):
        self.assertTrue(contains_phone_number("+1234567890"))
        self.assertTrue(contains_phone_number("9876543210"))
        self.assertFalse(contains_phone_number("1234+5"))
        self.assertFalse(contains_phone_number("abc1234567"))

    def test_correct_length_phone_number(self):
        self.assertTrue(correct_length_phone_number("+12345678901"))
        self.assertFalse(correct_length_phone_number("12345"))
        self.assertFalse(correct_length_phone_number(""))

    def test_count_spaces_inside_string(self):
        self.assertEqual(count_spaces_inside_string("Hello World"), 1) 
        self.assertEqual(count_spaces_inside_string("NoSpacesHere"), 0) 
        self.assertEqual(count_spaces_inside_string("  Spaces  "), 0)

    def test_contains_only_letters(self):
        self.assertTrue(contains_only_letters("Hello"))
        self.assertTrue(contains_only_letters("Hello World"))   
        self.assertFalse(contains_only_letters("Hello123"))     
        self.assertFalse(contains_only_letters("12345"))   