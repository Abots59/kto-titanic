import unittest
from typing import List

MAX_NAME_LENGTH: int = 7


def count_long_names(first_names: List[str]) -> int:
    """
    Count the number of first names longer than MAX_NAME_LENGTH
    and display a message for each name.
    """
    long_name_count: int = 0

    for first_name in first_names:
        if is_name_long(first_name):
            print(f"{first_name} contient plus de {MAX_NAME_LENGTH} lettres")
            long_name_count += 1
        else:
            print(f"{first_name} contient {MAX_NAME_LENGTH} lettres ou moins")

    return long_name_count


def is_name_long(first_name: str) -> bool:
    """Return True if the name length exceeds MAX_NAME_LENGTH."""
    return len(first_name) > MAX_NAME_LENGTH

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = count_long_names(first_names=first_names)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()