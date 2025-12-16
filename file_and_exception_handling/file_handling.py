## Method 1
# file = open('menu.txt','w')

# try: 
#     file.write('This is Python code')
# finally:
#     file.close()


## Method 2
with open('menu.txt','w') as file:
    file.write('This is new way of writing a file')