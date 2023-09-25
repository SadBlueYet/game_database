import sqlite3


class Database:
    def __init__(self):
        try:
            self.connection = sqlite3.connect("database.db")
            self.cursor = self.connection.cursor()
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS games (id INTEGER PRIMARY KEY, game_title TEXT, publisher TEXT, year_of_publication TEXT)"
            )
        except sqlite3.Error as e:
            print("Error initializing the database:", e)

    def add_game(self, game_title, publisher, year_of_publication):
        try:
            query = "INSERT INTO games (game_title, publisher, year_of_publication) VALUES (?, ?, ?)"
            self.cursor.execute(query, (game_title, publisher, year_of_publication))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error inserting game:", e)

    def get_all_games(self):
        try:
            query = "SELECT * FROM games"
            self.cursor.execute(query)
            games = self.cursor.fetchall()
            return games
        except sqlite3.Error as e:
            print("Error getting all games:", e)
            return

    def get_game_by_id(self, game_id):
        try:
            query = "SELECT * FROM games WHERE id = ?"
            self.cursor.execute(query, (game_id,))
            game = self.cursor.fetchone()
            return game
        except sqlite3.Error as e:
            print("Error getting game by id:", e)
            return

    def get_game_by_publisher(self, game_publisher):
        try:
            query = "SELECT * FROM games WHERE publisher = ?"
            self.cursor.execute(query, (game_publisher,))
            game = self.cursor.fetchall()
            return game
        except sqlite3.Error as e:
            print("Error getting game by publisher:", e)
            return

    def get_game_by_name(self, game_name):
        try:
            query = "SELECT * FROM games WHERE game_title = ?"
            self.cursor.execute(query, (game_name,))
            game = self.cursor.fetchall()
            return game
        except sqlite3.Error as e:
            print("Error getting game by name:", e)
            return

    def get_game_by_year(self, game_year):
        try:
            query = "SELECT * FROM games WHERE year_of_publication = ?"
            self.cursor.execute(query, (game_year,))
            game = self.cursor.fetchall()
            return game
        except sqlite3.Error as e:
            print("Error getting game by year:", e)
            return

    def get_game_by_all_criteria(
        self, game_title: str, game_publisher: str, game_year: int
    ):
        try:
            query = "SELECT * FROM games WHERE game_title = ? AND publisher = ? AND year_of_publication = ?"
            self.cursor.execute(query, (game_title, game_publisher, game_year))
            game = self.cursor.fetchall()
            return game
        except sqlite3.Error as e:
            print("Error getting game by all criteria:", e)
            return

    def edit_name(self, name: str, id: int):
        try:
            query = "UPDATE games SET game_title = ? WHERE id = ?"
            self.cursor.execute(query, (name, id))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error editing game name:", e)

    def edit_publisher(self, publisher: str, id: int):
        try:
            query = "UPDATE games SET publisher = ? WHERE id = ?"
            self.cursor.execute(query, (publisher, id))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error editing game publisher:", e)

    def edit_year(self, year: int, id: int):
        try:
            query = "UPDATE games SET year_of_publication = ? WHERE id = ?"
            self.cursor.execute(query, (year, id))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error editing game year:", e)

    def delete_game(self, id: int):
        try:
            query = "DELETE FROM games WHERE id = ?"
            self.cursor.execute(query, (id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error deleting game:", e)
