import random

class testdata:
    def __init__(self):
        self.small_data_set = list(range(1, 101))
        self.medium_data_set = list(range(1, 1001))
        self.large_data_set = list(range(1, 10001))
        random.shuffle(self.small_data_set)
        random.shuffle(self.medium_data_set)
        random.shuffle(self.large_data_set)
        
    def get_element_to_search(self):
        return int(input("Enter a number you want to find: "))

    def linear_search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    def binary_search(self, arr, x):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def jump_search(self, arr, x):
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0

        while arr[min(step, n) - 1] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1

        for i in range(prev, min(step, n)):
            if arr[i] == x:
                return i

        return -1

    def exponential_search(self, arr, x):
        n = len(arr)
        if arr[0] == x:
            return 0

        i = 1
        while i < n and arr[i] <= x:
            i *= 2

        return self.binary_search(arr[:min(i, n)], x)

    def interpolation_search(self, arr, x):
        low, high = 0, len(arr) - 1

        while low <= high and arr[low] <= x <= arr[high]:
            pos = low + ((high - low) // (arr[high] - arr[low])) * (x - arr[low])

            if arr[pos] == x:
                return pos
            elif arr[pos] < x:
                low = pos + 1
            else:
                high = pos - 1

        return -1

    def ternary_search(self, arr, x):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid1 = low + (high - low) // 3
            mid2 = high - (high - low) // 3

            if arr[mid1] == x:
                return mid1
            elif arr[mid2] == x:
                return mid2

            if x < arr[mid1]:
                high = mid1 - 1
            elif x > arr[mid2]:
                low = mid2 + 1
            else:
                low = mid1 + 1
                high = mid2 - 1

        return -1


#test_data_instance = testdata()
#element_to_search = test_data_instance.get_element_to_search()
#linearsearch = test_data_instance.linear_search(test_data_instance.small_data_set, element_to_search)
#binarysearch = test_data_instance.binary_search(test_data_instance.small_data_set, element_to_search)
#jumpsearch = test_data_instance.jump_search(test_data_instance.small_data_set, element_to_search)
#exponentialsearch = test_data_instance.exponential_search(test_data_instance.small_data_set, element_to_search)
#interpolationsearch = test_data_instance.interpolation_search(test_data_instance.small_data_set, element_to_search)
#ternarysearch = test_data_instance.ternary_search(test_data_instance.small_data_set, element_to_search)