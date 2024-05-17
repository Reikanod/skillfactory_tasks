text = """a long time ago
one guy saw an owl.
An owl was so intellegent
so the guy felt himself too stupid around it"""
file = open(r"additional_files\input.txt", "w")
file.write(text)
file = open(r"additional_files\input.txt", "r")
out_file = open(r"additional_files\output.txt", "w")
out_file.write(file.read())

