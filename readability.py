from cs50 import get_string
import string

text = get_string("Enter text: ")

letters = 0
words = 1
phrases = 0

for c in text:
    if c == "." or c == "!" or c == "?":
        phrases += 1
    if c in string.ascii_letters:
        letters += 1
    if c in string.whitespace:
        words += 1

L = (letters * 100) / words
S = (phrases * 100) / words

index = round((0.0588 * L) - (0.296 * S) - 15.8)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade", index)

