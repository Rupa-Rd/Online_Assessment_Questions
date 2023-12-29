# Arrays and Queries (BNY Mellon Code Divas Diversity Challenge 2023)
# Given the array of length n denoting set of numbers and q denotes the number of queries
# The queries of three types:
# 1. l r : For each i with l <= i <= r a[i] = a[i]/d, where d is the smallest prime factor of a[i]
# 2. l r : Print the sum of all a[i] with l <= i <= r
# 3. i k : Set a[i] = k

# Input Format:
# -> The first line denotes n and q
# -> The second line contains n number of integers
# -> The third line contains q number of Queries in the above mentioned format

# Output Format:
# Print the values when the Query type 2 is called

# Sample Test Case:
# 5 3
# 10 2 8 7 6
# 2 1 4
# 1 1 4
# 2 1 4
# Output :
# 27
# 11

# Explanation:
# For Query [2 1 4] :
#   10 + 2 + 8 + 7 = 27
# For Query [1 1 4] :
#   [5 1 4 1 6]
# For Query [2 1 4] :
#   5 + 1 + 4 + 1 = 11

def solve(n,q,A,Q):
    for queries in Q:
        query_type = queries[0]
        l = queries[1]
        r = queries[2]
        if query_type == 1:
            query1(A,l,r)
        elif query_type == 2:
            query2(A,l,r)
        else:
            query3(A,l,r)
    

def query1(arr,s,e):
    for i in range(s-1,e):
        smallest_prime = prime(arr[i])
        arr[i] = arr[i] // smallest_prime
    # print(arr,end=' ')
def query2(arr,s,e):
    sum_of_arr = 0
    for i in range(s-1,e):
        sum_of_arr += arr[i]
    print(sum_of_arr)

def query3(arr,i,k):
    arr[i] = k

def prime(num):
    if num % 2 == 0:
        return 2
    i = 3
    while i * i <= num:
        if i % 1 == 0:
            return i
        i += 2
    return num
def main():
    # For user input uncomment the below code
    # n,q = map(int,input().split(' '))
    # A = list(map(int,input(' ')))[:n]
    # Q = []
    # for i in range(q):
    #     temp = list(map(int,input().split(' ')))[:3]
    #     Q.append(temp)
    n = 5
    q = 3
    A = [10,2,8,7,6]
    Q = [[2,1,4],[1,1,4],[2,1,4]]
    solve(n,q,A,Q)
    

if __name__ == '__main__':
    main()