
import time as t
import random as r

class Jokenpo:

    def __init__(self):
        self.creates_double_lines()
        print("JOKENPÔ - CONTRA O COMPUTADOR")
        self.creates_double_lines()
        self.machine_choice = ""
        self.person_choice = 0
        self.options_list = ["PEDRA", "PAPEL", "TESOURA"]


    def delay_time(self):
        print("COMPUTADOR PENSANDO...")
        list_points_quantity = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        quantity_chosen = r.choice(list_points_quantity)
        for _ in range(quantity_chosen):
            seconds_list = [0.1, 0.2, 0.3, 0.4, 0.5]
            second_chosen = r.choice(seconds_list)
            t.sleep(second_chosen)
            print(".")
            second_chosen = r.choice(seconds_list)
            t.sleep(second_chosen)
        self.creates_double_lines()


    def creates_double_lines(self):
        print("=" * 60)


    def creates_simple_line(self):
        print("-" * 60)


    def introduction(self):
        print("INSTRUCÕES DE COMO JOGAR:")
        self.creates_simple_line()
        print("1--PEDRA")
        print("2--PAPEL")
        print("3--TESOURA")
        print("0--SAIR")
        self.creates_simple_line()


    def computer_choice_value(self):
        self.machine_choice = r.choice(self.options_list)
        return self.machine_choice
    

    def person_choice_value(self):
        self.person_choice = int(input("DIGITE O NÚMERO DA SUA ESCOLHA: "))
        self.creates_simple_line()
        return self.person_choice
    

    def show_choices(self):
        control_variable = True

        
        while control_variable:
            self.person_choice = self.person_choice_value()
            if self.person_choice == 0:
                print("FIM DE JOGO!!!")
                control_variable = False

            elif self.person_choice > 0 and self.person_choice < 4:
                self.delay_time()
                self.machine_choice = self.computer_choice_value()
                print(f"HUMANO(VOCÊ): {self.options_list[self.person_choice - 1]}")
                print(f"COMPUTADOR: {self.machine_choice}")
                self.creates_simple_line()
                self.check_winner()
                control_variable = False

            else:
                print("VALOR INVÁLIDO!!! TENTE NOVAMENTE!!")
                self.creates_double_lines()


    def check_winner(self):
        if self.options_list[self.person_choice - 1] == self.machine_choice:
            print("EMPATE!!!")

        else:
                
            if self.options_list[self.person_choice - 1] == "PEDRA" and self.machine_choice == "TESOURA" or self.options_list[self.person_choice - 1] == "PAPEL" and self.machine_choice == "PEDRA" or self.options_list[self.person_choice - 1] == "TESOURA" and self.machine_choice == "PAPEL":

                print("VOCÊ VENCEU!!!")

            elif self.person_choice == 0:
                print("")
                
            else:
                print("VOCÊ PERDEU")

        if self.person_choice != 0:
            self.creates_double_lines()
            self.show_choices()


start_Game = Jokenpo()
start_Game.introduction()
start_Game.show_choices()
