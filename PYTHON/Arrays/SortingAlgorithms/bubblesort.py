def bubblesort(arr):
    n = len(arr)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the number of elements: "))
    print("Enter the elements of the array: ")
    for i in range (n):
        a = int(input())
        arr.append(a)
    bubblesort(arr)
    print("Sorted array: ")
    for i in range(n):
        print(arr[i])