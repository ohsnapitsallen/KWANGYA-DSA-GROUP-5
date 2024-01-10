import TestData
import time


def measuretime(search_function, data_set, target_element):
    start_time = time.time()
    result = search_function(data_set, target_element)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time
    
test_data_instance = TestData.testdata()
element_to_search = TestData.element_to_search()
    
#LinearSearch
linearsearch_result, linearsearch_time = measuretime(test_data_instance.linear_search, test_data_instance.small_data_set, element_to_search)
    
#BinarySearch
binarysearch_result, binarysearch_time = measuretime(test_data_instance.binary_search, test_data_instance.small_data_set, element_to_search)
    
#JumpSearch
jumpsearch_result, jumpsearch_time = measuretime(test_data_instance.jump_search, test_data_instance.small_data_set, element_to_search)
    
#ExponentialSearch
exponentialsearch_result, exponentialsearch_time = measuretime(test_data_instance.exponential_search, test_data_instance.small_data_set, element_to_search)
    
#InterpolationSearch
interpolationsearch_result, interpolationsearch_time = measuretime(test_data_instance.interpolation_search, test_data_instance.small_data_set, element_to_search)
    
#TermarySearch
ternarysearch_result, ternarysearch_time = measuretime(test_data_instance.ternary_search, test_data_instance.small_data_set, element_to_search)
    
print(f"Linear Search Result: {linearsearch_result}, Time Measured: {linearsearch_time}")
print(f"Binary Search Result: {binarysearch_result}, Time Measured: {binarysearch_time}")
print(f"Jump Search Result: {jumpsearch_result}, Time Measured: {jumpsearch_time}")
print(f"Exponential Search Result: {exponentialsearch_result}, Time Measured: {exponentialsearch_time}")
print(f"Interpolation Search Result: {interpolationsearch_result}, Time Measured: {interpolationsearch_time}")
print(f"Ternary Search Result: {ternarysearch_result}, Time Measured: {ternarysearch_time}")
    


    