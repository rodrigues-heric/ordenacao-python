### insertion sort (para shell short)
def insertion_sort_v2(lista, inicio, incremento):
	for j in range(inicio+incremento, len(lista), incremento):
		chave = lista[j]
		i = j-incremento

		while((i >= 0) and (lista[i] > chave)):
			lista[i+incremento] = lista[i]
			i = i-incremento

		lista[i+incremento] = chave

### shell short 
def shell_sort(lista, passos):
	### imprime a lista inicial
	print(lista)

	### comeca ordenacao
	for p in range(passos, 0, -1):
		### prepara o incremento de cada laco
		incremento = (2**(p-1))
		
		for j in range(0, incremento):
			insertion_sort_v2(lista, j, incremento)
			
		print(lista)


### funcao que calcula (len(lista) / (2^k))
def num_passos(lista):
	### variaveis
	expoente = 1
	flag = True

	### em cada laco procura qual o maior valor possivel
	### que pode ser dividido o tamanho da lista
	while(flag):
		if((len(lista) / (2**expoente)) >= 1):
			expoente += 1
		else:
			flag = False

	expoente -= 1
	return expoente

### funcao principal
def main():
	# variaveis teste
	arr1 = [12, 2, 5, 4, 8, 7, 6, 9, 1, 15]
	arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	arr4 = []

	### decrementa de 20 ate 1
	### range(inicio, fim, incremento)
	for i in range(20, 0, -1):
		arr4.append(i)

	print("Lista 1:")
	shell_sort(arr1, num_passos(arr1))
	print("\n")

	print("Lista 2:")
	shell_sort(arr2, num_passos(arr2))
	print("\n")

	print("Lista 3:")
	shell_sort(arr3, num_passos(arr3))
	print("\n")

	print("Lista 4:")
	shell_sort(arr4, num_passos(arr4))
	print("\n")

if __name__ == "__main__":
	main()