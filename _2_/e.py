import re
import string

from collections import Counter


class TextHandler:
    def __init__(self, text: str):
        if not isinstance(text, str) or not text:
            raise ValueError('\'text\' must be a non-empty string')
        self._text = text
        self._words = re.findall(r'\b\S+\b', self._text)

    def print_longest(self):
        print(max(self._words, key=len))

    def print_most_common(self):
        print(Counter(self._words).most_common(1)[0][0])

    def print_count_of_special_symbols(self):
        count = 0
        for char in self._text:
            if self._is_special_symbol(char):
                count += 1
        print(count)

    def print_palindromes(self):
        palindromes = {word for word in self._words if self._is_palindrome(word.lower())}
        print(', '.join(palindromes))

    def _is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def _is_special_symbol(self, char: str) -> bool:
        return char in string.punctuation


if __name__ == '__main__':
    text_handler = TextHandler('a aA. Aba, acba! aa?\naAB-ca\n bAb AAa aaa! abba, aaAaa.\n dd - ab')
    text_handler.print_longest()
    text_handler.print_most_common()
    text_handler.print_count_of_special_symbols()
    text_handler.print_palindromes()