import sys
from datetime import datetime, timedelta

try:
    sexo = input("Informe seu sexo (masculino/feminino): ")
    if sexo.lower() not in ['masculino', 'feminino']:
        sys.exit("Sexo inválido, informe masculino ou feminino")

    nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    inicio_contri = input("Informe a data de início de contribuição (dd/mm/aaaa): ")

    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
    data_inicioc = datetime.strptime(inicio_contri, "%d/%m/%Y")

except ValueError:
    sys.exit("Formato de data inválido. Use dd/mm/aaaa")

data_reforma = datetime(2019, 11, 13)
data_hoje = datetime.today()

idade_dias = (data_hoje - data_nascimento).days
idade_anos = idade_dias // 365

dias_contri = (data_hoje - data_inicioc).days
anos_contri = dias_contri // 365

if data_inicioc < data_reforma:
    dias_contri_ate_reforma = (data_reforma - data_inicioc).days
    anos_contri_ate_reforma = dias_contri_ate_reforma // 365
else:
    anos_contri_ate_reforma = 0
    print("Início de contribuição após a reforma")

# --- Aposentadoria por idade ---
idade_nec = 65 if sexo.lower() == 'masculino' else 62
data_apo_idade = data_nascimento + timedelta(days=idade_nec * 365)

# Precisa de pelo menos 15 anos de contribuição
data_15_anos_contri = data_inicioc + timedelta(days=15 * 365)
if data_15_anos_contri > data_apo_idade:
    data_apo_idade = data_15_anos_contri

# --- Aposentadoria por tempo de contribuição com pedágio ---
tempo_nec = 35 if sexo.lower() == 'masculino' else 30
faltava_2019 = tempo_nec - anos_contri_ate_reforma

if faltava_2019 > 0:
    pedagio = faltava_2019 * 0.5
    total_faltando = faltava_2019 + pedagio
    dias_para_apo = int(total_faltando * 365)
    data_apo_pedagio = data_reforma + timedelta(days=dias_para_apo)
else:
    data_apo_pedagio = data_reforma

# --- Exibição dos resultados ---
print(f"\nIdade: {idade_anos} anos")
print(f"Tempo de contribuição: {anos_contri:.2f} anos")
print(f"Data de aposentadoria por idade: {data_apo_idade.strftime('%d/%m/%Y')}")
print(f"Data de aposentadoria por tempo de contribuição com pedágio: {data_apo_pedagio.strftime('%d/%m/%Y')}")

if data_hoje < data_apo_idade and data_hoje < data_apo_pedagio:
    print("Você ainda não pode se aposentar, nem por idade nem por tempo de contribuição.")









 
