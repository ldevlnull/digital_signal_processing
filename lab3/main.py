N_POINTS = 0
N_TYPE = 0
is_auto_correlation_selected = False
is_normalized_correlation_selected = False
OUTPUT_PATH = 'output.txt'


def read_data():
    data1, data2 = None, None
    global N_POINTS
    if is_auto_correlation_selected:
        print("Enter file path")
        file = open(input())
        data1 = extract_lined_numbers(file)
        N_POINTS = len(data1)
        file.close()
    else:
        print("Enter first data file path")
        file1 = open(input())
        print("Enter second data file path")
        file2 = open(input())
        data1, data2 = extract_lined_numbers(file1), extract_lined_numbers(file2)
        print(data1)
        print(data2)
        N_POINTS = len(data2)
        file1.close()
        file2.close()
    print('N ', N_POINTS)
    return data1, data2


def extract_lined_numbers(path):
    return list(map(lambda x: int(x), path.read().split(',')))


def auto_correlation(data1):
    acf1 = [0.0] * N_POINTS
    for i in range(N_POINTS):
        points_sum = 0
        j = N_POINTS - i
        for k in range(j):
            points_sum += data1[k] * data1[k + i]

        acf1[i] = points_sum / N_POINTS
    if is_normalized_correlation_selected:
        sf = acf1[0]
        for i in range(N_POINTS):
            acf1[i] = acf1[i] / sf
    return acf1


def cross_correlation(data1, data2):
    ccf = [0.0] * N_POINTS
    npt1 = N_POINTS - 1
    npt2 = 2 * N_POINTS
    for i in range(N_POINTS):
        i2 = npt1 + i
        i3 = npt1 - i
        sum1, sum2 = 0, 0
        j = N_POINTS - i
        for k in range(j):
            sum1 += data1[k] * data2[k + i]
            sum2 += data2[k] * data1[k + i]
        ccf[i2], ccf[i3] = sum1 / N_POINTS, sum2 / N_POINTS

    if is_normalized_correlation_selected:
        sum1, sum2 = 0, 0
        for i in range(N_POINTS):
            sum1 += data1[i] * data1[i]
            sum2 += data2[i] * data2[i]
        rxx, ryy = sum1 / N_POINTS, sum2 / N_POINTS
        sf = (rxx * ryy) ** 0.5
        for i in range(npt2):
            ccf[i] = ccf[i] / sf
    return ccf


def save_data(res):
    output_file = open(OUTPUT_PATH, 'w+')
    print('result ', res)
    output_file.write(str(res))
    output_file.close()


def main():
    global is_auto_correlation_selected, is_normalized_correlation_selected
    print("Select type of correlation\n1. Auto-correlation\n2. Cross-correlation")
    is_auto_correlation_selected = int(input()) == 1
    print("Select normalized or non-normalized correlation\n1. Normalized correlation\n2. Non-normalized correlation")
    is_normalized_correlation_selected = int(input()) == 1
    data1, data2 = read_data()
    save_data(auto_correlation(data1) if is_auto_correlation_selected else cross_correlation(data1, data2))
    exit(0)


if __name__ == '__main__':
    main()
