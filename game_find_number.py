import random

game_info = {
    'secret_figure': random.randint(1, 100),
    'game_status': 1,
    'selected_numbers': [],
    'attempts': 0,
}


def find_number():
    global game_info
    print("\nВы Угадали число! Подздравляю!")
    print(f"Количество попыток {game_info['attempts']}. ")
    print('Попытки:', game_info['selected_numbers'])

    restart = input("Хотите повторить игру?[y/n]: ")
    if restart in ["y", "yes"]:
        game_info['secret_figure'] = random.randint(1, 100)
        game_info['game_status'] = 1
        game_info['selected_numbers'] = []
        game_info['attempts'] = 0
        print("УГАДАЙТЕ ЧИСЛО:", end="\n\n")
    else:
        print("Спасибо за игру!")
        game_info['game_status'] = 0


def not_find(number):
    global game_info
    game_info['attempts'] += 1
    game_info['selected_numbers'].append(number)
    print(f"secret key not = {number}", "Мало" if number < game_info['secret_figure'] else "Много")


def start_game():
    print("УГАДАЙТЕ ЧИСЛО:", end="\n\n")
    while game_info['game_status']:
        # print("Введите число:", end=" ")
        number = int(input("Введите число:"))

        # out of range
        if not 1 <= number <= 100:
            print("Число выходит за диапозон 1<= x <= 100")

        # find number
        elif number == game_info['secret_figure']:
            find_number()

        # not find
        else:
            not_find(number)


if __name__ == "__main__":
    print("УГАДАЙТЕ ЧИСЛО:", game_info['secret_figure'])
    start_game()




