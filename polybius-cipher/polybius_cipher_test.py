import unittest

from polybius_cipher import PolybiusCipher


class PolybiusCipherTest(unittest.TestCase):
    def test_encode_with_basic_checkerboard(self):
        polybius_cipher = PolybiusCipher()
        self.assertEqual(
            polybius_cipher.encode("Scisle tajne"), "43 13 24 43 31 15 44 11 24 33 15"
        )

    def test_decode_with_basic_checkerboard(self):
        polybius_cipher = PolybiusCipher()
        self.assertEqual(
            polybius_cipher.decode("43 13 24 43 31 15 44 11 24 33 15"),
            "sci/jsletai/jne",
        )

    def test_encode_with_polish_checkerboard(self):
        polybius_cipher = PolybiusCipher(
            (
                ("a", "ą", "b", "c", "ć"),
                ("d", "e", "ę", "f", "g"),
                ("h", "i", "j", "k", "l"),
                ("ł", "m", "n", "ń", "o"),
                ("ó", "p", "q", "r", "s"),
                ("ś", "t", "u", "v", "w"),
                ("x", "y", "z", "ź", "ż"),
            )
        )
        self.assertEqual(
            polybius_cipher.encode("Ściśle tajne"), "61 14 32 61 35 22 62 11 33 43 22"
        )

    def test_decode_with_polish_checkerboard(self):
        polybius_cipher = PolybiusCipher(
            (
                ("a", "ą", "b", "c", "ć"),
                ("d", "e", "ę", "f", "g"),
                ("h", "i", "j", "k", "l"),
                ("ł", "m", "n", "ń", "o"),
                ("ó", "p", "q", "r", "s"),
                ("ś", "t", "u", "v", "w"),
                ("x", "y", "z", "ź", "ż"),
            )
        )
        self.assertEqual(
            polybius_cipher.decode("61 14 32 61 35 22 62 11 33 43 22"), "ściśletajne"
        )


if __name__ == "__main__":
    unittest.main()
