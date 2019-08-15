import unittest
import solution

class Testsolution(unittest.TestCase):

    def test_encode_1(self):
        # msg num : 31 chars, key : 8
        testInput = 'Common sense is not so common.'
        expected = 'Cenoonommstmme oo snnio. s s c'
        self.assertEqual(solution.encrypt(8, testInput), expected)

if __name__ == "__main__":
    unittest.main()
