import numpy as np

####################################################
# Problem 1: Classes
####################################################


class Course:
    def __init__(self, course_number):
        self.course_number = course_number
        self.roster = []
        
    def get_course_number(self):
        return self.course_number
        
    def add_student(self, student):
        self.roster.append(student)
        
    def drop_student(self,student):
        if student in self.roster:
            self.roster.remove(student)
        
    def get_roster(self):
        return sorted(self.roster)
        
####################################################
# Problem 2: Data filtering
####################################################


class DataFiltering:
    def __init__(self):
        self.data = np.loadtxt("boston.csv", delimiter=',')

    def get_percent_nan(self):
        return np.mean(np.isnan(self.data))

    def count_nan_per_column(self):
        return np.sum(np.isnan(self.data), axis=0)

    def average_columns_ignoring_nan_rows(self):
        mask = np.any(np.isnan(self.data), axis=1) == False
        return np.mean(self.data[mask], axis=0)

####################################################
# Problem 3: Data exploration
####################################################


class DataExploration:
    def __init__(self):
        self.data = np.loadtxt("iris.csv", delimiter=',', skiprows=1)
        self.features = self.data[:, :4]
        self.labels = self.data[:, -1]

    def sepal_measurements_for_biggest_petals(self):
        petal_areas = np.pi * self.features[:, 2] * self.features[:, 3] / 4.0
        idxs = np.argsort(petal_areas)[-3:]
        return self.features[idxs, :2]

    def max_values_per_column_in_znorm(self):
        mu = np.mean(self.features, axis=0)
        sigma = np.std(self.features, axis=0)
        Z = (self.features - mu) / sigma
        return np.max(Z, axis=0)
