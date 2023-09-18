def solution(N, A, B):
    # Implement your solution here
    graph = dict.fromkeys(range(N), 0)

    seconds = 0
    vertex = []
    for i in range(len(A)):
        vertex.append((A[i],B[i]))
    while True:
        for i in range(len(A)+1):
            for c in vertex:
                if i in c:
                    graph[i] += 1
        vertex1 = vertex
        for i in graph:
               if graph[i] <= 1:
                   vertex = list(filter(lambda x: x[1] != i and x[0] != i, vertex))

        if len(vertex) == len(vertex1):
            for i in range(N):
                if i not in A or i not in B:
                    return seconds + 1
                    break
                
            return seconds 
            break
        
        seconds += 1

## Time complexity = O(n^2)