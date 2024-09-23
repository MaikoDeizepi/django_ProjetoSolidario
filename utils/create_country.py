import pycountry
from projetoSolidario.models import Pais, Estado


def preencher_paises_estados():
    for country in pycountry.countries:
        pais, created = Pais.objects.get_or_create(nome=country.name)
        if created:
            print(f"Criado país: {pais}")

        try:
            subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)
            for subdivision in subdivisions:
                # Verifica se a subdivisão tem sigla
                if "-" in subdivision.code:
                    sigla = subdivision.code.split("-")[-1]
                else:
                    sigla = ""

                # Criar estado relacionado ao país
                estado, created = Estado.objects.get_or_create(
                    nome=subdivision.name,
                    sigla=sigla,
                    pais=pais,  # Utilizando o campo pais agora
                )
                if created:
                    print(f"Criado estado: {estado} para o país: {pais}")
        except (AttributeError, KeyError):
            print(f"Sem subdivisões encontradas para o país: {country.name}")
