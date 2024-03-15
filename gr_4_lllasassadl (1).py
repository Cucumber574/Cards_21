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
        'человек': False,
        'сумма': 0
        'предел': 16
    }

    player_2 = {
        'имя': 'Виндус',
        'карты': [],
        'человек': False,
        'сумма': 0
        'предел': 17
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

def calculate_total_values(player: dict) -> None:
    total = 0
    for card in player['карты']:
        total += card['цена']
    player['сумма'] = total

deck = get_deck()
show_cards()
shuffle(deck)
players = get_players()
cards_per_turn = len(deck) // len(players)
deal_cards(2)
show_stat()

for player in players:
    while True:
        system('cls')
        show_cards()
        calculate_total_values(player)
        print('сумма очков:', player['сумма'])

        if player['человек']:
            player_option = input('Взять карту из колоды (y/n)? ')
        else:
            if player['сумма'] < player['предел']:
                player_option = 'y'
            else:
                player_option = 'n'
        if player_option.lower() == 'y':
            if len(player['карты']) < cards_per_turn:
                player['карты'].append(deck.pop())
            else:
                print('Нельзя больше брать карты')
                break
        else:
            break
    input('ENTER - следующий игрок')

system('cls')
show_stat()


total_values = [player['сумма'] for player in players] 

if total_values.count(total_values[0] == len(total_values))
    print('Ничья')
else:
    total_values = [player['сумма'] for player in players if player['сумма'] < 22]
    for player in players:
            if player['сумма'] == max(total_values):
                print('Победил', player['имя'])

def show_stat() -> None:
    ''' Выводит очки'''
    players_total_values = [player['сумма'] for player in players if player['сумма'] < 22]
    max_value = max(players_total_values)

    for player in players:
        if player['сумма'] > 21:
            print(player['имя'], player['сумма'], '- перебор!')
        else:
            print(player['имя'], player['сумма'], '- ничья')

