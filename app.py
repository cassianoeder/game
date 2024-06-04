#DESAFIO DE CODIGO FINAL INSTITUTO MIX

#importar biblioteca random para poder sortear o jogador que vai iniciar
import random

#importei biblioteca os para poder limpar o terminal de tempos em tempos
import os

# Dicionário com todas as habilidades
habilidades = {
    "Golpe de Fogo": {"dano": 50, "custo": 15},
    "Lâmina de Gelo": {"dano": 55, "custo": 20},
    "Rajada Elétrica": {"dano": 60, "custo": 25},
    "Explosão Sombria": {"dano": 33, "custo": 14},
    "Pancada Terrestre": {"dano": 70, "custo": 33},
    "Chama Ardente": {"dano": 15, "custo": 1}
}

# Todas as defesas
defesas = {
    "Escudo de Fogo": {"reducao": 19, "custo": 5},
    "Barreira de Gelo": {"reducao": 15, "custo": 4},
    "Campo Elétrico": {"reducao": 10, "custo": 5},
    "Cúpula Sombria": {"reducao": 25, "custo": 7},
    "Fortaleza de Pedra": {"reducao": 5, "custo": 1},
    "Proteção de Aço": {"reducao": 10, "custo": 2}
}

def limpar_terminal():
    # Verifica se o sistema operacional é Windows
    if os.name == 'nt':
        # Comando para limpar o terminal no Windows
        os.system('cls')
    else:
        # Comando para limpar o terminal em sistemas Unix (Linux e macOS)
        os.system('clear')



class Jogador:
    def __init__(self, nome):
        self.nome = nome
        # Nível de energia padrão
        self.energia = 100

    # Função atacar recebe o parâmetro habilidade conforme jogador escolheu
    def ataque(self, habilidade):

        self.habilidade = habilidade
        # Com base no parâmetro de entrada da função busca e armazena a habilidade na variável
        habilidade_selecionada = habilidades.get(self.habilidade)

        # Se o get retornar True para a habilidade passada
        if habilidade_selecionada:
            # Busca dano e armazena na variável
            dano = habilidade_selecionada['dano']
            # Busca custo e armazena na variável
            custo = habilidade_selecionada['custo']
            print(f'    Ataque com {habilidade} efetuado por {self.nome}')

            self.energia -= custo
            return dano
        else:
            print(f'    A Habilidade {habilidade} não existe,\npróximo jogador')
            return 0

    # Função de defesa recebe o parâmetro de defesa
    def defender(self, defesa):

        # Com base no parâmetro de entrada da função busca e armazena a defesa
        self.defesa = defesa
        defesa_selecionada = defesas.get(self.defesa)

        if defesa_selecionada:
            # Armazena a redução do dano na variável
            reducao_dano_ataque = defesa_selecionada['reducao']
            # Busca custo e armazena na variável
            custo_da_defesa = defesa_selecionada['custo']

            self.energia -= custo_da_defesa

            return reducao_dano_ataque
        else:
            print(f'    A Defesa {defesa} não existe, \npróximo jogador')
            return 0
        
    #funcao usada para calcular dano recebido
    def dano_recebido(self, ataque_oponente, minha_defesa):
        self.ataque_oponente = ataque_oponente
        self.minha_defesa = defesas
        self.defesa = minha_defesa

        #dicionario de habilidades
        self.habilidade = habilidades

        #busca dano recebido pelo parametro da funcao
        dano = self.habilidade[self.ataque_oponente]['dano']
        defesa = self.minha_defesa[self.defesa]['reducao']

        #garantir que o dano nao seja negativo fazendo a energia aumentar
        reducao_energia = max(0, dano - defesa)

        self.energia -= reducao_energia

        print(f"\n    Dano causado pelo oponente de {reducao_energia} pontos!\n")


    # Função que mostra o nome e o nível de energia do jogador ao usar print na Classe
    def __str__(self):
        return f'{self.nome} com nível de energia em {self.energia}, portanto {"está quase morrendo!" if self.energia <= 60 else "está bem"}'


#menu de selecao ataques
def menu_ataque():
    ataque = int(input('''
            [1] "Golpe de Fogo"      
            [2] "Lâmina de Gelo"    
            [3] "Rajada Elétrica"    
            [4] "Explosão Sombria"   
            [5] "Pancada Terrestre"  
            [6] "Chama Ardente"     

            ESCOLHA SEU ATAQUE: '''))

    if ataque == 1:
        return "Golpe de Fogo"
    elif ataque == 2:
        return "Lâmina de Gelo"
    elif ataque == 3:
        return "Rajada Elétrica"
    elif ataque == 4:
        return "Explosão Sombria"
    elif ataque == 5:
        return "Pancada Terrestre"
    elif ataque == 6:
        return "Chama Ardente"
    else:
        return None

 

