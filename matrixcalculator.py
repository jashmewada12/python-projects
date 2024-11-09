import numpy as np
import os,time
def clrscr():
    os.system("cls" if os.name == "nt" else "clear")

def viewmat(matrix):
    for rows in matrix:
        print(*rows)
        

def display():
    clrscr()
    print("------Matrix Calculator------")
    print("1.Transpose of matrix1")
    print("2.Transpose of matrix2")
    print("3.Multiply matrix 1 & 2")
    print("4.Adding both the matrix")
    print("5.Subtracting matrix")
    print("6.View matrix")
    print("7.Adjoint of matrix 1")
    print("8.Adjoint of matrix 2")
    print("9.exit")
    print("-----------------------------")

def values(rows,cols):
    matrix = np.zeros((rows,cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            matrix[i,j] = int(input(f"Enter the value for [{i,j}]:"))
    return matrix
     

column1 = int(input("Columns on matrix1:"))
row1 = int(input("Rows on matrix1:"))
matrix1 = values(row1,column1)

column2 = int(input("Columns on mat2:"))
row2 = int(input("Rows on mat 2: "))
matrix2 = values(row2,column2)



while True:
    display()
    choice = int(input("Enter :"))
    if choice == 1:
        clrscr()
        print("Transpose of matrix1 :")
        viewmat(matrix1.T)
        time.sleep(4)
    
    elif choice ==  2:
        clrscr()
        print("Transpose of matrix2 :")    
        viewmat(matrix2.T)
        time.sleep(4)
    
    
    elif choice == 3:
        clrscr()
        if matrix1.shape[1] == matrix2.shape[0]:
            print(f"Multplication of the matrix is :")
            matrixm = np.dot(matrix1,matrix2)
            viewmat(matrixm)
            time.sleep(4)
    
    
    elif choice == 4:
        clrscr()
        if matrix1.shape == matrix2.shape:
            print(f"The addition of both the matrix is: ")
            matrixa = matrix1 + matrix2
            viewmat(matrixa)
            time.sleep(4)
    
    elif choice == 5:
        clrscr()
        if matrix1.shape == matrix2.shape:
            print(f"The subtraction of matrix is:")
            matrixsub = matrix1 - matrix2
            viewmat(matrixsub)
            time.sleep(4)
    

    
    elif choice == 6:
        clrscr()
        mat = int(input("what matrix:"))
        if mat == 1:
           viewmat(matrix1)
           time.sleep(4)
     
        elif mat == 2:
            viewmat(matrix2)
            time.sleep(4)
    
    elif choice == 7:
        adjmat1 = matrix1.conjugate().T
        viewmat(adjmat1)
        time.sleep(4)

    elif choice == 8:
        adjmat2 =matrix2.conjugate().T 
        viewmat(adjmat2)   
        time.sleep(4)
    elif choice == 9:
        break
    
    else:
        print("Invalid input")
        continue        