# Exercícios de Algoritmos e Programação

Esta pasta reúne exercícios e exemplos dos conteúdos estudados na disciplina de **Algoritmos e Programação**, ministrada por **Rondineli Seba Salomão**, na UNDB.

Os exemplos são independentes do CRUD de filmes e séries. Eles registram a prática dos conceitos da matéria; a aplicação de portfólio e as versões didáticas por ciclo estão apresentadas no [README principal](../README.md).

## Conteúdo

| Arquivo | Assuntos estudados |
|---|---|
| [exemplos_listas.py](exemplos_listas.py) | Listas com ingredientes de um sanduíche: índices, pertinência (`in`), `index`, `count`, `len`, fatias, compreensão de listas, cópia, `append`, `pop`, `remove`, `reverse`, ordenação e `enumerate`. Inclui operações numéricas com `sum`, `min` e `max`. |
| [lista_jogos.py](lista_jogos.py) | Exercício do laboratório sobre listas, índices com `enumerate()`, fatiamento e inclusão com `append()`. |
| [fatorial_recursivo.py](fatorial_recursivo.py) | Fatorial com recursividade e com `while`: caso base, chamadas com `n - 1`, retorno e comparação dos resultados. |

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

## Fatorial: recursividade e laço

Exercício complementar de estudo sobre o **Ciclo 11 do Logbook**, acrescentado em **22/11/2026** com apoio de IA (Codex). Esta data corresponde ao registro do exercício, posterior à aula de 04/11.

O fatorial multiplica os inteiros de 1 até o número escolhido. Por exemplo, `4! = 4 × 3 × 2 × 1 = 24`; por definição, `0! = 1`.

Na função recursiva, o **caso base** `n == 0` retorna `1` e encerra as chamadas. Nos demais casos, a função chama a si mesma com `n - 1`. Quando o caso base é alcançado, os retornos completam as multiplicações. Para `3`, o cálculo equivale a `3 × 2 × 1 × 1 = 6`.

A segunda função resolve o mesmo problema com `while`, acumulando o produto em `resultado`. O programa compara as duas soluções para 0, 1, 4 e 5. Os exemplos pressupõem inteiros não negativos pequenos: não há validação para outros tipos ou números negativos, e a versão recursiva está sujeita ao limite de recursão do Python.

Execute na raiz do repositório, sem instalar dependências:

```text
python AULAS/fatorial_recursivo.py
```

### Código do exercício

```python
# Exercício complementar: comparação entre recursividade e repetição.
# Use números inteiros não negativos pequenos, como os exemplos abaixo.
def fatorial_recursivo(n):
    # Caso base: interrompe as chamadas recursivas.
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)


def fatorial_com_laco(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado


for numero in [0, 1, 4, 5]:
    print(
        numero,
        fatorial_recursivo(numero),
        fatorial_com_laco(numero)
    )
```

### Saída no terminal

Cada linha apresenta o número, o resultado recursivo e o resultado com laço, nessa ordem.

```text
0 1 1
1 1 1
4 24 24
5 120 120
```

Para praticar, inclua o número `3` na lista e confira se as duas funções retornam `6`.
