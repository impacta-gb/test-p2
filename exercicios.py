import re
import random

## Ex01
def classificar_produto(quantidade):
    if quantidade == 0:
        return "Sem estoque"
    elif quantidade >= 1 and quantidade <= 5:
        return "Estoque baixo"
    elif quantidade >= 6 and quantidade <= 20:
        return "Estoque normal"
    elif quantidade > 20:
        return "Estoque alto"
    else:
        return "Quantidade inválida"

## Ex02
def inverter_palavras(texto):
    frase = " ".join(texto.split()[::-1])
    return frase


## Ex03
def validar_documento(documento):
    regex = r"^(\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})$"
    if re.match(regex, documento):
        return True
    return False

## Ex04
def gerar_codigo():
    numero = random.randint(0000, 9999)
    return f"USR-{numero}"

def criar_identificacao(nome):
    return f"Usuário {nome} cadastrado com código {gerar_codigo()}."


##
def verificar_permissao(usuario: str) -> bool:
    usuarios_autorizados = ["admin", "carlos"]
    return usuario in usuarios_autorizados


def acessar_sistema(usuario: str) -> str:
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"

##

fila_de_espera = ["Ana", "Bruno", "Carla"]

def obter_proximo_cliente():
    if fila_de_espera:
        return fila_de_espera.pop(0)
    return None

def registrar_atendimento(cliente):
    return True

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    
    if cliente is None:
        return "Fila vazia"
    
    sucesso = registrar_atendimento(cliente)
    
    if sucesso:
        return "Atendimento realizado"
    else:
        return "Falha no atendimento"
