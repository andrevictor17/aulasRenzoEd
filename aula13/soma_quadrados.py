from collections import Counter

def soma_quadrados(n):
    if n == 0:
        return [0]
    quadrado = []
    max = 1
    while (max  * max <= n):
        quadrado.append(max * max)
        max = max + 1

    historico = {0: 0}
    while len(quadrado)> 0:
        numero = n
        quadrado1 = quadrado.copy()
        x = quadrado1.pop()
        lista = []
        while(numero > 0):
            if numero in historico.keys() and numero is not n:
                lista = lista + historico[numero]
            else:
                if len(quadrado1) > 0:
                    if numero - x < 0:
                       x = quadrado1.pop()
                    else:
                        numero = numero - x
                        lista.append(x)
                        if(numero <= quadrado1[-1]):
                            x = quadrado1.pop()
                else:
                    numero = numero - x
                    lista.append(x)
        if n not in historico.keys():
            historico[n] = lista.copy()
        elif len(lista) <= len(historico[n]):
            historico[n] = lista.copy()
        quadrado.pop()
    return historico[n]

import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_1(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_2(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_3(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_4(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_5(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
