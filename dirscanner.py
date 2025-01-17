import requests
import argparse

# Configuração do argparse para capturar o domínio da linha de comando
parser = argparse.ArgumentParser(description="Simple Directory Scanner")
parser.add_argument("domain", type=str, help="Domain to scan (e.g., http://example.com)")
args = parser.parse_args()

# Obtém o domínio do argumento
domain = args.domain

# Lista de diretórios a serem verificados
directories = ["login.php", "admin", "js/scripts.js"]

print("DirScanner is starting...")

# Loop para verificar cada diretório
for dir in directories:
    link = f"{domain}/{dir}"  # Adiciona "/" entre o domínio e o diretório
    try:
        r = requests.get(link, timeout=5)  # Faz a requisição HTTP com timeout
        if r.status_code == 200:
            print(f"Directory [+] {link}")
        else:
            print(f"Directory [-] {link}")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {link}: {e}")

print("[X] Scan Completed")
