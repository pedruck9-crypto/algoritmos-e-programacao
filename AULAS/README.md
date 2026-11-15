# Exercícios de Algoritmos e Programação

Esta pasta reúne exercícios e exemplos dos conteúdos estudados na disciplina de **Algoritmos e Programação**, ministrada por **Rondineli Seba Salomão**, na UNDB.

Os exemplos são independentes do CRUD de filmes e séries. Eles registram a prática dos conceitos da matéria; a aplicação de portfólio e as versões didáticas por ciclo estão apresentadas no [README principal](../README.md).

## Conteúdo

| Arquivo | Assuntos estudados |
|---|---|
| [exemplos_listas.py](exemplos_listas.py) | Listas com ingredientes de um sanduíche: índices, pertinência (`in`), `index`, `count`, `len`, fatias, compreensão de listas, cópia, `append`, `pop`, `remove`, `reverse`, ordenação e `enumerate`. Inclui operações numéricas com `sum`, `min` e `max`. |
| [lista_jogos.py](lista_jogos.py) | Exercício do laboratório sobre listas, índices com `enumerate()`, fatiamento e inclusão com `append()`. |

O exercício de listas se relaciona às estruturas dinâmicas estudadas no ciclo 2. Os conteúdos desta pasta não substituem os requisitos específicos de cada ciclo.

## Como executar

Com Python instalado, abra o terminal na raiz do repositório e execute:

```text
python AULAS/exemplos_listas.py
```

O exercício usa apenas recursos da biblioteca padrão do Python e imprime os exemplos no terminal. Não precisa iniciar a API nem instalar as dependências do CRUD.

Novos exercícios podem ser adicionados com nomes descritivos e uma linha nesta tabela explicando o assunto estudado.

## Lista de jogos no laboratório

Este exercício serve como evidência para o **Ciclo 07 do Logbook**, sobre listas, armazenamento e iteração. O laço usa `enumerate()` para obter o índice e o nome de cada jogo. O comando `print(indice, jogo)` exibe os dois valores na mesma linha. A fatia `[1:4:1]` inclui os índices 1, 2 e 3, pois o limite final é exclusivo. Depois de adicionar Minecraft com `append()`, a fatia `[-2:]` mostra os dois últimos itens.

Execute na raiz do repositório:

```text
python AULAS/lista_jogos.py
```

### Código do exercício

```python
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
```

### Saída no terminal

```text
0 gta5
1 nedforspeed
2 24
3 30
4 fifa24
5 tetris
['nedforspeed', '24', '30']
['tetris', 'minecraft']
```
