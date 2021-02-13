#A simple function to find the coordinates of an element our problem matrix
def index_loc(element,matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == element:
        return i,j


#Input interface with the user. 
def prog_input():
    print("Welcome to Armie's 8-puzzle solver!")
    val = int(input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle: "))
    while val != 1 and val != 2:
        val = int(input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle: "))
    if val == 2:
        print("Enter your puzzle, use a zero to represent the blank\n")
        userList1 = input("Enter the first row, use space or tabs between numbers: ")
        print("\n")
        userList2 = input("Enter the second row, use space or tabs between numbers: ")
        print("\n")
        userList3 = input("Enter the third row, use space or tabs between numbers: ")
        print("\n")
        return [[userList1],[userList2],[userList3]]
    elif val == 1:
        return [['1','2','3'],['4','8','0'],['7','6','5']]