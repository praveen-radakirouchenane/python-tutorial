class OutOfRange(Exception):
    pass


def your_order(item):
    if item not in ['milk','sugar','protein']:
        raise OutOfRange('Your item in not available in our store!')
    print('Your ordered item is:',item)
    

#your_order('milk')
your_order('chicken')