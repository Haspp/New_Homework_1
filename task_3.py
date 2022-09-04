
def input_plane(x):
    a = [0] * x
    i: int
    for i in range(x):
        istina = False
        while not istina:
            try:
                number = float(input(f"Введите {i + 1} координату: "))
                a[i] = number
                istina = True
                if a[i] == 0:
                    istina = False
                    print("Координата не должно быть равна 0 ")
            except ValueError:
                print("Введите число")
    return a


def check_planes(xy):
    coord = 4
    if xy[0] > 0 and xy[1] > 0:
        coord = 1
    elif xy[0] < 0 < xy[1]:
        coord = 2
    elif xy[0] < 0 and xy[1] < 0:
        coord = 3
    print(f"Точка находится в {coord} четверти плоскости")


plane = input_plane(2)
check_planes(plane)
