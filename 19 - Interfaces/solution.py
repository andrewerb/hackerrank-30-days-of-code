""" Day 19: Interfaces
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic): #custom class
    def divisorSum(self, n):
        # sum of all divisors of n
        divisor_list = list()
        for divisor in range(1, n): #(range from 1 to n-1)
            if n % divisor == 0:
                divisor_list.append(divisor)
        
        divisor_sum = n
        for item in divisor_list:
            divisor_sum += item
        #print (str(divisor_list))
        return divisor_sum
            


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
