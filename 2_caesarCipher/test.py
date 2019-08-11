import unittest
import solution

class Testsolution(unittest.TestCase):

    def test_case_1(self):
        testInput = 'This is my secret message.'
        expected = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
        self.assertEqual(solution.caesar_cipher(testInput, 13, 'encode'), expected)

    def test_case_2(self):
        testInput = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
        expected = 'This is my secret message.'
        self.assertEqual(solution.encrypt(testInput, 13, 'decode'), expected)


if __name__ == "__main__":
    unittest.main()
