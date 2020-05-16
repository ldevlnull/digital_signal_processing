from math import pi, cos, sin


def main():
    sequence = [0, 9, 2, 7, 4, 3]
    print('sequence: ', sequence)
    r, i = discrete_fourier_transform(sequence)
    print('real: ', r, ' \nimagine: ', i)
    exit(0)


def discrete_fourier_transform(sequence):
    n = len(sequence)
    if n == 0:
        raise Exception('Given data is empty. Abort!')
    real_nums, imagine_nums = [0.0] * n, [0.0] * n
    for k in range(n):
        real_num, imagine_num = 0.0, 0.0
        for t in range(n):
            angle = 2 * pi * t * k / n
            real_num += sequence[t] * cos(angle)
            imagine_num += sequence[t] * sin(angle)
        real_nums[k], imagine_nums[k] = real_num, imagine_num
    return real_nums, imagine_nums


if __name__ == '__main__':
    main()
