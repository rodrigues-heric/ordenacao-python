import random

###################
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista)//2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        # listas temporarias
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1

            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # verifica se elementos foram deixdos
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

###################
def main():
    lista = [random.randint(0, 100) for x in range(10)]

    output = f'Lista aleatoria: \n{lista}'
    print(output)

    merge_sort(lista)
    output = f'Lista ordenada: \n{lista}'
    print(output)

if __name__ == "__main__":
    main()