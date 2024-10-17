from cities_game import CitiesGame

def play_game():
    game = CitiesGame()
    print("Добро пожаловать в игру 'Города'!")
    print("Чтобы выйти из игры, введите 'выход'.")
    
    while not game.is_game_over():
        print("\n" + game.get_message())
        city = input("Введите название города: ").strip().capitalize()
        
        if city.lower() == 'выход':
            print("Спасибо за игру! До свидания!")
            break
        
        game.make_move(city)
    
    if game.is_game_over():
        print("\n" + game.get_message())

if __name__ == "__main__":
    play_game()