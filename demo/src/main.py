import numpy as np 
import pandas as pd

def main():
    arr1=np.array([10,11,12,13,14,15])

    arr2d1 = np.array([[100,200],[10,12]])

    arr2 = np.array([20,30,40,50,60])

    #arr3 = arr1 + arr2

    print("sum",arr1.sum())

    print("mean",arr1.mean())

    print("standard deviation",arr1.std())

    arr22d = arr1.reshape(2,3)

    print(arr22d)

    A = np.array([[1,2],[3,4]])
    B = np.array([[5,6],[7,8]])

    C = np.dot(A,B)

    print(C)

    data = {
        "Name":["Jiten","Nambi","Rekha","Anil"],
        "Age":[40,34,35,38],
        "City":["Trv","Hyd","Blr","Trv"]
    }

    df= pd.DataFrame(data)

    print(df)

    df.to_csv("abcd.csv")

    df2= pd.read_csv("abcd.csv")

    print(df2["Name"])

if __name__=="__main__":
    main()