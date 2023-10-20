from user_actions import Actions
import time
import asyncio 


class GameInterface:

    def __init__(self):
        self.actions = Actions()
        self.user_input = self.actions.user_input
        
    
    async def interface(self):
        menu = (
        "[1] - Показать все игры\n"
        "[2] - Найти игру по критериям\n"
        "[3] - Добавить игру\n"
        "[4] - Редактировать данные об игре\n"
        "[5] - Удалить игру\n"
        "[0] - Выход"
        )

        while True:
            try:
                
                user_choise = await self.user_input.input_integer(menu)

                if user_choise == 1:
                    await self.actions.get_all_games()
                elif user_choise == 2:
                    await self.actions.get_game()
                elif user_choise == 3:
                    await self.actions.add_game()
                elif user_choise == 4:
                    await self.actions.edit_game()
                elif user_choise == 5:
                    await self.actions.delete_game()
                elif user_choise == 0:
                    await self.actions.db.disable()
                    return
                else:
                    await self.user_input.clear_screen()
                    print("\n\nНеверный выбор\n\n")
                                   
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                time.sleep(5)
                await self.actions.db.reconnect()
    
    async def connect(self):
        await self.actions.db.connect()

    

async def main():

    game_interface = GameInterface()
    await game_interface.connect()
    await game_interface.interface()


if __name__ == "__main__":
    asyncio.run(main())
