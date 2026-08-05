number = 13

print(f"Decimal : {number}")
print(f"Binary  : {bin(number)}")

print()

letter = "A"

print(f"Letter  : {letter}")
print(f"ASCII   : {ord(letter)}")
print(f"Binary  : {bin(ord(letter))}")

print()

message = "Hi"

for c in message:
    print(f"{c} -> {ord(c)} -> {bin(ord(c))}")