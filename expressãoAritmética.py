from aula4.pilha import Pilha
from aula5.fila import Fila

class ErroLexico(Exception):
    pass

class ErroSintatico(Exception):
    pass

def analise_lexica(expressao):
    """
    A função analisa um expreção e diz se está conforme os parametros passados,logo a função verifica se contem um caracter que nao seja alguns desses "0123456789.-+*/{}[]()"
    Tempo de execução O(n)
     Espaço de memoria O(n)
    :param expressao: recebe a expressao a ser analisada
    :return: fila com os caracteres indesejados  """

    fila = Fila()

    correto = R"0123456789.-+*/{}[]()"

    if expressao:
        valor = ''
        for n in expressao:
            if n in correto:
                if n in '(){}[].*/-+':
                    if valor:
                        fila.enfileirar(valor)
                        valor = ''
                    fila.enfileirar(n)
                else:
                    valor = valor + n
            else:
                raise ErroLexico()

        if valor:
            fila.enfileirar(valor)

    return fila


def analise_sintatica(fila):
    """
    Analisa a fila e diz se está sintatica ou nao.
    Tempo de execução O(n)
    Espaço de memoria O(n)
    :param expressao: fila a ser analisada
    :return: fila
    """

    if len(fila):
        fila_sintetica = Fila()
        valor = ''
        for n in range(len(fila)):
            if fila._deque[n] in '-+/*(){}[]':
                if valor:
                    if '.' in valor:
                        fila_sintetica.enfileirar(float(valor))
                    else:
                        fila_sintetica.enfileirar(int(valor))
                valor = ''
                fila_sintetica.enfileirar(fila._deque[n])
            else:
                valor = valor + fila._deque[n]
        if valor:
            if '.' in valor:
                fila_sintetica.enfileirar(float(valor))
            else:
                fila_sintetica.enfileirar(int(valor))
        return fila_sintetica
    else:
        raise ErroSintatico

def avaliar(expressao):
    """ Avalia a expressao e ve se está correta.
     Tempo de execução O(n)
     Espaço de memoria O(n)
     :param expressao: recebe a expressao a ser analisada
    :return: erro na expressao
    """
    if expressao:
        fila = analise_sintatica(analise_lexica(expressao))
        tamanho = len(fila)
        if tamanho == 1:
            return fila.primeiro()
        else:
            pilha = Pilha()
            for n in range(tamanho):
                pilha.empilhar(fila._deque[n])
                if pilha.__len__() >= 3 and str(pilha.topo()) not in '-+*/(){}[]':
                    valor = pilha.topo()
                    pilha.desempilhar()
                    if pilha.topo() == '+':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() + valor
                        pilha.empilhar(valor)
                    elif pilha.topo() == '-':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() - valor
                        pilha.empilhar(valor)
                    elif pilha.topo() == '*':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() * valor
                        pilha.empilhar(valor)
                    elif pilha.topo() == '/':
                        pilha.desempilhar()
                        valor = pilha.desempilhar() / valor
                        pilha.empilhar(valor)
                    else:
                        pilha.empilhar(valor)
                elif str(pilha.topo()) in ')}]' and n == tamanho - 1:
                    pilha.desempilhar()
                    while len(pilha) > 1:
                        if str(pilha.topo()) not in '-+*/(){}[]':
                            valor = pilha.topo()
                            pilha.desempilhar()
                            if pilha.topo() == '+':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() + valor
                                pilha.empilhar(valor)
                            elif pilha.topo() == '-':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() - valor
                                pilha.empilhar(valor)
                            elif pilha.topo() == '*':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() * valor
                                pilha.empilhar(valor)
                            elif pilha.topo() == '/':
                                pilha.desempilhar()
                                valor = pilha.desempilhar() / valor
                                pilha.empilhar(valor)
                            elif str(pilha.topo()) in '(){}[]':
                                pilha.desempilhar()
                                pilha.empilhar(valor)
                            else:
                                pilha.empilhar(valor)
                        else:
                            pilha.desempilhar()
            return pilha.topo()
    raise ErroSintatico()
import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],[e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
