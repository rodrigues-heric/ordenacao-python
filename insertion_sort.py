
### insertion sort function
def insertion_sort(list):
	for j in range(1, len(list)):
		chave = list[j]
		i = j-1

		while((i >= 0) and (list[i] > chave)):
			list[i+1] = list[i]
			i = i-1

		list[i+1] = chave

### main function
def main():
	# test variables
	arr1 = [12, 2, 5, 4, 8, 7, 6, 9, 1, 15]
	arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

	# print the lists
	print(arr1)
	insertion_sort(arr1)
	print(arr1)
	print()

	print(arr2)
	insertion_sort(arr2)
	print(arr2)
	print()

	print(arr3)
	insertion_sort(arr3)
	print(arr3)
	print()

if __name__ == "__main__":
	main()