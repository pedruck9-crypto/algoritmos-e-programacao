# Lista de jogos usada no exercício do laboratório.
lista_jogos = ["gta5", "nedforspeed", "24", "30", "fifa24", "tetris"]

# Mostra o índice e o nome de cada jogo.
for indice, jogo in enumerate(lista_jogos):
    print(indice, jogo)

# Seleciona os itens dos índices 1, 2 e 3.
corte = lista_jogos[1:4:1]
print(corte)

# Adiciona um jogo e mostra os dois últimos itens da lista.
lista_jogos.append("minecraft")
print(lista_jogos[-2:])
