class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #edge case 
        if numRows ==  1 or numRows>=len(s):
            return s
        #create a list for each rows
        rows=[""] * numRows
        current_row=0
        going_down=False
        for char in s:
            rows[current_row]+=char
            #change the direction  at the first and the last row
            if current_row==0 or current_row==numRows-1:
                going_down= not going_down
            #move up or move down
            if going_down:
                current_row +=1
            else:
                current_row -=1
        return "".join(rows)

        