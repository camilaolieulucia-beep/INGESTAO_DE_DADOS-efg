print("Exercício 14 — Frequência das letras iniciais")

import requests

URL_GO = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/52/municipios"
)


resposta = requests.get(URL_GO, timeout=20)
resposta.raise_for_status()
municipios = resposta.json()

letras_iniciais = {}
for municipio in municipios:
    letra_inicial = municipio["nome"][0].upper()
    if letra_inicial in letras_iniciais:
        letras_iniciais[letra_inicial] += 1
    else:
        letras_iniciais[letra_inicial] = 1
        
print("Frequência das letras iniciais:", letras_iniciais)
print(f" A letra com maior frequência é a letra: {max(letras_iniciais, key=letras_iniciais.get)}, que aparece {max(letras_iniciais.values())} vezes.")
