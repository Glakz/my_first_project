from getpass import getpass


while True:
    print("                 Угадай слово        ")
    quit_game = input("подтвердите начало игры введя 1, при вводе любого другого символа игра закроется: ")
    if quit_game != "1":
        break
    word_secred = getpass("         Загадайте слово и введите\n" \
    "Но будьте внимательны так как вы не увидите что вводите: ").lower().strip()
    hidden_word = ["_"] * len(word_secred)
    print(f"вы загадали слово {"*" * len(word_secred)} состоящее из {len(word_secred)} символов\n"
          "____________________________________________________________")
    while True:
        if "".join(hidden_word) != word_secred:
            secred_char = input("Отгадайте букву из секретного слова: ")
            if len(secred_char) != 1:
                print("Ошибка! Нужно ввести строго одну букву.")
                continue
            if secred_char in word_secred:
                count_index = 0
                while count_index < len(word_secred):
                    if secred_char == word_secred[count_index]:
                        hidden_word[count_index] = secred_char
                    count_index += 1
                print(f"Ваш результат: {''.join(hidden_word)}")

            else:
                print("Такой буквы нет!!!")    

        else:
            print(f"вы загадали слово: {''.join(hidden_word)}")
            break