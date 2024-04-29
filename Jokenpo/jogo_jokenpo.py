
import time as t
import random as r

class Jokenpo:

    def __init__(self):
        self.cria_linha_dupla()
        print("JOKENPÔ - CONTRA O COMPUTADOR")
        self.cria_linha_dupla()
        self.escolha_maquina = ""
        self.escolha_pessoa = 0
        self.lista_opcoes = ["PEDRA", "PAPEL", "TESOURA"]


    def tempo_delay(self):
        print("COMPUTADOR PENSANDO...")
        lista_quantidade_pontos = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        quantidade_escolhida = r.choice(lista_quantidade_pontos)
        for _ in range(quantidade_escolhida):
            lista_segundos = [0.1, 0.2, 0.3, 0.4, 0.5]
            segundo_escolhido = r.choice(lista_segundos)
            t.sleep(segundo_escolhido)
            print(".")
            segundo_escolhido = r.choice(lista_segundos)
            t.sleep(segundo_escolhido)
        self.cria_linha_dupla()


    def cria_linha_dupla(self):
        print("=" * 60)


    def cria_linha_simples(self):
        print("-" * 60)


    def introducao(self):
        print("INSTRUCÕES DE COMO JOGAR:")
        self.cria_linha_simples()
        print("1--PEDRA")
        print("2--PAPEL")
        print("3--TESOURA")
        print("0--SAIR")
        self.cria_linha_simples()


    def valor_escolha_computador(self):
        self.escolha_maquina = r.choice(self.lista_opcoes)
        return self.escolha_maquina
    

    def valor_escolha_pessoa(self):
        self.escolha_pessoa = int(input("DIGITE O NÚMERO DA SUA ESCOLHA: "))
        self.cria_linha_simples()
        return self.escolha_pessoa
    

    def mostra_escolhas(self):
        variavel_controle = True

        
        while variavel_controle:
            self.escolha_pessoa = self.valor_escolha_pessoa()
            if self.escolha_pessoa == 0:
                print("FIM DE JOGO!!!")
                variavel_controle = False

            elif self.escolha_pessoa > 0 and self.escolha_pessoa < 4:
                self.tempo_delay()
                self.escolha_maquina = self.valor_escolha_computador()
                print(f"HUMANO(VOCÊ): {self.lista_opcoes[self.escolha_pessoa - 1]}")
                print(f"COMPUTADOR: {self.escolha_maquina}")
                self.cria_linha_simples()
                self.verifica_vencedor()
                variavel_controle = False

            else:
                print("VALOR INVÁLIDO!!! TENTE NOVAMENTE!!")
                self.cria_linha_dupla()


    def verifica_vencedor(self):
        if self.lista_opcoes[self.escolha_pessoa - 1] == self.escolha_maquina:
            print("EMPATE!!!")

        else:
                
            if self.lista_opcoes[self.escolha_pessoa - 1] == "PEDRA" and self.escolha_maquina == "TESOURA" or self.lista_opcoes[self.escolha_pessoa - 1] == "PAPEL" and self.escolha_maquina == "PEDRA" or self.lista_opcoes[self.escolha_pessoa - 1] == "TESOURA" and self.escolha_maquina == "PAPEL":

                print("VOCÊ VENCEU!!!")

            elif self.escolha_pessoa == 0:
                print("")
                
            else:
                print("VOCÊ PERDEU")

        if self.escolha_pessoa != 0:
            self.cria_linha_dupla()
            self.mostra_escolhas()


iniciar_jogo = Jokenpo()
iniciar_jogo.introducao()
iniciar_jogo.mostra_escolhas()
