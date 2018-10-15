class Difference:
    def __init__(self, a):
        self.__elements = a
        # Add your code here
        self.maximumDifference = 0
    def computeDifference(self):
        # Nested traversal of array elements for max difference.
        for elem1 in self.__elements:
            for elem2 in self.__elements:
                if elem2 is elem1: # Skip computing difference on element with itself
                    pass
                current_difference = abs(elem1 - elem2) #absolute value
                if current_difference > self.maximumDifference:
                    self.maximumDifference = current_difference          
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)