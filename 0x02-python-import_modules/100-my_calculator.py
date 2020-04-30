#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

argv = sys.argv[1:]
argc = len(argv)


if __name__ == "__main__":
    if argc != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[0])
    b = int(argv[2])

    op = argv[1]

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    else:
        print('unknown operator. available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(a, op, b, res))
