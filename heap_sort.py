import random

###################
def heapify(lista, tamanho, index):
    maior = index 
    esquerda = 2 * index + 1
    direita  = 2 * index + 2

    if esquerda < tamanho and lista[index] < lista[esquerda]:
        maior = esquerda 

    if direita < tamanho and lista[maior] < lista[direita]:
        maior = direita

    if maior != index:
        lista[index], lista[maior] = lista[maior], lista[index]
        heapify(lista, tamanho, maior)

###################
def heap_sort(lista):
    tamanho = len(lista)

    for i in range(tamanho//2 - 1, -1, -1):
        heapify(lista, tamanho, i) 

    for i in range(tamanho-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

###################
def main():
    ### listas aleatorias
    crescente = [random.randint(0, 100) for x in range(10)]
    
    output = f'Lista em ordem aleatoria: \n{crescente}'
    print(output)

    heap_sort(crescente)
    
    output = f'\nLista em ordem crescente: \n{crescente}'
    print(output)

if __name__ == "__main__":
    main()