class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
    
        ans=''
        while columnNumber > 0:
            columnNumber-=1
            val = columnNumber % 26
            columnNumber = (columnNumber)//26
            ans=chr(65+val)+ans
        return ans
