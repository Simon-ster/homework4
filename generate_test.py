import unittest
import generate

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(generate.calculate("Bob","Jones"),"Bob Jones")
    def test2(self):
        self.assertEqual(generate.calculate("Bob",""),"Bob")
    def test3(self):
        self.assertEqual(generate.calculate(1,2),None)

if __name__ == "__main__":
    unittest.main()