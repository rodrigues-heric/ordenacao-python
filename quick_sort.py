import random

###################
def particao(lista, primeiro, ultimo):
    i = primeiro-1
    pivot = lista[ultimo]

    for j in range(primeiro, ultimo):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[ultimo] = lista[ultimo], lista[i+1]
    return (i+1)

###################
def quick_sort(lista, primeiro, ultimo):
    if len(lista) == 1:
        return lista 
    
    if primeiro < ultimo:
        part = particao(lista, primeiro, ultimo)

        quick_sort(lista, primeiro, part-1)
        quick_sort(lista, part+1, ultimo)


###################
def main():
    lista = [random.randint(0, 100) for x in range(10)]

    output = f'Lista aleatoria: \n{lista}'
    print(output)

    quick_sort(lista, 0, len(lista)-1)
    output = f'Lista ordenada: \n{lista}'
    print(output)

if __name__ == "__main__":
    main()