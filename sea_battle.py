import random

# корабли имеют два атрибута: позицию первого блока(строка в виде "21"), длину корабля(инт цифры)
class Ship:
    def __init__(self, position_of_first_shipblock, lenth_of_ship):
        self.position = position_of_first_shipblock
        self.len = lenth_of_ship
    def get_len(self):
        return self.len
    def set_len(self, new_len):
        self.len = new_len
# Класс Поле имеет в себе словарь с данными о поле и 7 кораблей
class Field:
    def __init__(self):
        self.field = {}
        self.ship_1 = Ship('', 3)
        self.ship_2 = Ship('', 2)
        self.ship_3 = Ship('', 2)
        self.ship_4 = Ship('', 1)
        self.ship_5 = Ship('', 1)
        self.ship_6 = Ship('', 1)
        self.ship_7 = Ship('', 1)
        self.list_of_ships = [self.ship_1, self.ship_2, self.ship_3, self.ship_4, self.ship_5, self.ship_6, self.ship_7]
        self.count_of_decks = 0
        for i in range(1, 7):
            for j in range(1, 7):
                self.field[f'{i}{j}'] = "O"


    def print_field(self):
        for i in range(1, 7):
            if i == 1:
                print("   | 1 | 2 | 3 | 4 | 5 | 6 |", end="")
            print("\n", i, "|", end="")
            for j in range(1, 7):
                print("", self.field[f"{i}{j}"], "|", end="")

    # передается объект класса Ship
    def add_ship(self, ship):
    # проверка на то, можно ли туда поставить корабль
        # проверка на корректность ввода
        if not ship.position in self.field:
            raise ValueError("Неверно указана позиция корабля")
        elif not str(int(ship.position) + ship.len - 1) in self.field:
            raise ValueError("Длина корабля выходит за пределы поля")
        # проверка на свободное место на всю длину корабля
        for i in range(ship.len):
            cur_pos_str = str(int(ship.position) + i)
            if self.field[cur_pos_str] != "O":
                raise ValueError("Корабли не должны пересекаться")
        # проверка на отступы от корабля
        pos_end_str = str(int(ship.position) + ship.len - 1)
        if not (  ( ship.position[1] == '1' or self.field[str(int(ship.position) - 1)] == "O" )
            and ( pos_end_str[1] == '6' or self.field[str(int(pos_end_str) + 1)] == "O" )  ):
            raise ValueError("У корабля должны быть отступы в одну клетку")
    # ставим корабль
        for i in range(ship.len):
            self.field[str(int(ship.position) + i)] = "■"
            self.count_of_decks += 1

    # передается позиция в виде строки "31" и объект класса Field - поле с туманом войны
    def shot(self, pos, fog_field = None):
        if pos not in self.field:
            raise ValueError("Вы неверно ввели позицию корабля")
        if not fog_field:
            fog_field = Field()
        if self.field[pos] == "O":
            self.field[pos] = "T"
            fog_field.field[pos] = "T"
        elif self.field[pos] == "T" or self.field[pos] == "X":
            raise ValueError("Вы уже стреляли в эту точку. Введите другое значение")
        elif self.field[pos] == "■":
            self.field[pos] = "X"
            fog_field.field[pos] = "X"
            self.count_of_decks = list(self.field.values()).count("■")


# Передаем объект класса Field. Рандомно размещаем на нем корабли
def fill_with_random_ships(F):
    list_of_field_keys = list(F.field.keys())
    for ship in F.list_of_ships:
        while list_of_field_keys:
            try:
                key = random.choice(list_of_field_keys)
                list_of_field_keys.remove(key)
                ship.position = key
                F.add_ship(ship)
            except ValueError:
                continue
            else:
                break


print("Начальное поле игрока")
player_ships = []
player_field = Field()
player_field.print_field()
comp_ships = []
comp_field = Field()
comp_field_for_player = Field()
print()
# игрок вводит позиции кораблей
"""
while True:
    try:
        for i in range(1, 8):
            if i == 1:
                a = input("Введите номер позиции 3-х палубного корабля: ")
                ship = Ship(a, 3)
                player_field.add_ship(ship)
            elif i == 2 or i == 3:
                a = input(f"Введите номер позиции {i - 1}ого 2-х палубного корабля: ")
                ship = Ship(a, 2)
                player_field.add_ship(ship)
            else:
                a = input(f"Введите номер позиции {i - 3}ого однопалубного корабля: ")
                ship = Ship(a, 1)
                player_field.add_ship(ship)
    except ValueError as er:
        print(f"Ошибка: {er}!".upper())
        print("Ниже введите позиции всех кораблей заново")
    else:
        break
"""
# временный вариант для тестирования. Рандомно заполню поле игрока
fill_with_random_ships(player_field)

print("\n", "="*28)
print("Поле игрока с кораблями:")
player_field.print_field()
print("\n", "-"*28)
print("Поле компа:")
comp_field_for_player.print_field()
print("\n", "="*28)

fill_with_random_ships(comp_field)

# игра начинается
list_of_field_pos = list(player_field.field.keys()) # здесь все ключи для поля, по которым будет стрелять комп
num_of_rounds = 0
while player_field.count_of_decks and comp_field.count_of_decks:
    while True:
        try:
            shot = input("\nВведите номер поля для стрельбы: ")
            comp_field.shot(shot, comp_field_for_player)
        except ValueError as er:
            print(er)
            print("Попробуйте еще раз")
        else:
            break

    while True:
        shot = random.choice(list_of_field_pos)
        list_of_field_pos.remove(shot)
        try:
            player_field.shot(shot)
        except ValueError:
            continue
        else:
            break
    num_of_rounds += 1
    print(f"\nХОД НОМЕР {num_of_rounds}")
    print("Поле игрока:")
    player_field.print_field()
    print("\n", "-"*28)
    print("Поле компа:")
    comp_field_for_player.print_field()
    print("\n", "=" * 28)

if not player_field.count_of_decks:
    print("Компьютер победил!")
else:
    print("Игрок победил!")













