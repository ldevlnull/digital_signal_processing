# from cmath import polar
from math import copysign

SIZE = 100
input_data = [5.0, 1.0, 0.0, 2.0, 6.0, 4.0, 7.0, 8.0]
points_amount = 10


def main():
    a, b, nest, dest, h = [0.0] * SIZE, [0.0] * SIZE, [0.0] * SIZE, [0.0] * SIZE, [0.0] * SIZE
    nk = 1
    m = 2 * nk
    j = 0
    for i in range(nk):
        for k in range(3):
            dest[j + k] = input_data[j + k]
            nest[j + k] = input_data[j + k + 3]
        j += 3
    polar(dest, b, nk)
    polar(nest, a, nk)
    process_z_transform(a, b, h, m)
    print("Result:")
    [print(num) for num in h if num != 0]


def polar(p, ab, sect):
    if sect < 2:
        for i in range(3):
            ab[ab.index(0)] = p[i]


def process_z_transform(a, b, h, m):
    res = [0.0] * 3
    res[1] = h[0] = a[0] / b[0]
    for n in range(1, points_amount):
        k = n
        if n > m:
            k = m
        for i in range(1, k + 1):
            res[0] += h[n - 1] * b[i]
        h[n] = (a[n] - res[0]) / b[0]
        t = copysign(1, h[n]) * h[n]
        res[1] += t
        res[2] += t * t


if __name__ == '__main__':
    main()
