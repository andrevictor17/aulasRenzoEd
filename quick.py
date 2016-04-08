import unittest
def _quick_recursivo(seq):
    def sort(inicio, final):
        if inicio >= final:
            return seq
        i_esquerda = inicio + 1
        i_direita = inicio + 1
        pivot = seq[inicio]
        while i_direita <= final:
            if seq[i_direita] < pivot:
                temp = seq[i_esquerda]
                seq[i_esquerda] = seq[i_direita]
                seq[i_direita] = temp
                i_esquerda += 1
            i_direita += 1
        temp = seq[inicio]
        seq[inicio] = seq[i_esquerda - 1]
        seq[i_esquerda - 1] = temp
        sort(inicio + 0, i_esquerda - 2)
        sort(i_esquerda, final)
    sort(0, len(seq) - 1)
    return seq

def quick_sort(seq):
    '''
    
    '''
    return _quick_recursivo(seq)


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
