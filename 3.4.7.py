with open(r'additional_files\input.txt', 'r') as f:
    list_1 = [line.strip() for line in f]
    list_1 = reversed(list_1)
    with open(r'additional_files\output.txt', 'a') as f_end:
        for line in list_1:
            line = line + '\n'
            f_end.write(line)


