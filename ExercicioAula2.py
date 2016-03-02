def max_(n,v):
    if n == 1:
        return v[0]
    else:
        x = max_(n-1,v)
        
        if x > v[n-1]:
            return x
            
        else:
            return v[n-1]
        
def min_(n,v):
    
    if n == 1:
        return v[0]
    else:
        x = min_(n-1,v)
        
        if x < v[n-1]:
            return x
            
        else:
            return v[n-1]

def max_min(n,v):
    '''
    :param n: tamanho lista
    :param v: lista
    :return: (max,min)
    Retorna o maior e o menor numero de uma lista, usando apenas recurção.
    O desempenho do software é O(n), devido a simplicidade de comparação,
    apenas comparando com o anterior da lista,porem quanto maior a lista maior o uso de memoria.
    '''
    
    maior = max_(n,v)
    menor = min_(n,v)
    
    return maior,menor
    
    
    
vetor = [1,5,3,4,6,7,8,1,1,1,1,1,1]
p = len(vetor)

print(max_min(p,vetor))

