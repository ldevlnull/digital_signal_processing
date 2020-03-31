input_data = [
    ([5, 4, 3], [1, 5, 6]),
    ([0, 7, 1, 4, 5, 6, 1, 2], [1, 0, 9, 2, 8, 7]),
    ([0, 9, 4, 5, 0, 7, 5], [4, 7, 3, 4, 9, 2, 1, 3, 7, 4])
]


def calculate_fm(xk, yk):
    # output`s list
    fm_len = (len(xk) + len(yk)) - 1
    fm = []

    # fills input lists with zeroes so they are the same length
    xk_init_size = len(xk)
    for i in range(len(yk) - 1):
        xk.append(0)
    for i in range(xk_init_size - 1):
        yk.append(0)

    yk.reverse()

    for m in range(fm_len):
        fm.append(0)
        for i in range(len(xk)):
            fm[m] += xk[i] * yk[i]
        xk.pop(-1)
        yk.pop(0)
    return fm


def main():
    for arr in input_data:
        xk = arr[0]
        yk = arr[1]
        print(calculate_fm(xk, yk))


if __name__ == '__main__':
    main()
