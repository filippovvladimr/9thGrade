def Matrix_Multiplication(A,B):
   if len(A[0]) != len(B):
       return "Error"

   m = len(A)
   n = len(B)
   p = len(B[0])

   result = [[0 for i in range(p)] for i in range(m)]

   for i in range(m):
       for j in range(p):
           for k in range(n):
               result[i][j] += A[i][k] * B[k][j]
   return result

print(Matrix_Multiplication([[1, 2, 3], [4, 5, 6], [7, 8, 9]] , [[1,2], [3,4], [5,6]]))



