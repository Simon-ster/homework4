import unittest
import avg

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(avg.calculate([1,2,3]),2)
    def test2(self):
        self.assertEqual(avg.calculate(['a']),None)
    def test3(self):
        self.assertEqual(avg.calculate([]),None)

if __name__ == "__main__":
    unittest.main()