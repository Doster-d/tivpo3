import unittest
from cities_game import CitiesGame

class TestCitiesGame(unittest.TestCase):

    def setUp(self):
        self.game = CitiesGame()

    def test_initialize_game(self):
        self.assertIsNotNone(self.game.cities)
        self.assertGreater(len(self.game.cities), 0)

    def test_valid_move(self):
        self.game.cities = ["Москва", "Архангельск", "Киев"]
        self.assertTrue(self.game.make_move("Москва"))
        self.assertEqual(self.game.last_city, "Москва")

    def test_invalid_move_wrong_first_letter(self):
        self.game.cities = ["Москва", "Архангельск", "Киев"]
        self.game.last_city = "Москва"
        self.assertFalse(self.game.make_move("Киев"))

    def test_invalid_move_city_not_in_list(self):
        self.game.cities = ["Москва", "Архангельск", "Киев"]
        self.assertFalse(self.game.make_move("Париж"))

    def test_game_over(self):
        self.game.cities = ["Москва", "Архангельск"]
        self.game.make_move("Москва")
        self.game.make_move("Архангельск")
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()