def solution(A,X,Y):
    res = [] # To store the cost of the rehabilitation after Y days
    # Looping to store the cost after Y days
    for i in range(0,len(A),Y):
        res.append(A[i])
    m = len(res) # m denotes the length of the array
    # If the number of sessions (X) is equal to the length of res array
    if m == X:
        return sum(res) # return the sum of the cost of rehabilitation
    res.sort() # Else sort it in ascending order
    min_cost = 0
    # store the minimum cost of X sessions in min_cost
    for j in range(X):
        min_cost += res[j]
    return min_cost # return the result

## Time Complexity - O(n)