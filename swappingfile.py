def swapFileData():
    file1 = input("Input the name of file 1: ")
    file2 = input("Input the name of file 2: ")
    file1 = file1 + '.txt'
    file2 = file2 + '.txt'
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)

swapFileData()