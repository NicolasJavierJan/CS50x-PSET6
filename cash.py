from cs50 import get_float

while True:
    n = get_float("Change owed: ") * 100
    if n > 0:
        break

quarter = 0
dime = 0
nickel = 0
penny = 0

while n > 0:
    while n >= 25:
        quarter += 1
        n -= 25
    while n >= 10:
        dime += 1
        n -= 10
    while n >= 5:
        nickel += 1
        n -= 5
    while n >= 1:
        penny += 1
        n -= 1

print(quarter + dime + nickel + penny)