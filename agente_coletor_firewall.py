import ipaddress
import os
import random
import sys
from datetime import datetime, timezone

import requests


ES_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200").rstrip("/")
ES_INDEX = os.getenv("ELASTICSEARCH_INDEX", "incidentes")
ES_USERNAME = os.getenv("ELASTICSEARCH_USERNAME")
ES_PASSWORD = os.getenv("ELASTICSEARCH_PASSWORD")

URL_ES = f"{ES_URL}/{ES_INDEX}/_doc"


def gerar_ipv4_aleatorio():
    while True:
        bits_aleatorios = random.getrandbits(32)
        ipv4 = ipaddress.IPv4Address(bits_aleatorios)
        if not ipv4.is_unspecified and not ipv4.is_loopback:
            return str(ipv4)


def main():
    if bool(ES_USERNAME) != bool(ES_PASSWORD):
        print(
            "Configure ELASTICSEARCH_USERNAME e ELASTICSEARCH_PASSWORD juntos.",
            file=sys.stderr,
        )
        return 1

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds").replace(
        "+00:00", "Z"
    )
    ipv4_origem = gerar_ipv4_aleatorio()
    ipv4_destino = "10.0.1.20"
    mensagem = {
        "@timestamp": timestamp,
        "ipv4": ipv4_origem,
        "src_ip": ipv4_origem,
        "dest_ip": ipv4_destino,
        "action": "deny",
        "message": (
            f"timestamp={timestamp} hostname=fw-01 src_ip={ipv4_origem} "
            f"dest_ip={ipv4_destino} src_port=54321 dest_port=22 "
            "proto=tcp action=deny"
        ),
    }
    autenticacao = (ES_USERNAME, ES_PASSWORD) if ES_USERNAME else None

    try:
        response = requests.post(
            URL_ES,
            json=mensagem,
            auth=autenticacao,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as erro:
        print(f"Falha ao enviar documento para o Elasticsearch: {erro}", file=sys.stderr)
        return 1

    print(f"Documento enviado para '{ES_INDEX}' (HTTP {response.status_code}).")
    print(f"IPv4 aleatório: {mensagem['ipv4']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
