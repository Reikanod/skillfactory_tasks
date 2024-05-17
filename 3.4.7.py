with open(r'additional_files\input.txt', 'r') as f:
    with open(r'additional_files\output.txt', 'w') as f_end:
        for line in reversed(f.readlines()):
            f_end.write(line)

