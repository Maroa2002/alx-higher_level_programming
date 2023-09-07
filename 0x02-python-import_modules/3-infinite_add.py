#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv)
    result = 0
    for i in range(1, num_args):
        result += int(argv[i])

    print(result)
