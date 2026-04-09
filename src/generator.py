import secrets
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))