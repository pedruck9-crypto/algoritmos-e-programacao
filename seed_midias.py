from db import init_db, create_midia


def seed():
    init_db()
    midias = [
        {"titulo": "Duna", "tipo": "filme", "genero": "ficção científica", "ano": 2021, "sinopse": "Um jovem herdeiro luta pelo controle do planeta Arrakis."},
        {"titulo": "Stranger Things", "tipo": "série", "genero": "suspense", "ano": 2016, "sinopse": "Adolescentes enfrentam forças sobrenaturais em Hawkins."},
        {"titulo": "The Witcher", "tipo": "série", "genero": "fantasia", "ano": 2019, "sinopse": "Um caçador de monstros percorre um mundo de caos e magia."},
        {"titulo": "A Origem", "tipo": "filme", "genero": "ação", "ano": 2010, "sinopse": "Um ladrão de sonhos tenta realizar um último trabalho impossível."},
        {"titulo": "Breaking Bad", "tipo": "série", "genero": "drama", "ano": 2008, "sinopse": "Um professor de química vira fabricante de metanfetamina."},
    ]

    inserted = 0
    for m in midias:
        create_midia(m)
        inserted += 1

    print(f"{inserted} mídias fictícias inseridas com sucesso.")


if __name__ == "__main__":
    seed()
