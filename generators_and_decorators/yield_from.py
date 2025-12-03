def order_one():
    yield "Red curry"
    yield "Green curry"

def order_two():
    yield "Pitta wrap"
    yield "Haloumi wrap"

def orders():
    yield from order_one()
    yield from order_two()

for _ in orders():
    print(_)