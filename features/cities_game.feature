# language: ru
Функционал: Игра "Города"
  Как игрок
  Я хочу играть в игру "Города"
  Чтобы проверить свои знания названий городов

  Сценарий: Начало новой игры
    Дано игра не начата
    Когда я начинаю новую игру
    Тогда я должен увидеть сообщение о начале игры

  Сценарий: Сделать правильный ход
    Дано игра начата
    И последний названный город "Москва"
    Когда я называю город "Архангельск"
    Тогда ход должен быть принят
    И "Архангельск" должен быть добавлен в список использованных городов

  Сценарий: Сделать неправильный ход - неверная первая буква
    Дано игра начата
    И последний названный город "Москва"
    Когда я называю город "Киев"
    Тогда ход должен быть отклонен
    И я должен увидеть сообщение об ошибке "Город должен начинаться с последней буквы предыдущего города"

  Сценарий: Сделать неправильный ход - город не из списка
    Дано игра начата
    Когда я называю город "Париж"
    Тогда ход должен быть отклонен
    И я должен увидеть сообщение об ошибке "Город отсутствует в списке доступных городов"

  Сценарий: Конец игры - нет больше возможных ходов
    Дано игра начата
    И все города, начинающиеся с последней буквы предыдущего города, уже использованы
    Когда я пытаюсь сделать ход
    Тогда игра должна закончиться
    И я должен увидеть сообщение "Игра окончена! Больше нет возможных ходов."