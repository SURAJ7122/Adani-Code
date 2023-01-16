import numpy as np
print("Enter no. of rows")
rows = int(input())
print("Enter no. of columns")
columns = int(input())
random_matrix_array = np.random.randint(1,100,size=(rows, columns))
print(random_matrix_array)
my_2d_list = random_matrix_array

def sort_2d_list(my_2d_list, column_index):
    return sorted(my_2d_list, key=lambda x: x[column_index])

sorted_2d_list = sort_2d_list(my_2d_list, 1)
print(sorted_2d_list)