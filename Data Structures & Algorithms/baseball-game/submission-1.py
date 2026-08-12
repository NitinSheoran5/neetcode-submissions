class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myArr = []
        sum = 0
        for x in operations:
            match x:
                case "+":
                    n = len(myArr)
                    ans = myArr[n-1]+myArr[n-2]
                    myArr.append(ans)
                    sum = sum + ans
                case "C":
                    ans = myArr.pop()
                    sum = sum - ans
                case "D":
                    ans = myArr[len(myArr)-1]*2
                    myArr.append(ans)
                    sum = sum + ans
                case _:
                    myArr.append(int(x))
                    sum = sum + int(x)
        
        return sum
