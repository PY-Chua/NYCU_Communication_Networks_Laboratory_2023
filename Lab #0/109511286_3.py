def min_money_needed(a_n, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in a_n:
        for j in range(i, amount + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)
    return dp[amount]

n_sets = int(input())
nlist=[]
for i in range(n_sets):
    N_S = list(map(int, input().split()))
    a_n = list(map(int, input().split()))
    nlist.append(min_money_needed(a_n, N_S[1]))
print(*nlist, sep="\n")