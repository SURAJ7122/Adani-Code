import numpy as np
print("Enter no. of rows")
rows = int(input())
print("Enter no. of columns")
columns = int(input())
random_matrix_array = np.random.randint(1,100,size=(rows, columns))
print(random_matrix_array)




