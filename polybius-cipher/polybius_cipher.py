class PolybiusCipher:
    def __init__(self, checkerboard=None):
        if checkerboard == None:
            self.polybius_checkerboard = (
                ("a", "b", "c", "d", "e"),
                ("f", "g", "h", ("i", "j"), "k"),
                ("l", "m", "n", "o", "p"),
                ("q", "r", "s", "t", "u"),
                ("v", "w", "x", "y", "z"),
            )
        else:
            self.polybius_checkerboard = checkerboard

    def get_coordinates(self, row_index: int, column_index: int) -> str:
        return "".join((str(row_index + 1), str(column_index + 1), " "))

    def encode(self, text: str) -> str:
        text = text.lower()
        ciphertext = ""

        for character in text:
            for row_index, letters in enumerate(self.polybius_checkerboard):
                for column_index, letter in enumerate(letters):
                    if type(letter) == tuple:
                        if character == letter[0] or character == letter[1]:
                            ciphertext += self.get_coordinates(row_index, column_index)
                    else:
                        if character == letter:
                            ciphertext += self.get_coordinates(row_index, column_index)

        return ciphertext[:-1]

    def decode(self, ciphertext: str):
        text = ""

        for number in ciphertext.split(" "):
            if len(number) == 2:
                row_index = int(number[0]) - 1
                column_index = int(number[1]) - 1

                if row_index == 1 and column_index == 3:
                    text += "i/j"
                else:
                    text += "".join(self.polybius_checkerboard[row_index][column_index])

        return text
