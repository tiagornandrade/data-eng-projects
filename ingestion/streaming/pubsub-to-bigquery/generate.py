import random
from uuid import uuid4
from faker import Faker
from datetime import date, datetime, timedelta


fake = Faker("pt_BR")

initial_date = datetime.now() - timedelta(days=15)
final_date = datetime.now() - timedelta(days=1)
event_timestamp_date = fake.date_time_between_dates(datetime.now()) - timedelta(days=1)

location = [
    {"contact_country": "Acre", "contact_city": "Rio Branco"},
    {"contact_country": "Alagoas", "contact_city": "Maceió"},
    {"contact_country": "Amapá", "contact_city": "Macapá"},
    {"contact_country": "Amazonas", "contact_city": "Manaus"},
    {"contact_country": "Bahia", "contact_city": "Salvador"},
    {"contact_country": "Ceará", "contact_city": "Fortaleza"},
    {"contact_country": "Distrito Federal", "contact_city": "Brasília"},
    {"contact_country": "Espírito Santo", "contact_city": "Vitória"},
    {"contact_country": "Goiás", "contact_city": "Goiânia"},
    {"contact_country": "Maranhão", "contact_city": "São Luís"},
    {"contact_country": "Mato Grosso", "contact_city": "Cuiabá"},
    {"contact_country": "Mato Grosso do Sul", "contact_city": "Campo Grande"},
    {"contact_country": "Minas Gerais", "contact_city": "Belo Horizonte"},
    {"contact_country": "Pará", "contact_city": "Belém"},
    {"contact_country": "Paraíba", "contact_city": "João Pessoa"},
    {"contact_country": "Paraná", "contact_city": "Curitiba"},
    {"contact_country": "Pernambuco", "contact_city": "Recife"},
    {"contact_country": "Piauí", "contact_city": "Teresina"},
    {"contact_country": "Rio de Janeiro", "contact_city": "Rio de Janeiro"},
    {"contact_country": "Rio Grande do Norte", "contact_city": "Natal"},
    {"contact_country": "Rio Grande do Sul", "contact_city": "Porto Alegre"},
    {"contact_country": "Rondônia", "contact_city": "Porto Velho"},
    {"contact_country": "Roraima", "contact_city": "Boa Vista"},
    {"contact_country": "Santa Catarina", "contact_city": "Florianópolis"},
    {"contact_country": "São Paulo", "contact_city": "São Paulo"},
    {"contact_country": "Sergipe", "contact_city": "Aracaju"},
    {"contact_country": "Tocantins", "contact_city": "Palmas"},
]

is_opportunity = ["Sim", "Não"]

lifecycle_stage = ["Cliente", "Lead", "Lead Qualificado", "Visitante"]

contact_origin = [
    "Busca Orgânica",
    "Desconhecido",
    "Tráfego Direto",
    "Outras Publicidades",
    "Desconhecido",
    "Outros Canais",
    "Redes Sociais",
    "Email",
    "Display",
    "Referências",
    "Mídia Paga",
]


def create_contacts(x) -> object:
    fake_data = {}
    for i in range(0, x):
        fake_data[i] = {}
        fake_data[i]["reference_day"] = event_timestamp_date
        fake_data[i]["tenant_id"] = uuid4()
        fake_data[i]["contact_id"] = uuid4()
        fake_data[i]["contact_name"] = fake.name()
        fake_data[i]["contact_email"] = fake.free_email()
        fake_data[i]["contact_job_title"] = fake.job()
        selected_location = random.choice(location)
        fake_data[i]["contact_city"] = selected_location["contact_city"]
        fake_data[i]["contact_country"] = selected_location["contact_country"]
        fake_data[i]["is_opportunity"] = random.choice(is_opportunity)
        fake_data[i]["lifecycle_stage"] = random.choice(lifecycle_stage)
        fake_data[i]["contact_origin"] = random.choice(contact_origin)
        fake_data[i]["created_at"] = fake.date_time_between_dates(
            datetime_start=initial_date, datetime_end=event_timestamp_date - timedelta(minutes=1)
        )
        fake_data[i]["last_conversion_at"] = event_timestamp_date
    return fake_data

