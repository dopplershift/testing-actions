import sys

if __name__ == '__main__':
    import os
    for i in range(10):
        print(f'{i}...hola')

    with open('test_data.txt', 'rt') as infile:
        for line in infile:
            print(line)