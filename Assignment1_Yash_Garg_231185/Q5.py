import numpy as np
arr1 = np.random.randint(1,10,(3,3))
print(f'Matrix 1 : \n',arr1)
arr2 = np.random.randint(1,10,(3,3))
print('-'*15)
print(f'Matrix 2 : \n',arr2)
print('-'*15)
arr3=arr1@arr2
print(f'Matrix Product : \n',arr3)
print('-'*15)
det = np.linalg.det(arr3)
print(f'Determinant is : ',det)