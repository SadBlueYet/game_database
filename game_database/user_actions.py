from database import Database
from tabulate import tabulate
import os


class Actions:
    # Конструктор класса
    def __init__(self, db: Database, headers: list[str]):
        self.db = db
        self.headers = headers

    # Получение всех игр
    def get_all_games(self):
        games = self.db.get_all_games()
        os.system("cls")
        #  Вывод в формате таблицы
        print(tabulate(games, headers=self.headers), "\n\n")

    # Получение игры по id
    def get_game_by_id(self):
        os.system("cls")
        try:
            user_choise = int(input("Введите id игры\n>>"))
            game = self.db.get_game_by_id(user_choise)
            # Если игра не найдена
            if game is None:
                print("\n\nИгра c таким id не найдена\n\n")
                return

            print(tabulate([game], headers=self.headers), "\n\n")
        except ValueError as e:
            print(f"Необходимо ввести целое число\n\n")

    # Получение игры по названию
    def get_game_by_name(self):
        os.system("cls")
        user_choise = input("Введите название игры\n>>")
        game = self.db.get_game_by_name(user_choise)
        # Если игра не найдена
        if not game:
            print("\n\nИгра c таким названием не найдена\n\n")
            return
        # Вывод в формате таблицы
        print(tabulate(game, headers=self.headers), "\n\n")

    # Получение игры по издателю
    def get_game_by_publisher(self):
        os.system("cls")

        user_choise = input("Введите издателя игры\n>>")
        game = self.db.get_game_by_publisher(user_choise)
        # Если игра не найдена
        if not game:
            print("\n\nИгра c таким издателем не найдена\n\n")
            return
        # Вывод в формате таблицы
        print(tabulate(game, headers=self.headers), "\n\n")

    # Получение игры по году публикации
    def get_game_by_year(self):
        os.system("cls")
        try:
            user_choise = int(input("Введите год публикации игры\n>>"))
            game = self.db.get_game_by_year(user_choise)
            # Если игра не найдена
            if not game:
                print("\n\nИгра c таким годом публикации не найдена\n\n")
                return
            # Вывод в формате таблицы
            print(tabulate(game, headers=self.headers), "\n\n")
        except ValueError as e:
            print(f"Необходимо ввести целое число\n\n")

    # Получение игры по всем критериям
    def get_game_by_all_criteria(self):
        os.system("cls")
        game_title = input("Введите название игры\n>>")
        game_publisher = input("Введите издателя игры\n>>")

        try:
            game_year = int(input("Введите год публикации игры\n>>"))
            game = self.db.get_game_by_all_criteria(
                game_title, game_publisher, game_year
            )
            # Если игра не найдена
            if not game:
                print("\n\nИгра с такими критериями не найдена\n\n")
                return
            # Вывод в формате таблицы
            print(tabulate(game, headers=self.headers), "\n\n")
        except ValueError as e:
            print(f"Необходимо ввести целое число\n\n")

    # Метод, определяющий по каким критериям получать игру
    def get_game(self):
        os.system("cls")
        menu = (
            "[1] - Найти игру по id\n"
            "[2] - Найти игру по названию\n"
            "[3] - Найти игру по издателю\n"
            "[4] - Найти игру по году публикации\n"
            "[5] - Найти игру по всем критериям\n"
            "[0] - Назад\n>>"
        )
        try:
            user_choise = int(input(menu))
            match user_choise:
                case 1:
                    self.get_game_by_id()
                case 2:
                    self.get_game_by_name()
                case 3:
                    self.get_game_by_publisher()
                case 4:
                    self.get_game_by_year()
                case 5:
                    self.get_game_by_all_criteria()
                case 0:
                    os.system("cls")
                    return
        except ValueError as e:
            print(f"Необходимо ввести целое число\n\n")

    # Добавление игры
    def add_game(self):
        while True:
            os.system("cls")

            game_title = input("Введите название игры\n>>")
            if game_title == "":
                print("\n\nНазвание игры не может быть пустым\n\n")
                continue

            publisher = input("Введите издателя игры\n>>")
            if publisher == "":
                print("\n\nИздатель игры не может быть пустым\n\n")
                continue
            try:
                year_of_publication = int(input("Введите год публикации игры\n>>"))
            except ValueError as e:
                print(f"Необходимо ввести целое число\n\n")
                continue

            self.db.add_game(game_title, publisher, year_of_publication)

            print("\n\nИгра добавлена\n\n")
            return

    # Метод, определяющий какие критерии нужно изменить
    def edit_game(self):
        os.system("cls")
        menu = (
            "[1] - Изменить название игры\n"
            "[2] - Изменить издателя игры\n"
            "[3] - Изменить год публикации игры\n"
            "[0] - Назад\n>>"
        )
        while True:
            try:
                game_id = int(input("Введите id игры для редактирования\n>>"))
                user_choice = int(input(menu))
                # Изменение данных игры
                match user_choice:
                    case 1:
                        new_name = input("Введите новое название игры\n>>")
                        self.db.edit_name(id=game_id, name=new_name)
                    case 2:
                        new_publisher = input("Введите нового издателя игры\n>>")
                        self.db.edit_publisher(id=game_id, publisher=new_publisher)
                    case 3:
                        new_year = int(input("Введите новый год публикации игры\n>>"))
                        self.db.edit_year(id=game_id, year=new_year)
                    case 0:
                        continue

                print("\n\nИгра успешно отредактирована\n\n")
                return
            except ValueError as e:
                print(f"Необходимо ввести целое число\n\n")

    # Удаление игры
    def delete_game(self):
        os.system("cls")
        while True:
            try:
                game_id = int(input("Введите id игры для удаления\n>>"))
                game = self.db.get_game_by_id(game_id)
                # Если игра не найдена
                if not game:
                    print("\n\nИгра c таким id не найдена\n\n")
                    continue

                print("Вы уверены, что хотите удалить эту игру?\n\n")
                print(
                    tabulate([game], headers=self.headers), "\n\n[1] - Да\n[0] - Нет\n"
                )

                user_choice = int(input(">>"))
            except ValueError as e:
                print(f"Необходимо ввести целое число\n\n")
                continue

            match user_choice:
                case 1:
                    self.db.delete_game(id=game_id)
                case 2:
                    return
            print("\n\nИгра удалена\n\n")
            return
