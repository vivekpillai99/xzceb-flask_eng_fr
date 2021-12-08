import unittest
from translator import frenchToEnglish, englishToFrench
class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
    def test2(self):
        self.assertNotEqual(frenchToEnglish("None"), "")
    def test3(self):
        self.assertEqual(frenchToEnglish("Bonjour, bienvenue en France"), \
            "Hello, welcome to France")
    def test4(self):
        self.assertEqual(frenchToEnglish("Mon nom est Vivek"), "My name is Vivek")

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
    def test2(self):
        self.assertNotEqual(englishToFrench("None"), "")
    def test3(self):
        self.assertEqual(englishToFrench("Hello, welcome to America"), \
            "Bonjour, bienvenue à l'Amérique")
    def test4(self):
        self.assertEqual(englishToFrench("My name is Vivek"), "Mon nom est Vivek")
unittest.main()