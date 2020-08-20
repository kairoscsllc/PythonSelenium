import unittest

class TestCaseClass(unittest.TestCase):

    def test_methoda(self):
        print("this is the setup method")

if __name__ == '__main__':
    unittest.main(verbosity=2)