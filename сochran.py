from scipy.stats import f

def calculate_CUL(n, N, alpha=0.05):
    # Вычисляем критическое значение коэффициента Фишера
    F_critical = f.ppf(1 - alpha/N, n-1, (N-1)*(n-1))

    # Вычисляем верхний предел критического значения
    CUL = 1 / (1 + (N-1) / F_critical)

    return CUL

# Ввод параметров

N = int(input("Введите количество строк опыта: "))   # количество серий данных
n = int(input("Введите повторность опыта: "))  # количество точек данных в каждой серии данных


alpha_input = input("Значение уровня значимости (alpha) по умолчанию равно 0.05: ")
alpha = float(alpha_input) if alpha_input else 0.05

CUL = calculate_CUL(n, N, alpha)
print("Критическое знаение критерия Кохрена: ", round(CUL, 4))
