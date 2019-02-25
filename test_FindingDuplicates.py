import unittest


class MyTestCase(unittest.TestCase):


    def test_number_of_dir(self):
        self.assert_()



    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
