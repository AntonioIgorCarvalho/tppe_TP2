def descricaoInvalida(descricao:str) -> bool:
    return descricao == None or descricao == ""

def valorInvalido(valor:float) -> bool:
    return valor <= 0 or valor == None