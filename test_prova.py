import pytest
from exercicios import *

from unittest.mock import patch

## Ex01
def test_produto_sem_estoque():
    result = classificar_produto(0)
    assert result == "Sem estoque"

def test_produto_estoque_baixo():
    result = classificar_produto(4)
    assert result == "Estoque baixo"

def test_produto_estoque_normal():
    result = classificar_produto(10)
    assert result == "Estoque normal"

def test_produto_estoque_alto():
    result = classificar_produto(70)
    assert result == "Estoque alto"

def test_produto_negativo():
    result = classificar_produto(-8)
    assert result == "Quantidade inválida"

## Ex02
def test_frase_varias_palavras():
    result = inverter_palavras("Python é muito interessante")
    assert result == "interessante muito é Python"

def test_frase_apenas_uma_palavra():
    result = inverter_palavras("Python")
    assert result == "Python"

def test_frase_vazia():
    result = inverter_palavras("")
    assert result == ""

def test_frase_espaco_extra():
    result = inverter_palavras("Python é muito   interessante")
    assert result == "interessante muito é Python"

def test_frase_numero_letras():
    result = inverter_palavras("Python é muito 100")
    assert result == "100 muito é Python"

## Ex03
def test_documento_11_digitos():
    result = validar_documento("12345678900")
    assert result is True


def test_documento_formatado():
    result = validar_documento("123.456.789-00")
    assert result is True


def test_documento_menos_11_digitos():
    result = validar_documento("1234567890")
    assert result is False


def test_documento_mais_11_digitos():
    result = validar_documento("1234567890301")
    assert result is False


def test_documento_contendo_letras():
    result = validar_documento("1234567e900")
    assert result is False


def test_documento_vazio():
    result = validar_documento("")
    assert result is False


## Ex04
# 1. Verificar se a mensagem foi gerada corretamente
def test_verificar_mensagem_gerada():
    with patch("exercicios.gerar_codigo", return_value="USR-1234"):
        resultado = criar_identificacao("Carlos")
        assert resultado == "Usuário Carlos cadastrado com código USR-1234."


# 2. Verificar se gerar_codigo() foi chamada
def test_verificar_se_gerar_codigo_foi_chamada():
    with patch("exercicios.gerar_codigo", return_value="USR-1234") as mock_gerar:
        criar_identificacao("Ana")
        mock_gerar.assert_called()


# 3. Verificar se a função foi chamada apenas uma vez
def test_verificar_se_gerar_codigo_foi_chamada_apenas_uma_vez():
    with patch("exercicios.gerar_codigo", return_value="USR-1234") as mock_gerar:
        criar_identificacao("Ana")
        mock_gerar.assert_called_once()


# 4. Utilizar Mock para simular diferentes códigos
def test_simular_diferentes_codigos():
    codigos = ["USR-1000", "USR-2000", "USR-3000"]
    with patch("exercicios.gerar_codigo", side_effect=codigos):
        for codigo_esperado in codigos:
            resultado = criar_identificacao("Lucas")
            assert (
                resultado
                == f"Usuário Lucas cadastrado com código {codigo_esperado}."
            )


def test_verificar_comportamento_com_nomes_diferentes():
    nomes = ["Beatriz", "João Silva", "Maria"]
    with patch("exercicios.gerar_codigo", return_value="USR-9999"):
        for nome in nomes:
            resultado = criar_identificacao(nome)
            assert (
                resultado == f"Usuário {nome} cadastrado com código USR-9999."
            )



## EX05
def test_usuario_com_permissao():
    with patch("exercicios.verificar_permissao", return_value=True):
        resultado = acessar_sistema("Carlos")
        assert resultado == "Acesso autorizado"


def test_usuario_sem_permissao():
    with patch("exercicios.verificar_permissao", return_value=False):
        resultado = acessar_sistema("Estranho")
        assert resultado == "Acesso negado"


def test_verificar_permissao_foi_chamada():
    with patch("exercicios.verificar_permissao", return_value=True) as mock_verificar:
        acessar_sistema("Carlos")
        mock_verificar.assert_called()


def test_verificar_permissao_chamada_com_usuario_correto():
    with patch("exercicios.verificar_permissao", return_value=True) as mock_verificar:
        acessar_sistema("Carlos")
        mock_verificar.assert_called_once_with("Carlos")


def test_simular_dois_cenarios_com_mock():

    with patch("exercicios.verificar_permissao", return_value=True):
        assert acessar_sistema("Ana") == "Acesso autorizado"


    with patch("exercicios.verificar_permissao", return_value=False):
        assert acessar_sistema("Beto") == "Acesso negado"

##

@patch('exercicios.registrar_atendimento', return_value=True)
@patch('exercicios.obter_proximo_cliente', return_value="Ana")
def test_atendimento_sucesso(mock_obter, mock_registrar):
    resultado = atender_proximo_cliente()
    assert resultado == "Atendimento realizado"

@patch('exercicios.obter_proximo_cliente', return_value=None)
def test_fila_vazia(mock_obter):
    resultado = atender_proximo_cliente()
    assert resultado == "Fila vazia"


@patch('exercicios.registrar_atendimento', return_value=False)
@patch('exercicios.obter_proximo_cliente', return_value="Bruno")
def test_falha_registro(mock_obter, mock_registrar):
    resultado = atender_proximo_cliente()
    assert resultado == "Falha no atendimento"


@patch('exercicios.registrar_atendimento', return_value=True)
@patch('exercicios.obter_proximo_cliente', return_value="Carla")
def test_obter_cliente_chamado(mock_obter, mock_registrar):
    atender_proximo_cliente()
    mock_obter.assert_called_once()


@patch('exercicios.registrar_atendimento', return_value=True)
@patch('exercicios.obter_proximo_cliente', return_value="Daniel")
def test_registrar_cliente_correto(mock_obter, mock_registrar):
    atender_proximo_cliente()
    mock_registrar.assert_called_once_with("Daniel")


@patch('exercicios.registrar_atendimento')
@patch('exercicios.obter_proximo_cliente', return_value=None)
def test_registrar_nao_chamado_fila_vazia(mock_obter, mock_registrar):
    atender_proximo_cliente()
