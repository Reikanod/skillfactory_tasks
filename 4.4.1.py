def p(n):
    if not n:
        return
    else:
        p(n-1)
        print(n)


p(10)