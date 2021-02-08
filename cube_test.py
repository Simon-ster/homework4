import unittest
import cube

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.calculate(1.5),3.375)
    def test2(self):
        with self.assertRaises(TypeError):
            cube.calculate("Hello")
    def test3(self):
        self.assertEqual(cube.calculate(-1),None)

if __name__ == "__main__":
    unittest.main()