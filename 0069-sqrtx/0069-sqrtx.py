
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:return None
        if x==0:return 0
        # guess the fisrt step
        guess=x/2.0
        while True:
            next_guess=(guess + x/guess)/2
            #  if the guess is barely changing we found it
            if abs(guess-next_guess)<0.000001:
                break
            guess=next_guess
        return int(guess)
        







        