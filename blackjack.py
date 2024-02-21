import random

class Deck:
    def __init__(self):
        self.cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(self.cartas)
        
    def dar_carta(self):
        return self.cartas.pop()
    
class Mao:
    def __init__(self):
        self.cartas = []
    
    def adicionar_carta(self, carta):
        self.cartas.append(carta)
    
    def pontuacao(self):
        pontuacao = 0
        num_as = 0
        for carta in self.cartas:
            if carta.isdigit():
                pontuacao += int(carta)
            elif carta in ['J', 'Q', 'K']:
                pontuacao += 10
            elif carta == 'A':
                num_as += 1
                pontuacao += 11
        while pontuacao > 21 and num_as:
            pontuacao -= 10
            num_as -= 1
        return pontuacao
    
    
def play_blackjack():
    deck = Deck()
    Mao_jogador = Mao()
    Mao_outro = Mao()
    
    Mao_jogador.adicionar_carta(deck.dar_carta())
    Mao_outro.adicionar_carta(deck.dar_carta())
    Mao_jogador.adicionar_carta(deck.dar_carta())
    Mao_outro.adicionar_carta(deck.dar_carta())
    
    print("Sua mão:",  Mao_jogador.cartas)
    print("Carta do dealer:", Mao_outro.cartas[0])
    
    while Mao_jogador.pontuacao() < 21:
        acao = input("Deseja bater (hit) ou parar (stand)? ").lower()
        if acao == 'hit' or acao == 'bater':
            Mao_jogador.adicionar_carta(deck.dar_carta())
            print("Sua mão:", Mao_jogador.cartas)
        elif acao == 'stand' or acao == 'parar':
            break
    
    pontuacao_jogador = Mao_jogador.pontuacao()
    if pontuacao_jogador> 21:
        print("Você estourou! Pontuação:", pontuacao_jogador)
        return
    
    while Mao_outro.pontuacao() < 17:
        Mao_outro.adicionar_carta(deck.dar_carta())
    
    Pontuacao_outro = Mao_outro.pontuacao()
    print("Mão do dealer:", Mao_outro.cartas, "Pontuação:", Pontuacao_outro)
    
    if Pontuacao_outro > 21 or pontuacao_jogador > Pontuacao_outro:
        print("Você ganhou!")
    elif Pontuacao_outro > pontuacao_jogador:
        print("Dealer ganhou!")
    else:
        print("Empate!")

play_blackjack()