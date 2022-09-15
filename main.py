class BoardNum:
    def __init__(self, num_array=None):
        self.num_array = num_array
        if self.num_array is None:
            self.num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def game_window(self):
        print(f"{objektas.num_array[0]}|{objektas.num_array[1]}|{objektas.num_array[2]}")
        print(f"{objektas.num_array[3]}|{objektas.num_array[4]}|{objektas.num_array[5]}")
        print(f"{objektas.num_array[6]}|{objektas.num_array[7]}|{objektas.num_array[8]}\n")

    def turn_x(self):
        input_x = int(input("Kryziuku eile: "))
        if not isinstance(objektas.num_array[input_x - 1], int):
            print("Cia jau yra padetas zenklas!")
            objektas.game_window()
            objektas.turn_x()
        if input_x > 9 or input_x < 1:
            print("Neteisingai ivestas ejimas")
            objektas.game_window()
            objektas.turn_x()
        objektas.num_array[input_x - 1] = "x"

    def turn_o(self):
        input_o = int(input("Nuliuku eile: "))
        if not isinstance(objektas.num_array[input_o - 1], int):
            print("Cia jau yra padetas zenklas!")
            objektas.game_window()
            objektas.turn_o()
        if input_o > 9 or input_o < 1:
            print("Neteisingai ivestas ejimas")
            objektas.game_window()
            objektas.turn_o()
        objektas.num_array[input_o - 1] = "o"

    def check_game_state(self):
        if objektas.num_array[0] == objektas.num_array[1] and objektas.num_array[1] == objektas.num_array[2]:
            print(f"Laimejo {objektas.num_array[0]}")
            return True
        if objektas.num_array[3] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[5]:
            print(f"Laimejo {objektas.num_array[3]}")
            return True
        if objektas.num_array[6] == objektas.num_array[7] and objektas.num_array[7] == objektas.num_array[8]:
            print(f"Laimejo {objektas.num_array[6]}")
            return True
        if objektas.num_array[0] == objektas.num_array[3] and objektas.num_array[3] == objektas.num_array[6]:
            print(f"Laimejo {objektas.num_array[0]}")
            return True
        if objektas.num_array[1] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[7]:
            print(f"Laimejo {objektas.num_array[1]}")
            return True
        if objektas.num_array[2] == objektas.num_array[5] and objektas.num_array[5] == objektas.num_array[8]:
            print(f"Laimejo {objektas.num_array[2]}")
            return True
        if objektas.num_array[0] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[8]:
            print(f"Laimejo {objektas.num_array[0]}")
            return True
        if objektas.num_array[2] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[6]:
            print(f"Laimejo {objektas.num_array[2]}")
            return True
        if all(isinstance(x, str) for x in objektas.num_array):
            print("Lygiosios!")
            return True

    def game_state(self):  # True = veikia, False = neveikia
        turn = 0
        while True:
            objektas.num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            play_game = int(input("Ar norite zaisti? 1 - Taip, 2 - Ne "))
            if play_game == 2:
                break
            while True:
                turn += 1
                if objektas.check_game_state():
                    break
                objektas.game_window()
                if turn % 2 == 0:
                    objektas.turn_x()
                else:
                    objektas.turn_o()


objektas = BoardNum()
objektas.game_state()
