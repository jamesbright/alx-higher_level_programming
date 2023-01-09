#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    valid_operators = ["+", "-", "*", "/"]

    if argv_count != 3:
        print("Usage [{:d}]: ./100-my_calculator.py <a> <operator> <b>".format(argv_count))
        exit(1)

    operator = sys.argv[2]
    a, b = int(sys.argv[1]), int(sys.argv[3])

    if not valid_operators.count(operator):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator ==  "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
