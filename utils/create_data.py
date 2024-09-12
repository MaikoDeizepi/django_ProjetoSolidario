import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 100

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from projetoSolidario.models import Evento, Empresa, Usuario, Endereco

    # Limpar tabelas
    #Evento.objects.all().delete()
    #Empresa.objects.all().delete()
    #Usuario.objects.all().delete()
    #Endereco.objects.all().delete()

    fake = faker.Faker('pt_BR')

    # Criar eventos
    evento_tipos = ['C', 'R', 'P', 'E', 'O']
    django_eventos = []
    for _ in range(NUMBER_OF_OBJECTS):
        nome_organizador = fake.name()
        telefone = fake.phone_number()
        email = fake.email()
        data_evento = fake.date_time_this_year()
        tipo_evento = choice(evento_tipos)
        local_evento = fake.address()
        limite_evento = str(fake.random_int(min=50, max=500))

        django_eventos.append(
            Evento(
                nome_organizador=nome_organizador,
                telefone=telefone,
                email=email,
                data_evento=data_evento,
                tipo_evento=tipo_evento,
                local_evento=local_evento,
                limite_evento=limite_evento,
            )
        )

    if len(django_eventos) > 0:
        Evento.objects.bulk_create(django_eventos)

    # Criar empresas
    django_empresas = []
    for _ in range(NUMBER_OF_OBJECTS):
        razao_social = fake.company()
        nome_fantasia = fake.company_suffix()
        cnpj = fake.cnpj()
        telefone = fake.phone_number()
        email = fake.email()

        django_empresas.append(
            Empresa(
                razao_social=razao_social,
                nome_fantasia=nome_fantasia,
                cnpj=cnpj,
                telefone=telefone,
                email=email,
            )
        )

    if len(django_empresas) > 0:
        Empresa.objects.bulk_create(django_empresas)

    # Criar endereços
    django_enderecos = []
    for _ in range(NUMBER_OF_OBJECTS):
        rua = fake.street_name()
        numero = fake.building_number()
        bairro = fake.bairro()
        cidade = fake.city()
        estado = fake.state()
        pais = fake.country()

        django_enderecos.append(
            Endereco(
                rua=rua,
                numero=numero,
                bairro=bairro,
                cidade=cidade,
                estado=estado,
                pais=pais,
            )
        )

    if len(django_enderecos) > 0:
        Endereco.objects.bulk_create(django_enderecos)
        
# Criar usuários (sem a relação com Endereco)
    django_usuarios = []
    for _ in range(NUMBER_OF_OBJECTS):
        primeiro_nome = fake.first_name()
        ultimo_nome = fake.last_name()
        email = fake.email()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90)
        sexo = choice(['F', 'M', 'L', 'P'])
        telefone = fake.phone_number()
        

        django_usuarios.append(
            Usuario(
                primeiro_nome=primeiro_nome,
                ultimo_nome=ultimo_nome,
                email=email,
                data_nascimento=data_nascimento,
                sexo=sexo,
                telefone=telefone,
              
            )
        )

    if len(django_usuarios) > 0:
        Usuario.objects.bulk_create(django_usuarios)
