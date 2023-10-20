import os
import sys
import aiosqlite



class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name

    async def __create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY,
                game_title TEXT,
                publisher TEXT,
                year_of_publication INTEGER
            )
        """
        await self.__execute_query(query=query)

    async def reconnect(self):
        await self.__connection.close()
        os.system("run.bat")

    async def connect(self):
            self.__connection = await aiosqlite.connect(self.db_name)
            await self.__create_table()

    async def disable(self):
        await self.__connection.close()

    async def __execute_query(self, query, params=None):
        if params:
            cur = await self.__connection.execute(query, params)
        else:
            cur = await self.__connection.execute(query)
        
        await self.__connection.commit()
        return cur
        
    async def add_game(self, game_title: str, publisher: str, year_of_publication: int):
        query = "INSERT INTO games (game_title, publisher, year_of_publication) VALUES (?, ?, ?)"
        params = (game_title, publisher, year_of_publication)
        await self.__execute_query(query, params)

    async def get_all_games(self):
        query = "SELECT * FROM games"
        return await self.__execute_query(query)

    async def get_game(self, game_publisher=None, game_name=None, game_year=None) -> list:
        if game_publisher is not None:
            query = "SELECT * FROM games WHERE publisher = ?"
            params = (game_publisher,)
        elif game_name is not None:
            query = "SELECT * FROM games WHERE game_title = ?"
            params = (game_name,)
        elif game_year is not None:
            query = "SELECT * FROM games WHERE year_of_publication = ?"
            params = (game_year,)

        return await self.__execute_query(query, params)
    
    async def edit_game(self, id, game_name=None, game_publisher=None, game_year=None) -> None:
        if game_name is not None:
            query = "UPDATE games SET game_title = ? WHERE id = ?"
            params = (game_name, id,)
        elif game_publisher is not None:
            query = "UPDATE games SET publisher = ? WHERE id = ?"
            params = (game_publisher, id,)
        elif game_year is not None:
            query = "UPDATE games SET year_of_publication = ? WHERE id = ?"
            params = (game_year, id,)
        
        await self.__execute_query(query, params)

    async def delete_game(self, game_id: int):
        query = "DELETE FROM games WHERE id = ?"
        await self.__execute_query(query, (game_id,))