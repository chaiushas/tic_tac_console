num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def game_window():
    print(f"{num_array[0]}|{num_array[1]}|{num_array[2]}")
    print(f"{num_array[3]}|{num_array[4]}|{num_array[5]}")
    print(f"{num_array[6]}|{num_array[7]}|{num_array[8]}\n")


def turn_x():
    input_x = int(input("Kryziuku eile: "))
    if not isinstance(num_array[input_x - 1], int):
        print("Cia jau yra padetas zenklas!")
        game_window()
        turn_x()
    if input_x > 9 or input_x < 1:
        print("Neteisingai ivestas ejimas")
        game_window()
        turn_x()
    num_array[input_x - 1] = "x"


def turn_o():
    input_o = int(input("Nuliuku eile: "))
    if not isinstance(num_array[input_o - 1], int):
        print("Cia jau yra padetas zenklas!")
        game_window()
        turn_o()
    if input_o > 9 or input_o < 1:
        print("Neteisingai ivestas ejimas")
        game_window()
        turn_o()
    num_array[input_o - 1] = "o"


def check_game_state():
    if num_array[0] == num_array[1] and num_array[1] == num_array[2]:
        print(f"Laimejo {num_array[0]}")
        return True
    if num_array[3] == num_array[4] and num_array[4] == num_array[5]:
        print(f"Laimejo {num_array[3]}")
        return True
    if num_array[6] == num_array[7] and num_array[7] == num_array[8]:
        print(f"Laimejo {num_array[6]}")
        return True
    if num_array[0] == num_array[3] and num_array[3] == num_array[6]:
        print(f"Laimejo {num_array[0]}")
        return True
    if num_array[1] == num_array[4] and num_array[4] == num_array[7]:
        print(f"Laimejo {num_array[1]}")
        return True
    if num_array[2] == num_array[5] and num_array[5] == num_array[8]:
        print(f"Laimejo {num_array[2]}")
        return True
    if num_array[0] == num_array[4] and num_array[4] == num_array[8]:
        print(f"Laimejo {num_array[0]}")
        return True
    if num_array[2] == num_array[4] and num_array[4] == num_array[6]:
        print(f"Laimejo {num_array[2]}")
        return True
    if all(isinstance(x, str) for x in num_array):
        print("Lygiosios!")
        return True


def game_state(state):  # True = veikia, False = neveikia
    turn = 0
    while state:
        if check_game_state():
            break
        turn += 1
        game_window()
        if turn % 2 == 0:
            turn_x()
        else:
            turn_o()


game_state(True)
