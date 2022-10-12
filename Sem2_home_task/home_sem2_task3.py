try:
    n = int(input("Введите количество измерений: "))

    coord_point_one = [];
    coord_point_two = [];
    for i in range(n):
        coord_point_one.append(int(input(f"Введите {i + 1}ю коордиту первой точки: ")))
        coord_point_two.append(int(input(f"Введите {i + 1}ю коордиту второй точки: ")))
    dis = 0
    for i in range(n):
        dis = dis + ((coord_point_two[i] - coord_point_one[i]) ** 2)


    print(f"Расстояние между точками равно {dis ** 0.5}")
except:
    print("Ошибка ввода")