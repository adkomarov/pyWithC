import ctypes
 
clibrary = ctypes.CDLL(r"./module.so")
 
addTwoNumbers = clibrary.add
addTwoNumbers.argtypes = [ctypes.c_int]
addTwoNumbers.restype = ctypes.c_int

qw=[]
for i in range(10,100):
    qw.append(addTwoNumbers(i))


print(qw)

'''
gcc -shared -o module.so -fPIC module.c
'''