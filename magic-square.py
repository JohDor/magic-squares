import random
size_of_matrix = int(input("Enter size of matrix:  "))
magic = False
matrices = [i for i in range (1, size_of_matrix**2+1)]
print(matrices)
def split_list(the_list, chunk_size):
    result_list = []
    while the_list:
        random.shuffle(the_list)
        result_list.append(the_list[:chunk_size])
        the_list = the_list[chunk_size:]
    random.shuffle(result_list)
    return result_list
h=split_list(matrices, 5)
print(h)
newLists = split_list(matrices, size_of_matrix)
magicValue = size_of_matrix*(size_of_matrix*size_of_matrix+1)/2
columnMatrix = [[] for x in range(size_of_matrix)]
def isMagicSquare(mat):
    s = 0
    for i in range(0, size_of_matrix):
        s = s + mat[i][i]
    s2 = 0
    for i in range(0, size_of_matrix):
        s2 = s2 + mat[i][size_of_matrix - i - 1]
    if (s != s2):
        return False
    for i in range(0, size_of_matrix):
        rowSum = 0;
        for j in range(0, size_of_matrix):
            rowSum += mat[i][j]
        if (rowSum != s):
            return False
    for i in range(0, size_of_matrix):
        colSum = 0
        for j in range(0, size_of_matrix):
            colSum += mat[j][i]
        if (s != colSum):
            return False
    return True
print(newLists)
g=True
g=isMagicSquare(newLists)
# print(h)
if g == False:
    isMagicSquare(newLists)
    print("Not Magic")
else:
    print("Magic")

#ask for primes
p = int(input("How many primes?  "))
#counts for primes
counts = 2
#counts for iterations
nums=2
while(counts<=p+1):
    count = 0
    i=2
    while(i<= nums//2):
        if (nums % i == 0):
            count += 1
            break
        i+=1
    if (count == 0 and nums != 1 ):
        print(" %d" %nums, end = ' ')
        counts += 1
    nums += 1
print(" ")
def isPrime(n):
    prime = True
    for i in range(2, n):
        if (n%i==0):
            prime=False
            break
        else:
            prime=True
    return prime
h=isPrime(int(input("Enter a number:  ")))
print(h)


for i in range(2, 101):
    h = isPrime(i)
    if h == True:
        print(' %d ' %i, end = ' ')
