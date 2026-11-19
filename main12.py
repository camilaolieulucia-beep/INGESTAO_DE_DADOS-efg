print("Exercício 12 — Participação percentual")

import requests

URL_GO = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/52/municipios"
)


resposta = requests.get(URL_GO, timeout=20)
resposta.raise_for_status()
municipios_go = resposta.json()

quantidade_estado = len(municipios_go) 
quantidade_total  = len(municipios_go)

percentual = quantidade_estado / quantidade_total * 100
print(f"Percentual de municípios GO: {percentual:.2f}") 


URL_SP = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/35/municipios"
)

resposta = requests.get(URL_SP, timeout=20)
resposta.raise_for_status()
municipios_sp = resposta.json()


quantidade_estado = len(municipios_sp) 
quantidade_total  = len(municipios_sp)

percentual = quantidade_estado / quantidade_total * 100
print(f"Percentual de municípios SP: {percentual:.2f}") 

URL_MG = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/31/municipios"
)

resposta = requests.get(URL_MG, timeout=20)
resposta.raise_for_status()
municipios_mg = resposta.json()


quantidade_estado = len(municipios_mg) 
quantidade_total  = len(municipios_mg)



percentual = quantidade_estado / quantidade_total * 100
print(f"Percentual de municípios MG: {percentual:.2f}") 