#menu de selecao defesas
def menu_defesa():
    defesa = int(input('''
            [1] "Escudo de Fogo"      
            [2] "Barreira de Gelo"     
            [3] "Campo Elétrico"       
            [4] "Cúpula Sombria"       
            [5] "Fortaleza de Pedra"   
            [6] "Proteção de Aço"     

            ESCOLHA SUA DEFESA: '''))

    if defesa == 1:
        return "Escudo de Fogo"
    elif defesa == 2:
        return "Barreira de Gelo"
    elif defesa == 3:
        return "Campo Elétrico"
    elif defesa == 4:
        return "Cúpula Sombria"
    elif defesa == 5:
        return "Fortaleza de Pedra"
    elif defesa == 6:
        return "Proteção de Aço"
    else:
        return None



# Função principal do jogo
def jogar():
 
    jogador1 = Jogador(input("Nome do Jogador 1: ").title())
    jogador2 = Jogador(input("Nome do Jogador 2: ").title())


    def mostrar_energia_jogadores():
        print(f"    {jogador1.nome} com nível de energia em: {jogador1.energia if jogador1.energia > 0 else '0'}")
        print(f"    {jogador2.nome} com nível de energia em: {jogador2.energia if jogador2.energia > 0 else '0'}\n")
        return None

    sortear_jogador = ['jogador1', 'jogador2', 'jogador2', 'jogador1']
    #sorteio do jogador que inicia
    sorteado = random.choice(sortear_jogador)
    #mostra qual o jogador que inicia e seu respectivo nome

    print("O JOGO TERMINA APÓS UM JOGADOR ATINGIR 0 PONTOS\n\nOBSERVAÇÕES:\nO ATAQUE COM MAIOR DANO CONSOME MAIS ENERGIA \n"
          "A DEFESA COM MAIOR REDUÇÃO DE DANOS CONSOME MAIS ENERGIA\nESPERO QUE ESTEJA COM SORTE\n")
    print(f"OS DOIS PARTICIPANTES INICIAM COM {jogador1.energia} PONTOS")
    print(f"    O jogo iniciará pelo {jogador1.nome.title() if sorteado == 'jogador1' else jogador2.nome.title()} Boa Sorte!")

    #padrao 0
    turno = 0
    #variavel que implementara o jogador ativo
    jogador_ativo = sorteado

    #looping while se mantem rodando enquanto os jogadores tiverem pontos
    while jogador1.energia > 0 and jogador2.energia > 0:

        #contador de turnos aumenta a cada rodada
        turno += 1
        print(f"    Turno {turno}\n")

        #se a variavel jog ativo = jogador1 passa para a jogada
        if jogador_ativo == 'jogador1':
            #ataque jog 1
            print(f"    BÓRA ATACAR SEM DÓ {jogador1.nome.upper()}")
            ataq = menu_ataque()

            #chama a funcao que limpa o terminal
            limpar_terminal()

            jogador1.ataque(ataq)
            print(f"    Nível de energia de {jogador1.nome} caiu para {jogador1.energia if jogador1.energia > 0 else '0'} pelo esforço do ataque!\n")
            

            #defesa jog2
            print(f"    Hora de se defender {jogador2.nome}")
            defesa = menu_defesa()

            limpar_terminal()

            jogador2.defender(defesa)

            #passa o ataque e a defesa para calcular o prejuizo de energia
            jogador2.dano_recebido(ataq, defesa)

            mostrar_energia_jogadores()

        #senao passa para jogador2
        else:
            #ataque jog2
            print(f"    BÓRA ATACAR SEM DÓ {jogador2.nome.upper()}")
            ataq = menu_ataque()

            #chama a funcao que limpa o terminal
            limpar_terminal()

            jogador2.ataque(ataq)
            print(f"    Nível de energia de {jogador2.nome} caiu para {jogador2.energia if jogador2.energia > 0 else '0'} devido o esforço do ataque!\n")


            #defesa jog1
            print(f"    Hora de se defender {jogador1.nome}")
            defesa = menu_defesa()

            limpar_terminal()

            jogador1.defender(defesa)

            #passa o ataque e a defesa para calcular o prejuizo de energia
            jogador1.dano_recebido(ataq, defesa)

            mostrar_energia_jogadores()

        ##################################################################################
        #apos a jogada verifica o jogador ativo e inverte para o proximo e refaz o looping
        if jogador_ativo == 'jogador1':
            jogador_ativo = 'jogador2'
        
        else:
            jogador_ativo = 'jogador1'
        #Fim do trecho responsavel por inverter a jogada
        ####################################################################################


        #VERIFICA QUAL JOGADOR TEM A MENOR PONTUACAO
        if jogador1.energia < 1 and jogador2.energia > 1:
            print(f"O VENCEDOR É O {jogador2.nome.upper()}\nMEUS PARABÉNS!")
            break
            

        elif jogador2.energia < 1 and jogador1.energia > 1:
            print(f"O VENCEDOR É O {jogador1.nome.upper()}\nMEUS PARABÉNS!")
            break
        

        elif jogador2.energia and jogador1.energia < 1:
            print(f"Ocorreu um empate entre {jogador1.nome} e {jogador2.nome}!")
            break

        else:
            #jogo continua
            pass

        #volta para o inicio do looping While


        

if __name__ == "__main__":
    jogar()
