numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def linear_search(numbers, target):
    steps=0
    for index, n in enumerate(numbers):
        steps+=1
        if n==target:
            return index, steps
    return -1, steps

def binary_search(numbers, target):
    low=0
    high=len(numbers) -1
    steps=0
    while low<=high:
        steps+=1
        mid = low + (high-low)//2
        if numbers[mid]==target:
            return mid, steps
        if numbers[mid]<target:
            low=mid + 1
        else:
            high=mid-1
    return -1, steps

def main():
    print('Searching for 1')
    print(linear_search(numbers, 1))
    print(binary_search(numbers,1))
    print('Searching for 7')
    print(linear_search(numbers, 7))
    print(binary_search(numbers,7))
    print('Searching for 15')
    print(linear_search(numbers, 15))
    print(binary_search(numbers,15))
    print('Searching for 18')
    print(linear_search(numbers, 18))
    print(binary_search(numbers,18))

main()