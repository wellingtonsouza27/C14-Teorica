from src.validator import validar_senha

# Testes Positivos
def test_positivo_basica():
    assert validar_senha("Senha123!") == True

def test_positivo_com_tamanho_minimo():
    assert validar_senha("Abc1@def") == True

def test_positivo_com_varios_simbolos():
    assert validar_senha("@Senha123!") == True

def test_positivo_com_letras_mistas():
    assert validar_senha("Aa123456!") == True

def test_positivo_com_numeros_grandes():
    assert validar_senha("Senha9999!") == True


# Testes Negativos
def test_negativo_muito_curta():
    assert validar_senha("S1!") == False

def test_negativo_sem_maiuscula():
    assert validar_senha("senha123!") == False

def test_negativo_sem_minuscula():
    assert validar_senha("SENHA123!") == False

def test_negativo_sem_numero():
    assert validar_senha("Senha!!!") == False

def test_negativo_sem_simbolo():
    assert validar_senha("Senha1234") == False