import numpy as np
array_1=np.array([1,2,3],dtype='int16') #For Making An Array
print(array_1)
#Getting Dimensions
print(array_1.ndim)
#Getting Shape
array_2=np.array([[1,2,3],[5,6,7]])
print(array_2)
print(array_2.shape) #Matrix Dimensions
#Getting Type
print(array_1.dtype)
print(array_1.itemsize)
#Get Total Size
print(array_1.nbytes)
print(array_1.size) #Total Number Of Element
#Accessing Specific Element And Row or Column
array_3=np.array([[1,2,3,4,5,6,7],[7,8,9,0,1,2,8]])
print(array_3)
print(array_3.shape)
print(array_3[0,6]) #Indexing Starts From Zero
print(array_3[0,-3]) #Negative Indexing Works
print(array_3[0,:]) #For A Specific Row
print(array_3[:,0]) #For A Specific Column
print(array_3[0,1:6:2]) #[Startindex:EndIndex:StepSize]
array_3[1,5]=978 #Replacing An Element
print(array_3)
array_3[:,1]=[45,87]
print(array_3) #Changing A Column We Can Also Change Row
array_4=np.array([[[[[1,2],[3,4],[5,6],[7,8]]]]]) #3D Array
print(array_4)
#Initializing Different Type Of Array
print(np.zeros((2,3)))
print(np.ones((2,4)))
print(np.full((2,2),567))
print(np.full(array_4.shape,5647))
print(np.full_like(array_4,7658))
print(np.random.rand(4,4))
print(np.random.random_sample(array_1))
print(np.random.randint(567,size=(2,2)))
print(np.random.randint(-4,7,size=(3,2)))
print(np.identity(3,dtype='int32')) #By Default It Uses float64 Data Type
identity_matrix=np.identity(3)
print(identity_matrix.dtype)
#Repeat An Array
array_5=np.array([[1,2,3],[4,5,6]])
print(array_5)
print(np.repeat(array_5,3,axis=0))
array_6=np.ones((5,5),dtype='int32')
array_7=np.zeros((3,3),dtype='int32')
array_7[1,1]=9
print(array_6)
print(array_7)
array_6[1:4,1:4]=array_7
print(array_6)
#Copying An Array
array_8=np.array([[1,2,3]])
array_9=array_8.copy() #<----It doesn't Copy it Instead It Points If You Wanna Copy It Use .Copy Method
array_9[0,2]=77
print(array_8)
print(array_9)
array_8=array_8+2
print(array_8) #Elementwise Addition Could Also be Subtraction and Multiplication or Division
array_8=array_8**2 #And Exponentiation
print(array_8)
array_10=np.array([5,6,7])
array_11=np.array([8,9,10])
print(array_10+array_11) #Additon of Two Array's
array_10=np.sin(array_10) #<----- Taking Sine Of All The Values In The Array
print(array_10)
array_10=np.arccosh(array_10) #<------ Taking Arccosh Of All The Value In The Array
try:
    print(array_10)
except:
    print('there was an error')
#I've Used Try And Except To Get Rid Of An Runtime Warning
#LINEAR ALGEBRA
array_12=np.full((3,2),2,dtype='int32')
print(array_12)
array_13=np.full((2,3),3,dtype='int32')
print(array_13)
array_14=np.matmul(array_13,array_12) #<---- The Final Matrix's Order Depends On the Sequence Of the Argument's Passed In Matmul Function

#We Use Matmul Function When Order Of the matrix Isn't The Same If the Order Is Same Then We can Proceed With Normal Multiplication


# HOW TO GET THE DETERMINANT OF A MATRICE


print(array_14)
array_15=np.ones((3,3),dtype='int32')
print(array_15)
array_15=np.linalg.det(array_15) #<---- To Get The Determinant
print(array_15)
array_16=np.identity(3,dtype='int32')
print(array_16)
array_16=np.linalg.det(array_16)
print(array_16)


#STATISTICS
array_17=np.array([[1,2,3],[5,6,7]])
array_18=array_17.copy()
array_19=array_17.copy()
array_17=np.min(array_17)
print(array_17)
array_18=np.max(array_18,axis=0)
print(array_18)
print(array_19)
print(np.sum(array_19))
print(np.sum(array_19,axis=0)) #<----This Add's ColumnWise
print(array_19)


# VERTICAL STACKING VECTORS AND HORIZONTAL STACKING VECTORS
array_20=np.array([546,678,989])
array_21=np.array([234,564,432])
print(array_20)
print(array_21)
array_22=np.vstack([array_21,array_20,array_21,array_20]) #Vstack Stacks One Array Over Another  BTW Stacking Also Depends Upon The Sequence Of the Argument Passed In.
print(array_22)
array_23=np.random.random((4,4))
array_24=np.random.random((4,4))
print(array_23)
print(array_24)
array_25=np.hstack([array_24,array_23])
print(array_25)

#LOADING A TXT FILE



filedata=np.genfromtxt('data.txt',delimiter=',',dtype='int16')
print(filedata)
filedata=filedata.astype('float64') #<---- AsType Method Changes The DataType
print(filedata)


#BOOLEAN MASKING AND ADVANCED INDEXING


print(filedata>6) #<---- All Combination Of Logical Operators Can Be Tried i.e >=,<=,== e.t.c.
print(filedata[filedata>6]) #<----Gives Us The Value Of The Element Where The Condition Is True
array_26=np.array([1,2,3,4,5,6,7,8,9])
print(array_26[[1,3,7]]) #<---Indexing With A List
filedata_1=np.genfromtxt('data.txt',delimiter=',',dtype='int32')
print(filedata_1)
print(np.any(filedata_1>6))
print(np.all(filedata_1>=7,axis=0))
print((filedata_1<2) & (filedata_1>6))
print(~((filedata_1<2) & (filedata_1>6))) #<---- Tilde Is Used As Not Operator








