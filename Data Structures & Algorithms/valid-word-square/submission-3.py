class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        r = len(words)
        n = 0
        for i in range(r):
            n = max(n, len(words[i]))
        n = max(n, r)
        for i in range(n):
            for j in range(i, n):
                x = "0"
                y = "0"
                try:
                    x = words[i][j]
                except Exception as e:
                    x = "-"
                try:
                    y = words[j][i]
                except Exception as e:
                    y = "-"
                print("x: " + x)
                print( "y: " + y)
                if x != y:
                    return False
        return True