import numpy as np

####################################################
# Problem 1: Classes
####################################################


class Course:
    def __init__(self, course_number):
        ## Add code here ##
        pass
        
    def get_course_number(self):
        ## Add code here ##
        pass
        
    def add_student(self, student):
        ## Add code here ##
        pass
        
    def drop_student(self,student_id):
        ## Add code here ##
        pass
        
    def get_roster(self):
        ## Add code here ##
        pass

####################################################
# Problem 2: Data filtering
####################################################


class DataFiltering:
    def __init__(self):
        self.data = np.loadtxt("boston.csv", delimiter=',')

    def get_percent_nan(self):
        ## Add code here for question 2.1 ##
        pass

    def count_nan_per_column(self):
        ## Add code here for question 2.2 ##
        pass

    def average_columns_ignoring_nan_rows(self):
        ## Add code here for question 2.3 ##
        pass

####################################################
# Problem 3: Data exploration
####################################################


class DataExploration:
    def __init__(self):
        self.data = np.loadtxt("iris.csv", delimiter=',', skiprows=1)

    def sepal_measurements_for_biggest_petals(self):
        ## Add code here for question 3.1 ##
        pass

    def max_values_per_column_in_znorm(self):
        ## Add code here for question 3.2 ##
        pass
