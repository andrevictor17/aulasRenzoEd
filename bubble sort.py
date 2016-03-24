import unittest


def bubble_sort(seq):
    '''
    A função ordena uma lista usando o metodo bubble sort, a função faz 2 loops, o primeiro loop é a lista como um todo,
    e o segundo é a troca de dos elementos, no primeiro ele pega a lista toda e entra no segundo, ai ele faz as comparaçoes de 2 em 2 itens,
    caso o item for menor ele troca os 2 de lugar, assim quando a lista for ordenada ele sai dos 2 loops e termina a execução.E se caso a 
    lista ja estiver ordena antes de rodar todos os loops a função dá um break no for para otimizar a função.
    Em tempo de execução a função é O(n²), e para espaço de memoria é O(1).
    :param seq: lista
    :return: lista ordena pelo metodo bubble sort
    '''

    cont =0
    for i_corrente in range(len(seq)-1,0,-1):
        for n in range(i_corrente):
            if seq[n]>seq[n+1]:
                seq[n] , seq[n+1] = seq[n+1],seq[n]
                cont += 1
        if cont == 0:
            break
    return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
