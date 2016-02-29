def max_min(n,v):
    '''

    :param n: tamanho lista
    :param v: lista
    :return: (min,max)

    Retorna o maior e o menor numero de uma lista, usando apenas recurção.
    O desempenho do software é O¹, devido a simplicidade de comparação,
    apenas comparando com o anterior da lista.
    Tive apenas um problema que nao consegui solucionar, nao consigo colocar os 2 valores no return(maior e menor), 
    quando coloco qualquer uma das variaveis sozinhas elas imprimem, mais quando coloco as duas da erro.
    '''
    if n == 1:
        return v[0]
    else:
        x = max_min(n-1,v)

        if x > v[n-1]:
            maior = x
            
        else:
            maior = v[n-1]
        if x < v[n-1]:
            menor = x
            
        else:
            menor = v[n-1]
    return maior
    
    

vetor = [1,5,3,4,6,7,8,1,1,1,1,1,1]
p = len(vetor)

print(max_min(p,vetor))
