def solution(begin, target, words):
    global ret
    ret = 51
    if target not in words:
        return 0
    
    length = len(begin)
    n = len(words)
    visited = [0] * n
    def dfs(i, cnt):
        global ret
        visited[i] = 1
        if words[i] == target:
            ret = min(ret, cnt)
            return
        for j in range(n):
            if visited[j]:
                continue
            visited[j] = 1
            diff = 0
            for k in range(length):
                if words[i][k] != words[j][k]:
                    diff += 1
            if diff == 1:
                dfs(j, cnt+1)
            visited[j] = 0
        visited[i] = 0
    
    
    for i in range(n):
        tmp = 0
        for j in range(length):
            if words[i][j] != begin[j]:
                tmp += 1
        if tmp == 1:
            dfs(i, 1)
                
    return ret

