from math import log, pi, cos, sin


def main():
    input_data = list(map(lambda x: complex(x, 0.0), [5.0, 1.0, 0.0, 2.0, 6.0, 4.0, 7.0, 8.0]))
    print('input: ', input_data)
    fft(input_data)
    print('output:')
    [print(num) for num in input_data]
    exit(0)


def fft(buffer):
    bits = int(log(len(buffer)) / log(2))

    for i in range(1, len(buffer)):
        swap_position = reverse(i, bits)
        t = buffer[i]
        buffer[i] = buffer[swap_position]
        buffer[swap_position] = t

    n = 2
    while n <= len(buffer):
        i = 0
        while i < len(buffer):
            for k in range(int(n/2)):
                ei = i + k
                oi = ei + int(n / 2)
                even, odd = buffer[ei], buffer[oi]
                term = (-2 * pi * k) / n
                exp = complex(cos(term), sin(term)) * odd
                buffer[ei], buffer[oi] = even + exp, even - exp
            i += n
        n <<= 1


def reverse(n, bits):
    reversed_n = n
    count = bits - 1

    n >>= 1
    while n > 0:
        reversed_n = (reversed_n << 1) | (n & 1)
        count -= 1
        n >>= 1

    return (reversed_n << count) & ((1 << bits) - 1)


if __name__ == '__main__':
    main()
