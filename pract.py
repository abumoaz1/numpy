import numpy as np

def Get_the_Numpy_version():
    print("Numpy version:", np.__version__)

def Show_the_Numpy_build_configuration():
    return np.show_config()

def get_help_with_numpy():
    return help(np.add)

def Create_a_null_vector_of_size_10():
    return np.zeros(10)
# print(Create_a_null_vector_of_size_10())

def Create_a_null_vector_of_size_10_and_update_the_fifth_value_to_1():
    a = np.zeros(10)
    a[4] = 1
    return a
# print(Create_a_null_vector_of_size_10_and_update_the_fifth_value_to_1())

def Create_a_vector_with_values_ranging_from_10_to_49():
    return np.arange(10, 50)
# print(Create_a_vector_with_values_ranging_from_10_to_49())

def Reverse_a_vector():
    a = np.arange(10, 50)
    return a[::-1]
# print(Reverse_a_vector())

def Create_a_3x3_matrix_with_values_ranging_from_0_to_8():
    return np.arange(9).reshape(3, 3)
# print(Create_a_3x3_matrix_with_values_ranging_from_0_to_8())

def Find_indices_of_non_zero_elements():
    a = np.array([1, 2, 0, 0, 4, 0])
    return np.nonzero(a)
# print(Find_indices_of_non_zero_elements())

def Create_a_3x3_identity_matrix():
    return np.eye(3)
# print(Create_a_3x3_identity_matrix())

def Create_a_3x3x3_array_with_random_values():
    return np.random.random((3, 3, 3))
# print(Create_a_3x3x3_array_with_random_values())

def Create_a_10x10_array_with_random_values_and_find_the_minimum_and_maximum_values():
    a = np.random.randint(0, 100, (10, 10))
    return a.min(), a.max()
# print(Create_a_10x10_array_with_random_values_and_find_the_minimum_and_maximum_values())

def Create_a_random_vector_of_size_30_and_find_the_mean_value():
    a = np.random.random(30)
    return a.mean()
# print(Create_a_random_vector_of_size_30_and_find_the_mean_value())

def Create_a_2d_array_with_1_on_the_border_and_0_inside():
    a = np.ones((5, 5))
    a[1:-1, 1:-1] = 0
    return a
print(Create_a_2d_array_with_1_on_the_border_and_0_inside())