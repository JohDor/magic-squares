#magic square generator
size_of_matrix = int(input("Enter size of matrix:  "))
matrices = [i for i in range (1, size_of_matrix**2+1)]
random.shuffle(matrices)
print(matrices)
def split_list(the_list, chunk_size):
    result_list = []
    while the_list:
        result_list.append(the_list[:chunk_size])
        the_list = the_list[chunk_size:]
    return result_list
newLists=split_list(matrices, size_of_matrix)
print(newLists)
print("")
# Python3 program to check whether a given
# matrix is magic matrix or not
# Returns true if mat[][] is magic
# square, else returns false.
def isMagicSquare(mat):
    # calculate the sum of
    # the prime diagonal1
    s = 0
    for i in range(0, N):
        s = s + mat[i][i]
    # the secondary diagonal
    s2 = 0
    for i in range(0, N):
        s2 = s2 + mat[i][N - i - 1]
    if (s != s2):
        return False
    # For sums of Rows
    for i in range(0, N):
        rowSum = 0;
        for j in range(0, N):
            rowSum += mat[i][j]
        # check if every row sum is
        # equal to prime diagonal sum
        if (rowSum != s):
            return False
    # For sums of Columns
    for i in range(0, N):
        colSum = 0
        for j in range(0, N):
            colSum += mat[j][i]
        # check if every column sum is
        # equal to prime diagonxal sum
        if (s != colSum):
            return False
    return True

N = len(newLists)
if (isMagicSquare(newLists)):
    print("Magic Square")
else:
    print("Not a magic Square")
