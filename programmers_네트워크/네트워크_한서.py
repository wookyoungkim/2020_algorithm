def solution(n, computers):
    ret = 0
    visited = [0] * n
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        ret += 1
        
        q = []
        q.append(i)
        while q:
            curr = q.pop(0)
            for nex in range(n):
                if curr == nex or visited[nex]:
                    continue
                if computers[curr][nex]:
                    visited[nex] = 1
                    q.append(nex)
        
    return ret
