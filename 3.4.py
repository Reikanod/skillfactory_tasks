file = open("file.txt", 'a')

seq = ["1 строка\n", "2 string\n", "3 string\n"]

file.writelines(seq)

file.close()