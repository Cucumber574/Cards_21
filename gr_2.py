from random import shuffle
from os import system
'''
Карта 
{
    'цена': 10
    'масть': 'пик'
    'название': '10'
}

Масти:
    черви, пики, бубны, крести

Колода:
    на каждую масть карты от 6 до туза = 36

Игроки
    от 2 до ...

Перетасовать колоду

Каждому игроку даем 2 карты
Можно смотреть только свои

Ход
    беру еще карту(сколько угодно, не больше чем осталось в колоде)
    или закончить ход

Каждый игрок делает 1 ход за партию

Если сумма всех карт игроков > 21, то это проигыш
Если все игроки проиграли, то ничья
Кто набрал самую большую сумму цен своих карт, то он победитель
'''

def get_deck() -> list[dict]: 
    '''Возращает колоду карт'''
    suits = ('черви', 'пики', 'бубны', 'крести')
    cards = {
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Валет': 2,
        'Дама': 3,
        'Король': 4,
        'Туз': 11,
        }
    deck = []
    for suit in suits:
        for item in cards:
            card = {
                'цена': cards[item],
                'масть': suit,
                'название': item
            }
            deck.append(card)
    return deck


def get_players() -> list[dict]:
    '''Возращает список игроков'''
    player_1 = {
        'имя': 'Вася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }

    player_2 = {
        'имя': 'Ася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    '''Раздает 2 карты каждому игроку'''
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop())

def show_cards() -> None:
    for card in player['карты']:
        print(card['название'], card['масть'])

deck = get_deck()
shuffle(deck)
players = get_players()
deal_cards(2)

for player in players:
    while True:
        system('cls')
        show_cards()
        player_option = input('Взять карту из колоды (y/n)? ')
        if player_option.lower() == 'y':
            player['карты'].append(deck.pop())
        else:
            break


system('cls')
for player in players:
    player['сумма'] = 0
    for card in player['карты']:
        player['сумма'] += card['цена']
    print(player['имя'], player['сумма'])

#print(max)


#победа
#перебор
#создавание доп. игроков