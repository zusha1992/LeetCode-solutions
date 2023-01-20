# 1871. Jump Game VII
# https://leetcode.com/problems/jump-game-vii/description/
from collections import deque
def canReach(s, minJump, maxJump):
    q, farthest = deque([0]), 0
    while q:
        i = q.popleft()
        start = max(i + minJump, farthest + 1)
        for j in range(start, min(len(s), i + maxJump + 1)):
            if s[j] == '0':
                q.append(j)
                if j == len(s) - 1:
                    return True
        farthest = i + maxJump
    return False


# https://leetcode.com/problems/jump-game-iii/
# 1306. Jump Game III
# Time Complexity - O(n).
# Memory - O(n).
def canReach(self, arr: List[int], start: int) -> bool:
  visited = [False] * len(arr)
    left, right = 0, len(arr) - 1
    neighbors = deque([start])
    while neighbors:
        i = neighbors.popleft()
        if arr[i] == 0:
            return True
        else:
            visited[i] = True
        jump_forword, jump_backwords = i + arr[i], i - arr[i]
        if left <= jump_forword <= right and not visited[jump_forword]:
            neighbors.append(jump_forword)
        if left <= jump_backwords <= right and not visited[jump_backwords]:
            neighbors.append(jump_backwords)
    return False
