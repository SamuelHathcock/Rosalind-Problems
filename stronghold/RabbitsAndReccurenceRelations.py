count = 0
a = 1
b = 1
c = 0

while count < 10:
    c = a+b
    a = b
    b = c
    print(c)
    
    count+=1