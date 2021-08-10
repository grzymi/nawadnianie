def suma(*args):
    with open('ToStart.txt', 'w') as f:
        x = 0
        for i in args:
            x = x+i
        f.write(str(x))
