class BoardNum:
    def __init__(self, num_array=None, win_x=0, win_o=0, draw=0, play_again=0):
        if num_array is None:
            num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.num_array = num_array
        self.win_x = win_x
        self.win_o = win_o
        self.draw = draw
        self.play_again = play_again

    class WinCounter:
        def __init__(self, win_x=0, win_o=0, draw=0):
            self.win_x = win_x
            self.win_o = win_o
            self.draw = draw

    def game_window(self):
        print(f"{objektas.num_array[6]}|{objektas.num_array[7]}|{objektas.num_array[8]}")
        print(f"{objektas.num_array[3]}|{objektas.num_array[4]}|{objektas.num_array[5]}")
        print(f"{objektas.num_array[0]}|{objektas.num_array[1]}|{objektas.num_array[2]}\n")

    def turn_x(self):
        input_x = int(input("Kryžiukų eile: "))
        if not isinstance(objektas.num_array[input_x - 1], int):
            print("Čia jau yra padėtas ženklas!")
            objektas.game_window()
            objektas.turn_x()
        if input_x > 9 or input_x < 1:
            print("Neteisingai įvestas ėjimas")
            objektas.game_window()
            objektas.turn_x()
        objektas.num_array[input_x - 1] = "x"

    def turn_o(self):
        input_o = int(input("Nuliukų eilė: "))
        if not isinstance(objektas.num_array[input_o - 1], int):
            print("Cia jau yra padetas zenklas!")
            objektas.game_window()
            objektas.turn_o()
        if input_o > 9 or input_o < 1:
            print("Neteisingai įvestas ėjimas")
            objektas.game_window()
            objektas.turn_o()
        objektas.num_array[input_o - 1] = "o"

    def check_game_state(self):
        if objektas.num_array[0] == objektas.num_array[1] and objektas.num_array[1] == objektas.num_array[2]:
            print(f"Laimėjo {objektas.num_array[0]}")
            if objektas.num_array[0] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[3] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[5]:
            print(f"Laimėjo {objektas.num_array[3]}")
            if objektas.num_array[3] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[6] == objektas.num_array[7] and objektas.num_array[7] == objektas.num_array[8]:
            print(f"Laimėjo {objektas.num_array[6]}")
            if objektas.num_array[6] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[0] == objektas.num_array[3] and objektas.num_array[3] == objektas.num_array[6]:
            print(f"Laimėjo {objektas.num_array[0]}")
            if objektas.num_array[0] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[1] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[7]:
            print(f"Laimėjo {objektas.num_array[1]}")
            if objektas.num_array[1] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[2] == objektas.num_array[5] and objektas.num_array[5] == objektas.num_array[8]:
            print(f"Laimėjo {objektas.num_array[2]}")
            if objektas.num_array[2] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[0] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[8]:
            print(f"Laimėjo {objektas.num_array[0]}")
            if objektas.num_array[0] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if objektas.num_array[2] == objektas.num_array[4] and objektas.num_array[4] == objektas.num_array[6]:
            print(f"Laimėjo {objektas.num_array[2]}")
            if objektas.num_array[2] == "x":
                objektas.win_x += 1
            else:
                objektas.win_o += 1
            return True
        if all(isinstance(x, str) for x in objektas.num_array):
            print("Lygiosios!")
            objektas.draw += 1
            return True

    def game_state(self):
        turn = 0
        while True:
            if objektas.play_again == 1:
                will_play = int(input("Ar norite zaisti dar karta? 1 - TAIP, 2 - NE"))
                if will_play == 1:
                    objektas.num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                else:
                    break
            while True:
                turn += 1
                if objektas.check_game_state():
                    objektas.game_window()
                    print(f"Kryziuku pergales: {objektas.win_x}\n"
                          f"Nuliuku pergales: {objektas.win_o}\n"
                          f"Lygiosios: {objektas.draw}")
                    objektas.play_again = 1
                    break
                objektas.game_window()
                if turn % 2 == 0:
                    objektas.turn_x()
                else:
                    objektas.turn_o()


objektas = BoardNum()
objektas.game_state()
