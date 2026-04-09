from src.generator import gerar_senha

def test_gera_senha_tamanho_padrao():
    senha = gerar_senha()
    assert len(senha) == 12

def test_gera_senha_tamanho_customizado():
    senha = gerar_senha(16)
    assert len(senha) == 16

def test_gera_senha_tipo_string():
    senha = gerar_senha()
    assert isinstance(senha, str)

def test_gera_senha_nao_vazia():
    senha = gerar_senha()
    assert senha != ""

def test_gera_senhas_diferentes():
    senha1 = gerar_senha()
    senha2 = gerar_senha()
    assert senha1 != senha2