N_POINTS = 0
acf1 = []
N_TYPE = 0
ccf = []
is_auto_correlation_selected = False
is_normalized_correlation_selected = False


def read_data():
    data1, data2 = None, None
    global N_POINTS
    if is_auto_correlation_selected:
        print("Enter file path \n");
        file = open(input())
        data1 = file.read()
        N_POINTS = len(data1)
        file.close()
    else:
        print("Enter first data file path \n")
        file1 = open(input())
        print("Enter second data file path \n")
        file2 = open(input())
        data1, data2 = file1.read(), file2.read()
        file1.close()
        file2.close()
    return data1, data2


def acf(data1):
    for i in range(N_POINTS):
        points_sum = 0
        j = N_POINTS - i
        for k in range(j):
            points_sum += data1[k] * data1[k + i]

        acf1[i] = points_sum / N_POINTS
    if N_TYPE == 1:
        sf = acf1[0]
        for i in range(N_POINTS):
            acf1[i] = acf1[i] / sf


def xcf(data1, data2):
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

    if N_TYPE == 1:
        sum1, sum2 = 0, 0
        for i in range(N_POINTS):
            sum1 += data1[i] * data1[i]
            sum2 += data2[i] * data2[i]
        rxx, ryy = sum1 / N_POINTS, sum2 / N_POINTS
        sf = (rxx * ryy) ** 0.5
        for i in range(npt2):
            ccf[i] = ccf[i] / sf


def main():
    print("Select type of correlation \n")
    print("1. Auto-correlation \n")
    print("2. Cross-correlation \n")
    main.is_auto_correlation_selected = input() == 1
    print("Select normalized or non-normalized correlation \n")
    print("1. Normalized correlation \n")
    print("2. Non-normalized correlation \n")
    main.is_normalized_correlation_selected = input() == 1
    data1, data2 = read_data()

    if is_auto_correlation_selected:
        acf(data1)
    else:
        xcf(data1, data2)
    return


if __name__ == '__main__':
    main()
