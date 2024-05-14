from game_logic import play_round
from settings import read_initial_money

def main():
    capital = read_initial_money()
    bet = 0

    while True:
        print(f"Ваш текущий капитал: ${capital}")
        bet = int(input("Сколько денег вы хотите поставить на число от 1 до 10? (0 для выхода): "))

        if bet == 0:
            break

        if bet > capital:
            print("У вас недостаточно денег для этой ставки!")
            continue

        chosen_number = int(input("На какое число вы ставите? (от 1 до 10): "))

        result, winning_number = play_round(bet, chosen_number)
        capital += result

        if result > 0:
            print(f"Поздравляем! Вы выиграли ${result}! Выигрышное число: {winning_number}")
        else:
            print(f"К сожалению, вы проиграли ${abs(result)}. Выигрышное число: {winning_number}")

        play_again = input("Хотите сыграть еще раз? (да/нет): ")
        if play_again.lower() != 'да':
            break

    print(f"Игра окончена. Ваш итоговый капитал: ${capital}")
    if capital > read_initial_money():
        print("Поздравляем, вы в выигрыше!")
    else:
        print("К сожалению, вы в проигрыше.")


if __name__ == "__main__":
    main()
