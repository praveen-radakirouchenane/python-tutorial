orders = ["lemon soda", "ginger"]

try:
    print(orders[3])
except IndexError:
    print("Index out of bound exception")

print("Good bye!")
