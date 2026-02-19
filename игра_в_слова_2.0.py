import random
vowels = "аеёиоуыэюя"
eng_char = "abcdefghijklmnopqrstuvwxyz"
while True:
    print("---------Игра в слова ----------")
    print("       Правила игры:\nВводим слова на русском языке\n"
          "Каждый раз после введения слова случайным образом определяется кто пишет слово\n"
          "Выигрывает тот кто набрал быстрее очки, их количество вы сможете указать ниже!!!\n"
          "Для выхода из игры в момент ввода слова введите 'q'\n"
          "____________________________________________")
    quit_game = input("подтвердите начало игры введя 1, при вводе любого другого символа игра закроется: ")
    if quit_game != "1":
        break
    red_total = 0  # общий счёт красного игрока
    blue_total = 0  # общий счёт для синего игрока
    print("__________________________________________________")
    point_for_win = int(input("   Укажите до число до скольки будем играть :    "))
    print("Определим кто пишет слово и приступим к игре")
    while red_total < point_for_win and blue_total < point_for_win:
        red_word_points = 0 # Очки за текущее слово
        blue_word_points = 0 # Очки за текущее слово
        index = 0 # индекс для перебора символов в слове
        print("Определяем кто пишет слово: ")
        red_random = random.randint(1, 10)
        blue_random = random.randint(1, 10)
        if red_random > blue_random: 
            # после проверки какой из гроков будет ходить, перебираем символы и ведём подсчёт очков
            print(f"У красного выпало число {red_random}\n У синего выпало число {blue_random}")
            user_input = input("Слово за красным: ").lower()
            if user_input == "q":
                break
            while index < len(user_input):
                char = user_input[index]
                index += 1
                if char in eng_char:
                    print("Вы ввели слово на английском, переключите раскладку на русский")
                    break
                if char in vowels:
                    red_word_points += 1
            print(f"Очки за слово: {red_word_points}")
            red_total += red_word_points
            print(f"общий счёт:\n   Красный {red_total}\n   Синий {blue_total}")
        elif blue_random > red_random:
            print(f"У синего выпало число {blue_random}\n У красного выпало число {red_random}")
            user_input = input("Слово за синим: ").lower()
            if user_input == "q":
                break
            while index < len(user_input):
                char = user_input[index]
                index += 1
                if char in eng_char:
                    print("Вы ввели слово на английском, переключите раскладку на русский")
                    break
                if char in vowels:
                    blue_word_points += 1
            print(f"Очки за слово: {blue_word_points}")
            blue_total += blue_word_points
            print(f"общий счёт:\n   Красный {red_total}\n   Синий {blue_total}\n"
                  f"__________________________________________")
    else:
        if red_total > blue_total:
            print(f"Красный игрок выигрывает со счётом: {red_total}\n"
                  f"_________________________________________")
        else:
            print(f"Синий игрок выигрывает со счётом: {blue_total}\n"
                  f"_________________________________________")
