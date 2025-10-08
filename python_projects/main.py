from typing import Literal, List
from colorama import Fore


class Encryptor:
    def __init__(self, text):
        self.text: str = text
        self.satzzeichen = ["!", " "]
        self.alphabet: List[Literal] = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"]

    def encrypt_string(self) -> str:
        corrected_string = ""

        for string_part in self.text:
            if string_part in self.satzzeichen:
                corrected_string += string_part
                continue

            elif string_part != "z":
                for idx, stuff in enumerate(self.alphabet):
                    if stuff == string_part:
                        print(f"Enumerating string: {stuff} to {self.alphabet[idx +1]}")
                        corrected_string += self.alphabet[idx + 1]

            else:
                corrected_string += "a"

        return corrected_string


corrected_string = Encryptor("Veni Vidi Vici".lower()).encrypt_string()
print(f"{Fore.LIGHTCYAN_EX}{corrected_string}")





