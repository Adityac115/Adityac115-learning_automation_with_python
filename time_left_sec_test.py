from time_left_sec import to_seconds
import unittest

class Testtime(unittest.TestCase):
    def test_basic(self):
        input=1,2,3 
        expected=3723
        self.assertEqual(to_seconds(*input),expected)
 

unittest.main()