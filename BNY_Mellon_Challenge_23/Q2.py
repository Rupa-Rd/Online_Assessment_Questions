# Arrays and Queries (BNY Mellon Code Divas Diversity Challenge 2023)
# Given the array of length n denoting set of numbers and q denotes the number of queries
# Queries

# 1. L X: Change the value of A[L] to X
# 2. L R X: Find the first index P such that A[P] <= X and L <= P <= R and 
# also print P for this type of Query. If there is no such P, Print -1.

# Input Format:
# -> The first line denotes n and q
# -> The second line contains n number of integers
# -> The third line contains q number of Queries in the above mentioned format

# Output Format:
# Print the values when the Query type 2 is called

# Sample Test Case:
# 10 4
# 12 71 80 22 48 13 75 81 68 52
# 2 1 10 27
# 1 2 49
# 1 3 26
# 2 2 10 7
# Output :
# 1
# -1

# Explanation:
# For Query [2 1 10 27] :
#   12 <= 27 -> Index = 1
# For Query [1 2 49] :
#   12 49 80 22 48 13 75 81 68 52
# For Query [1 3 26] :
#   12 49 26 22 48 13 75 81 68 52
# For Query [2 2 10 7]:
#   -1 Since no elements are <= 7

def solve(n,q,A,Q):
    for queries in Q:
        query_type = queries[0]
        l = queries[1]
        if query_type == 1:
            k = queries[2]
            query1(A,l,k)
        else:
            r = queries[2]
            k = queries[3]
            print(query2(A,l,r,k))
        
    

def query1(A,l,k):
    A[l] = k
def query2(A,l,r,k):
    for i in range(l-1,r):
        if A[i] <= k:
            return i +1
    return -1
def main():
    # For user input uncomment the below code
    # n,q = map(int,input().split(' '))
    # A = list(map(int,input(' ')))[:n]
    # Q = []
    # for i in range(q):
    #     temp = list(map(int,input().split(' ')))[:3]
    #     Q.append(temp)
    n = 10
    q = 4
    A = [12,71,80,22,48,13,75,81,68,52]
    Q = [[2,1,10,27],[1,2,49],[1,3,26],[2,2,10,7]]
    solve(n,q,A,Q)
    

if __name__ == '__main__':
    main()