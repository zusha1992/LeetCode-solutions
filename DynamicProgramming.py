
# https://leetcode.com/problems/jump-game/
def jump1(nums):
    if len(nums) == 1:
        return True
    target = len(nums) - 1
    dp = [False] * len(nums)
    dp[-1] = True
    for i in range(target - 1, -1, -1):
        for j in range(i + 1, i + nums[i]+1):
            if dp[j] == True:
                dp[i] = True
                break
    return dp[0]

# https://leetcode.com/problems/jump-game-ii/
def jump2(nums):
    if len(nums) == 1:
        return 0
    target = len(nums) - 1
    dp = [0] * (len(nums))
    dp[-1] = 1
    for i in range(target - 1, -1, -1):
        if i + nums[i] >= target:
            dp[i] = 1
        else:
            tmp_list = list(filter(lambda x: x != 0,dp[i + 1: i + nums[i] + 1]))
            if tmp_list:
                dp[i] = 1 + min(tmp_list)
    return dp[0]