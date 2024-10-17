class CitiesGame:
    def __init__(self):
        self.cities = ["Москва", "Архангельск", "Киев", "Владивосток", "Калининград", "Донецк", "Краснодар"]
        self.used_cities = set()
        self.last_city = None
        self.message = "Игра началась! Назовите город."

    def make_move(self, city):
        if city not in self.cities:
            self.message = f"Город отсутствует в списке доступных городов"
            return False
        if self.last_city and city[0].lower() != self.last_city[-1].lower():
            self.message = f"Город должен начинаться с последней буквы предыдущего города"
            return False
        if city in self.used_cities:
            self.message = f"Город '{city}' уже был использован."
            return False
        
        self.used_cities.add(city)
        self.last_city = city
        if self.is_game_over():
            self.message = "Игра окончена! Больше нет возможных ходов."
        else:
            self.message = f"Ход принят. Следующий город должен начинаться на букву '{city[-1].upper()}'."
        return True

    def is_game_over(self):
        if not self.last_city:
            return False
        game_over = all(city in self.used_cities or city[0].lower() != self.last_city[-1].lower() for city in self.cities)
        if game_over:
            self.message = "Игра окончена! Больше нет возможных ходов."
        return game_over

    def get_message(self):
        return self.message