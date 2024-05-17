class WorkWithFile:
    def __init__(self, a, b):
        self.file = open(a, b)

    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with WorkWithFile(r"additional_files\input.txt", 'r') as f:
    print(f.read())