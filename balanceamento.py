import unittest

class PilhaVaziaErro(Exception):
    pass


class Pilha():
    def __init__(self):
        self.pilha = []

    def topo(self):
        try:
            return self.pilha[-1]
        except:
            raise PilhaVaziaErro()

    def vazia(self):
        if len(self.pilha) == 0:
            return True
    def empilhar(self,valor):
        self.pilha.append(valor)
    def desempilhar(self):
        if len(self.pilha) == 0:
            raise PilhaVaziaErro()
        else:
            return self.pilha.pop(-1)


def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    :param expressao: string com expressao a ser balanceada
    :param abre: contem os caracteres que abrem
    :param fecha: contem os caracteres que fecham
    :param pilha: recebe a classe pilha
    :param tam: recebe o tamanho
    :param quant: recebe a quantidade de vezes que a função "passa"

    A função vai comparar toda a string, quando passa na lista 'abre' ele adciona na pilha o conteudo
    semelhante da lista 'fecha', quando se encontra um parametro da lista 'fecha' se tira o ultimo item da pilha
    e se compara, caso seja igual adciona +1 a variavel 'quant', se caso a variavel tiver o mesmo valor da variavel 'tam'
    a expressao está balanceada
    A logica é simples, então sempre será O(n), pois ele varre a string toda em todos os casos   
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    abre = ['(','[','{']
    fecha = [')',']','}']
    pilha = Pilha()
    tam =0
    quant = 0
    for i in range(len(expressao)):
        for x in range(3):
            if expressao[i] == abre[x]:
                pilha.empilhar(fecha[x])
                tam += 0.5
            elif (expressao[i] == fecha[x] and pilha.vazia()):
                return False
            elif expressao[i] == fecha[x]:
                comparacao = pilha.desempilhar()
                tam +=0.5
                if comparacao == fecha[x]:
                    quant += 1

    if quant == tam:
        return True
    else:
        return False



class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
