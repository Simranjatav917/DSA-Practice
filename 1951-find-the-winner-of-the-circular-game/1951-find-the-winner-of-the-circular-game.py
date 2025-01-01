class Solution(object):
    def findTheWinner(self, n, k):
        winner = 0
        for i in range(1, n + 1):
            winner = (k + winner) % i
            
        return winner + 1