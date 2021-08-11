import datetime

def suma(*args):
    with open('ToStart.txt', 'w') as f:
        for i in args:
            f.write(f'{i}/n')
    
