def insertion_sort():
    arr = []
    n = int(input("Enter the number of elements in the list: "))
    for i in range(n):
        element = int(input("Enter element {}:".format(i+1)))
        arr.append(element)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print("Sorted list:", arr)
print(insertion_sort())