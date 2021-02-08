import unittest
import cube

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.calculate(1.5),3.375)
    def test2(self):
        self.assertEqual(cube.calculate("Hello"),None)
    def test3(self):
        self.assertEqual(cube.calculate(-1),None)

if __name__ == "__main__":
    unittest.main()