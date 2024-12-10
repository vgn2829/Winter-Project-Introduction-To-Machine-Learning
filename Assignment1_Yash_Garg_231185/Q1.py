import numpy as np
arr=np.random.randint(low=1,high=100,size=(4,4,4))
print(arr)
mean=arr.mean()
std_dev=arr.std()
print("-"*150)
z_value=(arr-mean)/std_dev
print(f'Z_Score : \n',z_value)
    


