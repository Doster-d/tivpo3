from behave import given, when, then
from cities_game import CitiesGame

@given('игра не начата')
def step_impl(context):
    context.game = None

@when('я начинаю новую игру')
def step_impl(context):
    context.game = CitiesGame()

@then('я должен увидеть сообщение о начале игры')
def step_impl(context):
    assert context.game is not None
    assert context.game.get_message() == "Игра началась! Назовите город."

@given('игра начата')
def step_impl(context):
    context.game = CitiesGame()

@given('последний названный город "{gorod}"')
def step_impl(context, gorod):
    context.game.make_move(gorod)

@when('я называю город "{gorod}"')
def step_impl(context, gorod):
    context.rezultat_hoda = context.game.make_move(gorod)

@then('ход должен быть принят')
def step_impl(context):
    assert context.rezultat_hoda is True

@then('"{gorod}" должен быть добавлен в список использованных городов')
def step_impl(context, gorod):
    assert gorod in context.game.used_cities

@then('я должен увидеть сообщение о принятии хода')
def step_impl(context):
    assert "Ход принят" == context.game.get_message()

@then('ход должен быть отклонен')
def step_impl(context):
    assert context.rezultat_hoda is False

@then('я должен увидеть сообщение об ошибке "{soobshchenie}"')
def step_impl(context, soobshchenie):
    assert soobshchenie == context.game.get_message()

@given('все города, начинающиеся с последней буквы предыдущего города, уже использованы')
def step_impl(context):
    context.game.cities = ["Москва", "Архангельск"]
    context.game.make_move("Москва")
    context.game.make_move("Архангельск")

@when('я пытаюсь сделать ход')
def step_impl(context):
    context.konec_igry = context.game.is_game_over()

@then('игра должна закончиться')
def step_impl(context):
    assert context.konec_igry is True

@then('я должен увидеть сообщение "Игра окончена! Больше нет возможных ходов."')
def step_impl(context):
    assert "Игра окончена! Больше нет возможных ходов." == context.game.get_message()
