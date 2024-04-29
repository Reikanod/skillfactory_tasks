def check_for_win(player_num, cell_num, field_1):
    symbol = ""
    if player_num == 1:
        symbol = 'X'
    else:
        symbol = '0'
    field_1[cell_num] = symbol
    print_field(field_1)
    if (    field_1['00'] == field_1['10'] == field_1['20'] != '-' or
            field_1['01'] == field_1['11'] == field_1['21'] != '-' or
            field_1['02'] == field_1['12'] == field_1['22'] != '-' or
            field_1['00'] == field_1['11'] == field_1['22'] != '-' or
            field_1['02'] == field_1['11'] == field_1['20'] != '-'    ):
        print(f"Игрок {player_num} победил!")
        return True
    else:
        return False


def print_field(field_2):
    print(f"""
      0 1 2
    0 {field_2['00']} {field_2['10']} {field_2['20']}
    1 {field_2['01']} {field_2['11']} {field_2['21']}
    2 {field_2['02']} {field_2['12']} {field_2['22']}""")


player_number = None
cell_num = None
field = {
    '00': '-', '10': '-', '20': '-',
    '01': '-', '11': '-', '21': '-',
    '02': '-', '12': '-', '22': '-'
}

print("Начинаем игру.\nСначала вводим номер столбца, потом строки в формате '01'\nПоле:")
print_field(field)
while True:
    cell_num = input("Ход первого игрока: ")
    player_number = 1
    if check_for_win(player_number, cell_num, field):
        break
    cell_num = input("Ход второго игрока: ")
    player_number = 2
    if check_for_win(player_number, cell_num, field):
        break