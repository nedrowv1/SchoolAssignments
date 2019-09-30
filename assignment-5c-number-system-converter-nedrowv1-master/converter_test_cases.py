import unittest
import BinaryConverter


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(BinaryConverter.convert_dec_to_bin(3.0), 11)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(12.0), 1100)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(25.0), 11001)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(50.0), 110010)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(10.0), 2)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(101.0), 5)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(11011.0), 27)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(11001101.0), 205)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(3.5), 11.1)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(12.25), 1100.01)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(25.75), 11001.11)
        self.assertEqual(BinaryConverter.convert_dec_to_bin(50.35), 110010.0101100110011001101)  # long line
        self.assertEqual(BinaryConverter.convert_bin_to_dec(10.1), 2.5)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(101.001), 5.125)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(11011.101), 27.625)
        self.assertEqual(BinaryConverter.convert_bin_to_dec(11001101.0111111), 205.4921875)  # long line


if __name__ == '__main__':
    unittest.main()
