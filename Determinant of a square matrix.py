"""determinant of a square matrix by Stylianos Regas"""
import math
import copy

'''displays the matrix in correct formatting'''
def printMatrix(ma):

    for i in range(len(ma)):
        print(ma[i],end = " ")


        i = i+1
        if i % math.sqrt(len(ma)) == int(0):
            print("")

'''finds the determinat of the square matrix'''
def Determinant(m):
    determinant = 0
    if m is not None:
        length = int(len(m))
        square = int(math.sqrt(length))


        if(length == 1):
            determinant = m[0]

        elif(length == 4):
            first = (m[0]*m[length-int(1)])
            second = (m[int(square-int(1))]*m[int(length-square)])
            determinant = first - second

        elif(length > 4):
            copy = m.copy()
            determinant = m[0]*Determinant(subMatrix(1,copy))
            copy = m.copy()



            for (i) in range(square-1):
                if(i % 2 == 0):
                    determinant -= (m[i+1])*(Determinant(subMatrix(i+2,copy)))
                    copy = m.copy()
                else:
                    determinant += (m[i+1])*(Determinant(subMatrix(i+2,copy)))
                    copy = m.copy()

    return determinant

'''finds the submatrices for the larger square matrices'''
def subMatrix(pos,mt):
    if mt is not None:
        square= int(math.sqrt(len(mt)))

        for count in range(square):
            mt.pop(0)

        for count in range(square-1):
            mt.pop(pos+(square *count)-(count+1))

    return mt

'''main asks for input on the distance of the matrix, and then asks for inputs for the numbers'''
n = int(input("enter the square for the matrix"))
matrix = []

for count in range(n*n):
    number = int(input("enter a number"))
    matrix.append(number)


printMatrix(matrix)

print("\n")
print("determinant of matrix: ",Determinant(matrix))






