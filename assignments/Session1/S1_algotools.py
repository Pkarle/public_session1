##
#
# @author Alexandre Benoit, LISTIC Lab, IUT Annecy le vieux, FRANCE
# @brief a set of generic functions for data management

"""
# a variable
a=1 # default type : int

# an empty list
mylist = []

#a filled list
mylist2=[1,2,3]

#append to a list
mylist.append(10)

# a buggy list
mybuggylist=[1,'a', "Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""

def average_above_zero(tab):
    """
    brief: computes teh average of ...
    Args:
        tab: a list of numeric value
    Return: 
        The computed average
    Raises:
        ValueError if no positive value is found
    """
    if not(isinstance(tab, list)):
        raise ValueError('Expected a list as input')
    average = -99
    valSum = 0.0
    nPositiveValues = 0
    NMAX = len(tab)
    for idx in range(NMAX):
        if tab[idx] > 0:
            valSum = valSum + float(tab[idx])
            nPositiveValues = nPositiveValues + 1

    if nPositiveValues <= 0:
        raise(ValueError('No positive value found'))
    average = valSum / nPositiveValues
    return average

tab = [1, 2, 3, 4, -5]

moy = average_above_zero(tab)
print('Positive values average = ' + str(moy))
print('Positive values average = '.format(v=moy))


def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    if input_list == 0:
        raise ValueError('Empty list given')

    maxVal = 0
    maxIndex = 0
    for idx in range(len(input_list)):
        if maxVal < input_list[idx]:
            maxVal = input_list[idx]
    
    return maxVal, maxIndex

maxList = [1, 8, 18, 287, 23]

print(max_value(maxList))