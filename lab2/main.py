input_data = [
    [0, 9, 2, 7, 4, 3], [6, 8, 6, 4], [5, 1, 0, 2, 6, 4, 7, 8], [0, 1, 2, 8, 7, 4, 0]
]


def scale(xk, alpha):
    return [x * alpha for x in xk]


def time_reverse(xk):
    return [-x for x in xk]


def shift(xk, N):
    return [x - N for x in xk]


def dilate(xk, alpha):
    if alpha.__class__ is not int:
        raise ArithmeticError
    res = []
    if alpha > 1:
        for i in range(len(xk)):
            if i % alpha == 0:
                res.append(xk[i])
    elif alpha < 1:
        res.append(xk[0])
        res.append(xk[1])

        for i in range(len(xk)-2):
            [res.insert(-1, x) for x in __linear_interpolation(res[-1], res[-2], alpha)]
            res.append(xk[i + 2])
    return res


def __linear_interpolation(a, b, alpha):
    alpha = -alpha+1
    res = [((a + b)/alpha)*i for i in range(1, alpha)]
    return res if a > b else reversed(res)


def sum_signals(xk, yk):
    return [x + y for (x, y) in zip(xk, yk)]


def multiply_signals(xk, yk):
    return [x * y for (x, y) in zip(xk, yk)]


def main():
    for signal in input_data:
        scale_alpha = 3
        offset = 2
        dilate_alpha = 2
        print('init: ', signal)
        print('scaled by {}: '.format(scale_alpha), scale(signal, scale_alpha))
        print('time reversed: ', time_reverse(signal))
        print('shifted by {}: '.format(offset), shift(signal, offset))
        print('dilated by {}'.format(dilate_alpha), dilate(signal, dilate_alpha))
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")

    for (signal1, signal2) in zip([input_data[0], input_data[2]], [input_data[1], input_data[3]]):
        print('sum of {} and {}: '.format(signal1, signal2), sum_signals(signal1, signal2))
        print('multiply {} and {}: '.format(signal1, signal2), multiply_signals(signal1, signal2))
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")


if __name__ == '__main__':
    main()
