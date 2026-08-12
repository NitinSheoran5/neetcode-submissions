class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myArr = []
        sum = 0
        for x in operations:
            match x:
                case "+":
                    n = len(myArr)
                    myArr.append(myArr[n-1]+myArr[n-2])
                case "C":
                    myArr.pop()
                case "D":
                    myArr.append(myArr[len(myArr)-1]*2)
                case _:
                    myArr.append(int(x))
        for x in myArr:
            sum = sum + x
        
        return sum
