#!/usr/bin/env python
# coding: utf-8

# # Introdução
# 
# #### Este projeto investigará se existe a correlação entre o potencial econômico de um país e a expectativa de vida de seus cidadãos.
# 
# ##### Os objetivos são preparar os dados, seguidos da análise com gráficos e buscar explicar os achados do estudo.
# 
# Aqui estão algumas perguntas que este projeto buscará responder:
# 
# A expectativa de vida aumentou ao longo do tempo nas seis nações?
# O PIB aumentou ao longo do tempo nas seis nações?
# Existe uma correlação entre o PIB e a expectativa de vida de um país?
# Qual é a expectativa média de vida nessas nações?
# Qual é a distribuição dessa expectativa de vida?
# Fontes de dados
# 
# PIB Fonte: Dados das contas nacionais do Banco Mundial e arquivos de dados das Contas Nacionais da OCDE.
# 
# Expectativa de vida Fonte de dados: Organização Mundial da Saúde

# In[112]:


#Importando módulos 
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

#Carregando o banco de dados
all_data = pd.read_csv("all_data.csv")

##Analisando os tipos de dados do banco
print(all_data['Country'].unique())

##Renomeando as colunas de forma mais dinâmica
all_data = all_data.rename({"Life expectancy at birth (years)":"LEABY"}, axis = "columns")
print(all_data.head())

##Filtrando o banco de dados por país
countries_in_data = all_data['Country'].unique()

##Ditribuição dos dados referente ao PIB
plt.figure(figsize=(8,6))
sns.displot(all_data.GDP, rug = True, kde=False)
plt.xlabel("PIB em trilhões")
plt.ylabel("Contagem")
plt.show()

##Ditribuição dos dados referente a expectativa de vida
plt.figure(figsize=(8,6))
sns.displot(all_data.LEABY, rug = True, kde=False)
plt.xlabel("Expectativa de vida em anos")
plt.ylabel("Contagem")
plt.show()

##Analisando a evolução da expectativa de vida de cada país ao longo do intervalo de dados
for country in countries_in_data:
    country_data = all_data[all_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['LEABY'], linestyle='--', marker='o')
    plt.title('Evolução da expectativa de vida por país')
    plt.xlabel('Ano')
    plt.ylabel('Expectativa de vida (Anos)')
plt.legend(countries_in_data)
plt.show()

##Analisando a evolução do PIB de cada país ao longo do intervalo de dados
for country in countries_in_data:
    country_data = all_data[all_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['GDP'], linestyle='--', marker='o')
    plt.title('Evolução do PIB por país')
    plt.xlabel('Ano')
    plt.ylabel('PIB')
plt.legend(countries_in_data)
plt.show()

##Analisando a relação entre o PIB e a expectativa de vida por país
for country in countries_in_data:
    country_data = all_data[all_data['Country'] == country]
    plt.subplot(1,2,1)
    plt.plot(country_data['Year'], country_data['GDP']/10**12)
    plt.xlabel('Ano')
    plt.ylabel('PIB em trilhões')
    plt.title('Evoulão PIB ' + country)
    plt.subplot(1,2,2)
    plt.plot(country_data['Year'], country_data['LEABY'])
    plt.ylabel('PIB em trilhões')
    plt.title('Evoulão PIB ' + country)
    plt.title('Evolução EdV ' + country)
    plt.subplots_adjust(wspace=1)
    plt.show()

##Analisando a representatividade do PIB por país.
PIB_total_por_pais = all_data.groupby(['Country']).sum().GDP
plt.pie(PIB_total_por_pais, labels=countries_in_data, autopct='%0.1f%%')
plt.show()

##Analisando o pico de expectativa de vida por país.
edv_max_por_pais = all_data.groupby(['Country']).max()['LEABY']
store_x = [element for element in range(len(countries_in_data))]
plt.figure(figsize=(10, 5))
plt.bar(store_x, edv_max_por_pais, width=0.3)
ax = plt.subplot()
ax.set_xticks(range(len(countries_in_data)))
ax.set_xticklabels(countries_in_data)
plt.show()

##Analisando a relação entre o PIB e a expectativa de vida por país.
graph = sns.FacetGrid(all_data, col="Country", col_wrap=3,
                      hue = "Country", sharey = False, sharex = False)
graph = (graph.map(sns.scatterplot,"LEABY", "GDP")
         .add_legend()
         .set_axis_labels("Life expectancy at birth (years)", "GDP in Trillions of U.S. Dollars"));



# In[ ]:




