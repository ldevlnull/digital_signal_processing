import math

def low_freq_filter(input_signal, output_signal, size_in):
    filter_len = 20  # Довжина фільтру
    Fd = 2000  # Частота дискретизації вхідних даних
    Fs = 20  # Частота лінії пропускания
    Fx = 50  # Частота лінії затухания

    H = []  # Імпульсна характеристика фільтру
    H_id = []  # Ідеальна імпульсна характеристика
    W = []  # Вагова функція

    # Розрахунок імпульсної характеристики фильтру
    Fc = (Fs + Fx) / (2 * Fd)

    for i in range(filter_len):
        if i == 0:
            H_id[i] = 2 * math.pi * Fc
        else:
            H_id[i] = math.sin(2 * math.pi * Fc * i) / (math.pi * i)
        # вагова функція Блекмана
        W[i] = 0.42 - 0.5 * math.cos((2 * math.pi * i) / (filter_len - 1)) + 0.08 * math.cos((4 * math.pi * i) / (filter_len - 1))
        H[i] = H_id[i] * W[i]

    # Нормалізації функції пропускання
    impulse_sum = 0
    for i in range(filter_len):
        impulse_sum += H[i]
    for i in range(filter_len):
        H[i] /= impulse_sum  # сума коефіцієнтів рівна 1

    # Фільтрація вхідних данних
    for i in range(size_in):
        output_signal[i] = 0
        for j in range(filter_len - 1):  # формула фільтру
            if (i - j) >= 0:
                output_signal[i] += H[j] * input_signal[i - j]
