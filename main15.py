import requests

URL = (
    "https://servicodados.ibge.gov.br"
    "/api/v1/localidades/estados/52/municipios"
)

resposta = requests.get(URL, timeout=20)
resposta.raise_for_status()
municipios = resposta.json()
print(f"total de municípios: {len(municipios)}")

print("----------------------------------------------------------------")

municipio = [municipio for municipio in municipios if "goiás" in municipio["nome"].lower()]
print(f"total com nome Goiás: {len(municipio)} municípios")
print("----------------------------------------------------------------")
for municipio in municipio:
    print(municipio["nome"])

print("----------------------------------------------------------------")
quantidade_nomes_compostos = sum(1 for municipio in municipios if " " in municipio["nome"])
print(f"total de nomes compostos: {quantidade_nomes_compostos} municípios")
print("----------------------------------------------------------------")
média_tamanho_nomes = sum(len(municipio["nome"]) for municipio in municipios) / len(municipios)
print(f"média do tamanho dos nomes: {média_tamanho_nomes:.2f} caracteres")
print("----------------------------------------------------------------")

#município_com_nome_mais_longo; 
#total de ocorrências com IDs duplicados.