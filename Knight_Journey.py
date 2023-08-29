def creaMatriz(n,m):
 ''' 
 This funtion creates an empty matrix filled with 0.
 @param n : Number of rows.
 @param m : Number of colummns.
 @type n: int
 @type m: int
 @return: It returns and n*m matrix filled with 0
 @rtype: Matrix (list of list)
 '''
 matriz = []
 for i in range(n):
     a = [0]*m
     matriz.append(a)
 return matriz

#Creates a 8x8 matrix that resembles a chess board
matriz = creaMatriz(8, 8)

def knight_valid_move(x_initial,y_initial,x_end, y_end):
    '''
    Funtion that verifies that the inputed step is valid, based on the chess rules
    for the kight
    
    @param x_initial: Initial position of the knight in the x axis
    @param y_initial: Initial position of the knight in the y axis
    @param x_end: Inputed position in the x axis
    @param y_end: Inputed position in the y axis
    @returns: True if conditions are metted and False otherwise
    '''
    #Don't account for the negative values, this happens because the knight
    ##can move backwards
    mov_abs_x = abs(x_initial-x_end) 
    mov_abs_y = abs(y_initial-y_end)
    
    #based on the chess rules the knight always move 3 titles, and the "!0" 
    ##prevents the kight to move the 3 titles in a straight line.. 
    return mov_abs_x + mov_abs_y == 3 and mov_abs_x != 0 and mov_abs_y != 0
        

def knight_jorney(matriz, x_ini, y_ini, jorney, index):
    """
    This is the main funtion and it's the one that backtracks until the correct solution in found'

    Parameters
    ----------
    matriz : Matrix
        This is the inputed matrix that resembles the chess board, it has to be empty.
    x_ini : integer
        Starting position of the knight in the x axis.
    y_ini : integer
        Starting position of the knight in the x axis.
    jorney : List
        This varible tracks the jorney of the knight through all the titles that were visited.
    index : integer
        This variable tracks the completion rate of the the problem.

    Returns
    -------
    TYPE: Matrix
        It returns the inputed matrix filled with numbers with the steps taken by the knight 
        in order to sort all the chess board without repeting titles and following the chess rules.

    """
    matrix_area = len(matriz) ** 2 #The area of any given square is the 2 square of it.
    
    if index > matrix_area:  # End contition of the algorithm
        for i in range(8): 
            print(matriz[i]) # This part prints the matrix in an easier way to visualize the result
        return 
    
    else:
           for i in range(len(matriz)): #Sorts all the rows of the matrix
                for j in range(len(matriz)): #Sorts all the columns of the matrix
                    new_pos = [i,j] #gives a possible new position
                    #Runs the valid algorithm to verify the new suggested step
                    valid = knight_valid_move(x_ini, y_ini, new_pos[0], new_pos[1])
                    #verifies if the new position is valid, the new position is not used and the matrix
                    #title is not used.
                    if valid and new_pos not in jorney and matriz[i][j]<1:
                        jorney.append(new_pos[::]) #Append the new valid move to the jorney
                        x_ini = new_pos[0]
                        y_ini = new_pos[1]
                        matriz[i][j] = index #Assigns that title the step number
                        if knight_jorney(matriz, x_ini, y_ini, jorney, index + 1): #Backtraks the main funtion
                            return True
                        matriz[i][j] = 0 #Returns the previous used title to 0 (empty)
                        jorney.pop() # Removes that title from the jorney list.


knight_pos = [2,2] #Posicion incial del caballo       

#Try the funtion
knight_jorney(matriz, knight_pos[0], knight_pos[1], [], 1)
