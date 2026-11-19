print("Exercício 11 — Comparação de três estados: o gerente deseja saber onde há mais municípios")

import requests

URL_GO = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/52/municipios"
)


resposta = requests.get(URL_GO, timeout=20)
resposta.raise_for_status()
municipios = resposta.json()

print("Total de registros  Goiás:", len(municipios))


URL_SP = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/35/municipios"
)

resposta = requests.get(URL_SP, timeout=20)
resposta.raise_for_status()
municipios = resposta.json()

print("Total de registros São Paulo:", len(municipios))


URL_MG = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/31/municipios"
)

resposta = requests.get(URL_MG, timeout=20)
resposta.raise_for_status()
municipios = resposta.json()

print("Total de registros Minas Gerais:", len(municipios))

