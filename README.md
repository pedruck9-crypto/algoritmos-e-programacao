# Ciclo 3.1 — Aplicação em funções com dados salvos em JSON

Esta versão continua a aplicação do Ciclo 3, organizada em funções, e acrescenta persistência local por meio da biblioteca padrão `json` do Python.

## Funcionalidades

- Menu interativo no terminal.
- Cadastrar, listar, buscar, atualizar e excluir mídias.
- Identificadores sequenciais.
- Salvamento automático no arquivo `midias.json`.
- Carregamento dos dados ao iniciar o programa.
- Funções separadas para as operações e para o fluxo principal do menu.

## Conceitos praticados

Variáveis, operadores, condicionais, laços, listas, dicionários, parâmetros, retorno de valores, decomposição em funções e persistência de dados com JSON.

## Tecnologias

Python e terminal, utilizando apenas recursos da biblioteca padrão. Não há API web, interface gráfica ou banco de dados.

## Arquivo de dados

Os registros são armazenados em:

    midias.json

O arquivo é criado automaticamente na primeira operação de cadastro, atualização ou exclusão. Ele pode ser lido por qualquer aplicação compatível com JSON.

## Como o JSON é usado

- `json.dump()` escreve a lista de mídias no arquivo `midias.json`.
- `json.load()` lê o arquivo e recupera os dicionários ao iniciar o programa.
- `ensure_ascii=False` mantém corretamente caracteres acentuados.
- `indent=4` deixa o arquivo mais legível.

## Executar

Na raiz do repositório:

    python crud_filmes_e_series.py

Os dados permanecem disponíveis entre uma execução e outra por meio do arquivo `midias.json`.
