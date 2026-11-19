print("Exercício 13 — Ranking dos estados")


import requests

URL_GO = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/52/municipios"
)


resposta = requests.get(URL_GO, timeout=20)
resposta.raise_for_status()
municipios_go = resposta.json()

print("Total de registros  Goiás:", len(municipios_go))


URL_SP = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/35/municipios"
)

resposta = requests.get(URL_SP, timeout=20)
resposta.raise_for_status()
municipios_sp = resposta.json()

print("Total de registros São Paulo:", len(municipios_sp))


URL_MG = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/31/municipios"
)

resposta = requests.get(URL_MG, timeout=20)
resposta.raise_for_status()
municipios_mg = resposta.json()

print("Total de registros Minas Gerais:", len(municipios_mg))

dicionario = {
    "estado_go": {"Goiás": len(municipios_go)},
    "estado_sp": {"São Paulo": len(municipios_sp)},    
    "estado_mg": {"Minas Gerais": len(municipios_mg)},
    "total": len(municipios_go) + len(municipios_sp) + len(municipios_mg),
    "ativo": True,
}
ranking_estados = sorted([dicionario["estado_go"], dicionario["estado_sp"], dicionario["estado_mg"]], key=lambda item: list(item.values())[0], reverse=True)
print("Ranking dos estados:", ranking_estados)



