import unittest

def insertion_sort(seq):
    '''
    A função ordena uma lista usando o metodo insertion sort, a função faz 2 loops, o primeiro loop é a lista como um todo,
    e o segundo é a troca de dos elementos, no primeiro ele pega a lista toda apartir do segundo elemento e entra no segundo loop, ai ele faz as comparaçoes do item com o seu antecessor,
    caso o item for menor ele troca os 2 de lugar, assim quando a lista for ordenada ele sai dos 2 loops e termina a execução.E se caso a
    lista ja estiver ordena antes de rodar todos os loops a função dá um break no for para otimizar a função.
    Em tempo de execução a função é O(n²), e para espaço de memoria é O(1).
    :param seq: lista
    :return: lista ordena pelo metodo insertion_sort
    '''
    for i in range(1, len(seq)):
        aux = seq[i]
        n = i
         cont = 0
        while n > 0 and aux < seq[n - 1]:
            seq[n] = seq[n - 1]
            n -= 1
            cont += 1
        seq[n] = aux
        if cont == 0 :
            break
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
