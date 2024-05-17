with open(r"additional_files\numbers.txt", "r") as file:
    list_1 = list(map(int, file.read().split()))
    with open(r'additional_files\output.txt', 'a') as out_file:
        out_file.write(str(max(list_1) + min(list_1)))

