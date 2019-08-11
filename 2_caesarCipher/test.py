import unittest
import solution
import hack

class Testsolution(unittest.TestCase):

    def test_encode_1(self):
        testInput = 'This is my secret message.'
        expected = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
        self.assertEqual(solution.caesar_cipher(testInput, 13, 'encode'), expected)

    def test_decode_1(self):
        testInput = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
        expected = 'This is my secret message.'
        self.assertEqual(solution.encrypt(testInput, 13, 'decode'), expected)

    def test_hack_1(self):
        testInput = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
        expected = 'This is my secret message.'
        got = list(filter(lambda msg: msg == expected, hack.hack(testInput)))
        self.assertEqual(len(got), 1)


if __name__ == "__main__":
    unittest.main()
