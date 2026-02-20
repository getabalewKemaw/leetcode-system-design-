class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # first convert the the binary to integer of base2
        sum_integer=int(a,2)+int(b,2)
        # then return back to the binary values
        # we start from the second since we do not want those as well
        return bin(sum_integer)[2:]



        