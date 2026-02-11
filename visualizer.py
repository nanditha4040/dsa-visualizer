import random
import time
import os

def generate_array():
    return [random.randint(1, 15) for _ in range(8)]

def show(arr):
    os.system('cls')
    for x in arr:
        print("█" * x)
    print("-" * 20)
    time.sleep(0.4)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            show(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = generate_array()
bubble_sort(arr)
