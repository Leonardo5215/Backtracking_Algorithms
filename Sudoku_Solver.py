import time #imported to track the elapse time of the

def valid_pos_n_num (matrix, x_pos, y_pos, n):
    '''
    Parameters
    ----------
    matrix : List (Matrix)
        Sudoku Matrix 8x8.
    x_pos : Int
        x position of the number.
    y_pos : Int
        y position of the number.
    n : Int
        Input number.

    Returns
    -------
    True if the number is well placed by sudoku rules
    False if the number not comply with the sudoku rules.

    '''
    valid = False #valid flag
   
    
    if matrix[x_pos][y_pos] == 0:
        
        if n>=1 and n<=9: #checks if the number must be between 1 and 9
               
            for i in range(9): #check if the number is repeted in one of the columns
                 if matrix[i][y_pos] == n:
                     return False
                  
            for j in range(9): #check if the number is repeted in one of the rows
                 if matrix[x_pos][j] == n:
                     return False
                     
            rowSq = (x_pos // 3) *3
            colSq = (y_pos // 3) *3   
    
            for i in range(rowSq,rowSq+3,1): #checks if the the number is repeted in the give sector
                for j in range(colSq, colSq+3):
                    if matrix[i][j] == n:
                        return False 
            
            valid = True #Valid flag 
    
    return valid


#Given solvable sodoku riddle
matrix =[[8, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 3, 6, 0, 0, 0, 0, 0], 
         [0, 7, 0, 0, 9, 0, 2, 0, 0], 
         [0, 5, 0, 0, 0, 7, 0, 0, 0], 
         [0, 0, 0, 0, 4, 5, 7, 0, 0], 
         [0, 0, 0, 1, 0, 0, 0, 3, 0], 
         [0, 0, 1, 0, 0, 0, 0, 6, 8], 
         [0, 0, 8, 5, 0, 0, 0, 1, 0],
         [0, 9, 0, 0, 0, 0, 4, 0, 0]]

#this funtion verifies that the given sudoku matrix is solved, this is the end condition.
def find(matrix):
    
    for i in range(len(matrix)): #sorts through all the rows
        for j in range(len(matrix[i])): #sorts through all the columns
            if matrix[i][j] == 0: #Verifies if it's still empty
                
                return False
    return True


def sudoku_solver (matrix): #this is the main funtion that backtracks until the solution is found
    
    finished = find(matrix) #uses the find algo to find out if the sudoku is solved
    if finished:
       # Sudoku solved, print the matrix
       for row in matrix:
           print(row)
       return True
            
    else:
        
        for i in range(9): #sorts all the rows of the matrix 
            for j in range(9): #sorts all the columns of the matrix 
                if matrix[i][j] ==0: #verifies if the given position is empty
                    for k in (range(1,10)): #Tries a number between 1-9
                        valid= valid_pos_n_num(matrix, i, j, k)
                        if valid: #verifies if the given number is valid in that position
                            matrix[i][j] = k #inserts the number in the given title
                            if sudoku_solver(matrix): #Backtracks the main funtion
                                return True
                            else:
                                matrix[i][j] = 0 #Cleans the given title title when backtraking
                    return False        
                    
time_start = time.time()  #start time           

sudoku_solver(matrix) #Solves the sudoku riddle

time_finished = time.time() - time_start #finnish time

print ('Elapse time: ',time_finished, 's') #prints the elapse time