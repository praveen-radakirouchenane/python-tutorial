def get_boxes() :
    yield "box 1"
    yield "box 2"
    yield "box 3"


box = get_boxes()
print(box) # this line will return only the reference of the function 
print(next(box)) # this will return only the first yield and pause the execution  
print(next(box)) # this will exactly resume from where it left and return the yield 
print(next(box))