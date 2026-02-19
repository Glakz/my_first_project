import math
p = math.pi # 3.141592653589793 пи для подсчёта площади круга 

print("Калькулятор запущен \nУкажите какой калькулятор вам необходим: ")
print("1 - Просто калькулятор", 
      "2 - Конвертер валют", 
      "3 - Калькулятор площадей фигур", 
      "4 - Калькулятор объемов фигур")
type_calculate = int(input("Укажите номер калькулятора: "))
if type_calculate == 1:
    print("Просто калькулятор")
    first_variable = float(input("Введите первое число: "))
    arithmetic_operator = input("Введите один из арифметических операторов: '+' '-' '/' '*' ")
    second_variable = float(input("Введите второе число: "))
    if arithmetic_operator == "+" :
       result =  first_variable + second_variable
    elif arithmetic_operator == "-" :
        result =  first_variable - second_variable 
    elif arithmetic_operator == "*" :
        result =  first_variable * second_variable
    elif arithmetic_operator == "/" :
        if second_variable != 0:
            result =  first_variable / second_variable
        else:
            result = "На 0 делить нельзя"
    else:
        print("Введено не коректное значение!!!")
    print(result)    
elif type_calculate == 2:
    print("Конвертер валют")
    print("Конвертер валют по соотношению к USD: 'BYN','RUB','CNY'")
    type_money = (input("укажите какую валюты вы желаете конвертировать: ")).upper()
    USD = int(input("Сколько USD вы хотите конвертировать в другую валюту: "))
    BYN = 2.8684 # Бел. рубли по соотношению к доллару
    RUB = 76.7568 # Рус. рубли по соотношению к доллару
    CNY = 6.9314 # Юань по соотношению к доллару
    if type_money == "BYN":
        print(USD * BYN, + "рублей")
    elif type_money == "RUB":
        print(USD * RUB, "рублей")
    elif type_money == "CNY":
        print(USD * CNY, "юаней")
    else:
        print("Указаны не верные данные")
elif type_calculate == 3:
    print("Калькулятор площадей фигур")
    geometric_shape = (input("Укажите какой фигуры площадь необходимо высчитать: 'квадрат','прямоугольник','треугольник','круг': ")).lower()
    if geometric_shape == 'квадрат':
        print(f"высчитываем площадь {geometric_shape}а")
        side_one = float(input("Укажите длину первой стороны в см: "))
        side_two = float(input("Укажите длину второй стороны в см: "))
        print(f"площадь {geometric_shape}а", side_one * side_two,"см")
    if geometric_shape == 'прямоугольник':
        print(f"высчитываем площадь {geometric_shape}а")
        side_one = float(input("Укажите длину первой стороны в см: "))
        side_two = float(input("Укажите длину второй стороны в см: "))
        print(f"площадь {geometric_shape}а", side_one * side_two,"см")
    elif  geometric_shape == 'треугольник':
        print(f"высчитываем площадь {geometric_shape}а")
        base = float(input("Укажите длину основания: "))
        height = float(input("Укажите длину высоты: "))
        print(f"площадь {geometric_shape}а", (base * height) / 2,"см")
    elif geometric_shape == 'круг':
        print(f"высчитываем площадь {geometric_shape}а")
        radius = float(input("Укажите радиус круга: "))
        result = round(p * radius**2, 2)
        print(f"площадь {geometric_shape}а {result}")
    else:
        print("Указано не корректное  название фигуры")
elif type_calculate == 4:
    print("Калькулятор объемов фигур")
    geometric_shape = (input("Укажите какой фигуры объем необходимо высчитать: 'куб','цилиндр','сфера','конус': ")).lower()
    if geometric_shape == 'куб':
        print(f"высчитываем объём {geometric_shape}а")
        side_one = float(input("Укажите длинну первой стороны в см: "))
        side_two = float(input("Укажите длинну второй стороны в см: "))
        height = float(input("Укажите длинну высоты: "))
        print(f"объём {geometric_shape}а", side_one * side_two * height,"см³")
    elif geometric_shape == 'цилиндр':
        print(f"высчитываем объём {geometric_shape}а")
        radius = float(input("Укажите радиус дна: "))
        base_radius = p * radius**2
        height = float(input("Укажите длину высоты: "))
        cylinder_volume = round(base_radius * height, 2)
        print(f"объём {geometric_shape}а {cylinder_volume}см³")
    elif  geometric_shape == 'сфера':
        print(f"высчитываем объём {geometric_shape}ы")
        radius = float(input("Укажите радиус сферы: "))
        sphere_volume =  (4/3) * p * radius**3
        print(f"объём {geometric_shape}ы {sphere_volume}см³")
    elif geometric_shape == 'конус':
        print(f"высчитываем объём {geometric_shape}а")
        radius = float(input("Укажите радиус дна: "))
        base_radius = p * radius**2
        height = float(input("Укажите длину высоты: "))
        cylinder_volume = round((1/3) * base_radius * height, 2)
        print(f"объём {geometric_shape}а {cylinder_volume}см³")
    else:
        print("Указано не корректное название фигуры")
else:
    print("Введено не корректное значение!!!")
