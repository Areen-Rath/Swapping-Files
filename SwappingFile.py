with open("Test1.txt", 'r') as a:
    data_a = a.read()

with open("Test2.txt", 'r') as b:
    data_b = b.read()

with open("Test1.txt", 'w') as a:
    a.write(data_b)

with open("Test2.txt", 'w') as b:
    b.write(data_a)