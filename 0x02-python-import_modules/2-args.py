#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv)
    args_list = argv

    if num_args == 1:
        print(f"{num_args - 1} arguments.")
    elif num_args == 2:
        print(f"{num_args - 1} argument:")
    else:
        print(f"{num_args - 1} arguments:")

    for i in range(1, num_args):
        print(f"{i}: {args_list[i]}")
