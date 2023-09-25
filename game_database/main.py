from database import Database
from user_actions import Actions
import user_actions as ua


def main():
    headers = ["Номер", "Название", "Издатель", "Год публикации"]
    menu = (
        "[1] - Показать все игры\n"
        "[2] - Найти игру по критериям\n"
        "[3] - Добавить игру\n"
        "[4] - Редактировать данные об игре\n"
        "[5] - Удалить игру\n"
        "[0] - Выход\n>>"
    )

    db = Database()
    actions = Actions(db, headers)

    while True:
        try:
            user_choise = int(input(menu))
        except ValueError as e:
            print(f"{e}\nВведите целое число")
            continue

        match user_choise:
            case 1:
                actions.get_all_games()
            case 2:
                actions.get_game()
            case 3:
                actions.add_game()
            case 4:
                actions.edit_game()
            case 5:
                actions.delete_game()
            case 0:
                break


if __name__ == "__main__":
    main()
