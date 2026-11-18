import json


ARQUIVO_DADOS = "midias.json"
midias = []
proximo_id = 1


def salvar_midias():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(midias, arquivo, ensure_ascii=False, indent=4)


def carregar_midias():
    global midias, proximo_id
    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            midias = json.load(arquivo)
    except FileNotFoundError:
        midias = []

    if midias:
        proximo_id = max(midia["id"] for midia in midias) + 1
    else:
        proximo_id = 1


def cadastrar_midia():
    global proximo_id
    titulo = input("Título: ").strip()
    if titulo == "":
        print("O título não pode ficar vazio.")
        return
    midia = {
        "id": proximo_id,
        "titulo": titulo,
        "tipo": input("Tipo (filme/série): ").strip(),
        "genero": input("Gênero: ").strip(),
        "ano": input("Ano: ").strip(),
        "sinopse": input("Sinopse: ").strip(),
    }
    midias.append(midia)
    salvar_midias()
    print("Mídia cadastrada com identificador", proximo_id)
    proximo_id += 1


def listar_midias():
    if not midias:
        print("Nenhuma mídia cadastrada.")
        return
    for midia in midias:
        print("\nID: {}".format(midia["id"]))
        print("Título: {}".format(midia["titulo"]))
        print("Tipo: {}".format(midia["tipo"]))
        print("Gênero: {}".format(midia["genero"]))
        print("Ano: {}".format(midia["ano"]))
        print("Sinopse: {}".format(midia["sinopse"]))


def buscar_midia(identificador):
    for midia in midias:
        if midia["id"] == identificador:
            return midia
    return None


def atualizar_midia():
    identificador = input("Identificador da mídia: ").strip()
    if not identificador.isdigit():
        print("Informe um identificador numérico.")
        return
    midia = buscar_midia(int(identificador))
    if midia is None:
        print("Mídia não encontrada.")
        return
    campos = ["titulo", "tipo", "genero", "ano", "sinopse"]
    rotulos = ["Novo título", "Novo tipo", "Novo gênero", "Novo ano", "Nova sinopse"]
    indice = 0
    while indice < len(campos):
        novo_valor = input(rotulos[indice] + " (Enter mantém o atual): ").strip()
        if novo_valor != "":
            midia[campos[indice]] = novo_valor
        indice += 1
    salvar_midias()
    print("Mídia atualizada.")


def excluir_midia():
    identificador = input("Identificador da mídia: ").strip()
    if not identificador.isdigit():
        print("Informe um identificador numérico.")
        return
    midia = buscar_midia(int(identificador))
    if midia is None:
        print("Mídia não encontrada.")
        return
    midias.remove(midia)
    salvar_midias()
    print("Mídia excluída.")


def executar_menu():
    carregar_midias()
    while True:
        print("\n=== CRUD de Filmes e Séries — Ciclo 3.1 ===")
        print("1 - Cadastrar mídia")
        print("2 - Listar mídias")
        print("3 - Buscar mídia")
        print("4 - Atualizar mídia")
        print("5 - Excluir mídia")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_midia()
        elif opcao == "2":
            listar_midias()
        elif opcao == "3":
            identificador = input("Identificador: ").strip()
            if identificador.isdigit():
                midia = buscar_midia(int(identificador))
                if midia is None:
                    print("Mídia não encontrada.")
                else:
                    print(midia)
            else:
                print("Informe um identificador numérico.")
        elif opcao == "4":
            atualizar_midia()
        elif opcao == "5":
            excluir_midia()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    executar_menu()
