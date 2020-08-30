##################################################
# PROBLEM 1: Filtering even numbers
##################################################
# Fill in the body of the following function, evens_only.
# The function takes one argument, a list of numbers (float 
# or integer). You should write code so that evens_only 
# returns a list containing only the even, integer valued
# numbers from this list. The returned list must also 
# satisfy the following conditions:
#   1) The data type of all numbers in the returned list
#      should be Integer.
#   2) The numbers in the returned list should be in the 
#      same order as in input_list.
#
# For example, evens_only([1,2,2.5,3,4]) should return the 
# list [2,4].

def evens_only(input_list):
	even_nos = [num for num in input_list if num % 2 == 0]
	print("Even numbers in the list: ", even_nos) 
    ### Add your code here ###

##################################################
# PROBLEM 2: Piecewise function
##################################################
# Fill in the body of the function piecewise that takes 
# a single float argument and returns the function 
# defined in the assignment handout, F(x). The data 
# type of the retruned value should be float.

def piecewise(x):
    if x<0:
        return -1
    elif 0<=x<2:
        return 3*(x**2)
    else:
        return -x
    ### Add your code here ###
    
##################################################
# PROBLEM 3: Character count
##################################################
# Fill in the body of the function character_count.
# character_count takes a string file_path, reads in 
# the text file at file_path as a string, and counts the 
# number of times each alphabetic character (a 
# through z) appears in the file. character_count
# should return a dictionary that maps each letter
# that appears at least once in the string to its 
# count. The keys of this dictionary should have type 
# string and the values should have type int.

def character_count(input_string):
    dict={}
    for n in input_string:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
    ### Add your code here ###
