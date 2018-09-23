import unittest

from lib.command_fetcher import getCommandMode, FileMode, InteractiveMode

# python -m test.getCommandMode

class TestingGetCommandMode(unittest.TestCase):
    """
    Testing Parking Lot.
    """

    def test_get_mode(self):
        a,b,c,d = 0,1,2,3
        try:
            getCommandMode(a)
        except Exception as e:
            self.assertEqual(e.message, "Unknown Mode")
        try:
            getCommandMode(d)
        except Exception as e:
            self.assertEqual(e.message, "Unknown Mode")
        mode = getCommandMode(b)
        self.assertEqual(mode.__class__, InteractiveMode)
        mode = getCommandMode(c)
        self.assertEqual(mode.__class__, FileMode)

if __name__ == '__main__':
    unittest.main()
