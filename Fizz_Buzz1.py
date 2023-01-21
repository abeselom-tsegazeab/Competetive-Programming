class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        me =[]
        for i in range(1,n+1):
            if i % 3 ==0 and i % 5 ==0:
                me.append("FizzBuzz")
            elif i % 3 ==0:
                me.append("Fizz")
            elif i % 5 ==0:
                me.append("Buzz")
            else:
                me.append(str(i))
        return me


