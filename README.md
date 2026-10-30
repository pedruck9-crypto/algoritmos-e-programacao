# CRUD de Filmes e Séries — evolução com IA e autenticação

**Status desta branch: planejamento de funcionalidades futuras.**

A branch `Crud_com_imagens_geradas_por_ia_e_autenticacao` parte do CRUD de portfólio e reúne o plano para adicionar contas de usuários, permissões, PostgreSQL, armazenamento persistente de imagens e geração opcional de capas com IA.

Este README documenta a proposta. Autenticação, integração com IA, fila de tarefas e PostgreSQL ainda não estão implementados. Os esboços em Python abaixo são ilustrativos e dependem de serviços e funções que precisam ser desenvolvidos.

Projeto de estudo de **Pedro Lucas Pereira Rolim**, estudante de Sistemas de Informação na UNDB, desenvolvido a partir da disciplina de **Algoritmos e Programação**, ministrada por **Rondineli Seba Salomão**. Esta evolução amplia o escopo acadêmico original.

## Navegação

- [Versão principal](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/main).
- [Branch de portfólio](https://github.com/pedruck9-crypto/algoritmos-e-programacao/tree/Crud_portf%C3%B3lio).
- [Documentação do CRUD atual](docs/DOCUMENTACAO-PORTFOLIO.md): instalação, execução, API, testes e Docker.
- [Exercícios das aulas](AULAS/README.md).

## O que já existe na base desta branch

- API FastAPI para criar, listar, consultar, atualizar e excluir mídias.
- Filtros e paginação na API.
- Interface HTML, CSS e JavaScript.
- SQLite com SQLModel.
- Capas SVG geradas por código, com alternativa para imagens ausentes ou quebradas.
- Cadastro automático de “Vingadores: Ultimato”, com o pôster configurado.
- Geração de credenciais demonstrativas com senha armazenada como hash.
- Testes automatizados e configuração Docker.

As credenciais demonstrativas existentes não autenticam visitantes nem protegem as rotas. O modelo atual chamado `Usuario` representa esses registros demonstrativos; ele precisará ser separado das futuras contas reais ou migrado explicitamente.

## Funcionalidades futuras

| Funcionalidade | Resultado esperado | Situação |
|---|---|---|
| PostgreSQL | Persistir contas, mídias e tarefas em banco durável. | Planejada |
| Cadastro e login | Identificar o usuário e iniciar uma sessão. | Planejada |
| Autorização | Permitir que cada pessoa altere apenas seu catálogo e suas tarefas. | Planejada |
| Sessão e logout | Expirar acessos e encerrar sessões de forma controlada. | Planejada |
| Armazenamento de imagens | Guardar as capas geradas fora do disco temporário da Vercel. | Planejada |
| Botão “Criar capa com IA” | Solicitar uma ilustração a partir de título, gênero e sinopse. | Planejada |
| Fila de geração | Processar imagens sem depender da duração de uma requisição web. | Planejada |
| Acompanhamento e recuperação | Mostrar progresso, falhas e opção de tentar novamente. | Planejada |
| Limites de geração | Controlar uso simultâneo, repetição de cliques e orçamento. | Planejada |
| Chaves individuais de API | Permitir que cada usuário configure a própria chave, em uma etapa posterior. | Planejada |

## Fluxo de uma capa com IA

1. O usuário autenticado abre uma mídia do próprio catálogo.
2. Clica em **“Criar capa com IA”**.
3. O servidor verifica a sessão, a propriedade da mídia, a disponibilidade do serviço e a cota de geração.
4. Uma tarefa é registrada no PostgreSQL e encaminhada para uma fila persistente.
5. Um processo de geração monta a descrição e chama o provedor de IA.
6. A imagem é salva em armazenamento persistente de arquivos.
7. O banco recebe a referência da imagem e a tarefa é marcada como concluída.
8. A interface consulta o andamento, mostra uma prévia e permite aplicar a nova capa.

Enquanto a tarefa estiver em andamento ou falhar, a capa atual continua disponível. O servidor deve evitar solicitações duplicadas e impedir que uma tarefa antiga sobrescreva uma capa escolhida mais recentemente.

Para obter texto legível e manter a identidade visual do catálogo, a proposta inicial é pedir uma ilustração sem letras e desenhar título e informações da mídia por código.

Exemplo de descrição:

> Ilustração cinematográfica de ficção científica para “Ecos do Tempo”: um viajante diante de um portal espacial com fragmentos de diferentes épocas, tons azuis e roxos, composição horizontal e espaço livre para o título. Não incluir letras nem logotipos.

## Serviço de IA e uso de chaves

O primeiro provedor proposto é a API de imagens da OpenAI. O modelo, qualidade, dimensões, custos e disponibilidade deverão ser conferidos na documentação oficial no momento da implementação.

Na primeira etapa, a geração pode ficar restrita a um administrador, usando uma chave configurada no servidor e um orçamento controlado. A geração pública só deve ser liberada após implementar autenticação, autorização e limites.

Em uma etapa posterior, cada usuário poderá cadastrar a própria chave. Nesse caso:

- A chave deve ser transmitida ao servidor por HTTPS e nunca incluída no código público, em URLs ou em logs.
- Caso seja armazenada, deve ser criptografada com uma chave de proteção mantida fora do banco ou guardada em um serviço de segredos.
- Senhas de login recebem hash; chaves de API exigem armazenamento recuperável protegido, pois serão usadas para chamar o provedor.
- A interface deve mostrar somente uma identificação mascarada e permitir substituir ou remover a chave.
- A fila deve receber apenas a referência da credencial; o processo de geração recupera o segredo no momento necessário.
- A cobrança da geração ocorre na conta do provedor associada à chave utilizada. Isso precisa ser explicado antes da solicitação.

Não salvar a chave em `localStorage`, no `index.html` ou em texto puro no PostgreSQL.

## Esboço em Python: solicitar e acompanhar geração

**Exemplo conceitual, não executável como está.** Funções de autenticação, acesso ao banco e fila ainda precisam ser implementadas. Este bloco não deve substituir a API atual antes de existir essa infraestrutura.

```python
from fastapi import Depends, FastAPI

app = FastAPI()


@app.post("/midias/{midia_id}/capa-ia", status_code=202)
def solicitar_capa(
    midia_id: int,
    usuario=Depends(obter_usuario_autenticado),
):
    # Consultar pelo ID e pelo proprietário evita acesso ao catálogo de terceiros.
    midia = buscar_midia_do_usuario(midia_id, usuario.id)
    verificar_permissao_para_ia(usuario)
    verificar_cota_e_tarefa_em_andamento(usuario.id, midia.id)

    # Registrar a tarefa e reservar a cota de forma consistente no servidor.
    tarefa = registrar_e_enfileirar_geracao(
        midia_id=midia.id,
        usuario_id=usuario.id,
    )
    return {"tarefa_id": tarefa.id, "status": "aguardando"}


@app.get("/tarefas/{tarefa_id}")
def consultar_tarefa(
    tarefa_id: str,
    usuario=Depends(obter_usuario_autenticado),
):
    tarefa = buscar_tarefa_do_usuario(tarefa_id, usuario.id)
    return {
        "status": tarefa.status,
        "imagem_url": tarefa.imagem_url,
        "mensagem": tarefa.mensagem_publica,
    }
```

A identificação do usuário deve vir da sessão validada pelo servidor, nunca de um `usuario_id` enviado livremente pelo navegador. Além dessa rota de IA, as rotas existentes de criação, atualização e exclusão também precisarão verificar o proprietário.

## Esboço em Python: processo de geração

**Pseudocódigo de um worker separado da requisição web.** A fila deve ser durável; iniciar uma tarefa somente na memória da função web não garante que ela termine na Vercel.

```python
def processar_geracao(tarefa_id: str):
    tarefa = carregar_e_reservar_tarefa(tarefa_id)

    try:
        midia = buscar_midia_do_usuario(
            tarefa.midia_id, tarefa.usuario_id
        )
        marcar_tarefa(tarefa.id, "gerando")
        descricao = montar_descricao_da_capa(midia)

        # A chave é obtida no servidor; ela não vai no conteúdo da fila.
        chave = obter_chave_protegida_para_geracao(tarefa.usuario_id)
        imagem = gerar_imagem_no_provedor(
            chave_api=chave,
            descricao=descricao,
        )

        referencia = salvar_imagem_em_armazenamento_persistente(imagem)
        salvar_resultado_para_aprovacao(tarefa.id, referencia)
        marcar_tarefa(tarefa.id, "concluida")
    except ErroDeGeracao:
        registrar_falha_sem_segredos(tarefa.id)
        marcar_tarefa(tarefa.id, "falhou")
```

Será necessário definir timeout, tentativas limitadas, recuperação de tarefas interrompidas e destino de arquivos gerados que não forem aplicados. Erros exibidos ao visitante não devem revelar chaves nem detalhes internos do provedor.

## PostgreSQL e estrutura dos dados

PostgreSQL é o banco persistente proposto. A configuração atual ainda usa SQLite e `DB_PATH`; apenas criar uma variável `DATABASE_URL` não muda o funcionamento do código existente.

A migração precisará adaptar a criação do engine SQLModel, instalar o driver escolhido para PostgreSQL, configurar conexões para o ambiente de implantação e criar migrações de esquema versionadas, por exemplo com Alembic.

| Entidade planejada | Dados principais |
|---|---|
| Conta | ID, identificação de login única, hash da senha e datas. |
| Mídia | Campos atuais, ID do proprietário e referência da capa aplicada. |
| Tarefa de geração | ID, proprietário, mídia, estado, datas, tentativas e referência do resultado. |
| Credencial do provedor | Proprietário, provedor e segredo protegido ou referência ao serviço de segredos. |

Antes de migrar, planejar como tratar as tabelas existentes e copiar os dados que precisarem ser preservados. Os registros de credenciais demonstrativas não devem virar contas autenticáveis automaticamente.

PostgreSQL guarda os registros e referências; os arquivos das imagens ficam em armazenamento persistente próprio para arquivos. Salvar imagens apenas em `/tmp` não garante sua conservação.

## Autenticação e autorização

- Criar cadastro e login com validação no servidor.
- Armazenar apenas o hash das senhas de contas, com biblioteca apropriada para senhas.
- Escolher sessões ou tokens; para uma sessão em cookie, configurar `HttpOnly`, `Secure`, `SameSite` e proteção contra CSRF conforme o fluxo adotado.
- Implementar expiração, logout e tratamento de tentativas excessivas de login.
- Garantir autorização em todas as operações de mídia, chave e tarefa.
- Adicionar recuperação de conta e confirmação de contato antes de ampliar o uso público, se fizerem parte dos requisitos.

Esconder um botão na interface não substitui a autorização da rota no servidor.

## Configuração futura do ambiente

Exemplo de nomes de variáveis para um futuro `.env.example`. Os valores abaixo são apenas ilustrativos; a aplicação atual não lê todas essas configurações.

```dotenv
DATABASE_URL=postgresql+psycopg://usuario:senha@localhost:5432/catalogo
AUTH_SECRET=
OPENAI_API_KEY=
IMAGE_MODEL=
IMAGE_STORAGE_BUCKET=
QUEUE_URL=
```

O prefixo `postgresql+psycopg` pressupõe a escolha e instalação do driver `psycopg`. A integração real deve carregar as configurações no servidor e validar variáveis obrigatórias.

O arquivo `.env` local já é ignorado pelo Git. Somente um modelo sem segredos deve ser versionado. Na Vercel, configurar os segredos nas variáveis de ambiente e separar as configurações de desenvolvimento, preview e produção. Contas, planos pagos e serviços externos devem ser configurados deliberadamente antes de habilitar gerações reais.

## Ordem sugerida de implementação

1. Preparar PostgreSQL, conexão e migrações; conferir a preservação dos dados necessários.
2. Criar contas, sessão e autorização por proprietário.
3. Configurar armazenamento persistente de imagens.
4. Implementar fila, estados das tarefas e acompanhamento na interface.
5. Integrar o provedor de IA em ambiente de desenvolvimento, inicialmente para administrador.
6. Adicionar orçamento, cotas, prevenção de cliques duplicados e tratamento de falhas.
7. Exibir o botão por mídia, prévia e aplicação da nova capa, mantendo o SVG alternativo.
8. Avaliar chaves individuais, proteção dos segredos e exclusão das credenciais.
9. Validar a versão em preview antes de propor integração à `main`.

## Critérios para considerar a versão pronta

- Um visitante sem login não consegue solicitar gerações pagas.
- Um usuário não acessa nem modifica mídias, tarefas ou chaves de outra conta.
- Cliques repetidos não disparam cobranças duplicadas para a mesma solicitação.
- Falhas e timeouts mantêm a capa existente e permitem recuperação controlada.
- Dados e imagens continuam disponíveis após reiniciar ou implantar a aplicação.
- Não há segredos no repositório, nos logs ou nas respostas da API.
- O CRUD e a regra de “Vingadores: Ultimato” continuam funcionando.
- Testes cobrem autenticação, autorização, persistência e o fluxo de geração com provedor simulado; chamadas pagas ficam separadas dos testes automáticos comuns.
- A documentação informa custos, limitações e quais funcionalidades estão efetivamente disponíveis.

## Referências para a implementação

- [API de geração de imagens da OpenAI](https://developers.openai.com/api/docs/guides/image-generation).
- [Segurança no FastAPI](https://fastapi.tiangolo.com/tutorial/security/).
- [Documentação do SQLModel](https://sqlmodel.tiangolo.com/).
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/).
- [Documentação do Alembic](https://alembic.sqlalchemy.org/en/latest/).

O desenvolvimento pode avançar em entregas pequenas. O README deve ser atualizado à medida que cada recurso sair do planejamento e passar a funcionar.
