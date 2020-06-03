from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n < 9 and n > 0:
        break

i = 1
j = n - 1

while i <= n: 
    print(" " * j, "#" * i, sep="")
    i += 1
    j -= 1
