import numpy as np
import numpy.linalg as la
from sklearn.linear_model import LinearRegression
import unittest

############################################################
# Problem 1: Gauss-Jordan Elimination
############################################################

# def gauss_jordan(A):
#     ## Add code here ##
#     n = A.shape[0]
#
#     # for every row k, up to n
#     for k in range(n):
#         # TODO: Perform some swap
#         # Check if A_i*k element is 0
#         if A[i_star, k] == 0:
#             return None
#         # TODO: Reduce below diagonal
#         for j in range(k+1, n):
#             # TODO: Calculate f
#             f = A[j,k]/A[k,k]
#             # TODO: A_j = A_j - fA_k
#
#     for ...:
#     return -1

def gauss_jordan(A):
    ## Add code here ##

    n = A.shape[0]

    # A = np.hstack((A,np.eye(n)))
    B = np.eye(n)

    for k in range(n):

        i = np.argmax(abs(A[k:, k])) + k

        if A[i, k] == 0:
            print("Matrix is not invertible")

            return  # after this,return to the k-loop

        A[[k, i], :] = A[[i, k], :]  # swap rows k and i if the matrix is not invertible

        B[[k, i], :] = B[[i, k], :]  # also swap the same rows in the identity matrix

        # elimination of all entries below the diagonal

        for j in range(k + 1, n):
            f = A[j, k] / A[k, k]

            A[j, :] = A[j, :] - f * A[k,
                                    :]  # substract a scaled version of row k from j so that the kth column in j is o

            B[j, :] = B[j, :] - f * B[k, :]

    for k in range(n)[::-1]:

        A[k, :] = A[k, :] / A[k, k]  # scale the row so that the diagonal entry = 1

        B[k, :] = B[k, :] / A[k, k]

        # elimination of all entries above the diagonal

        for j in range(k)[::-1]:
            f = A[j, k] / A[k, k]

            A[j, :] = A[j, :] - f * A[k, :]

            B[j, :] = B[j, :] - f * B[k, :]

    return B


############################################################
# Problem 2: Ordinary Least Squares Linear Regression
############################################################

def linear_regression_inverse(X,y):
    ## Add code here ##
    return -1
    
def linear_regression_moore_penrose(X,y):
    ## Add code here ##
    return -1
    
def generate_data(n,m):
    """
        Generates a synthetic data matrix X of size n by m
        and a length n response vector.

        Input:
            n - Integer number of data cases.
            m - Integer number of independent variables.

        Output:
            X - n by m numpy array containing independent variable
                observasions.
            y - length n numpy array containg dependent variable
                observations.
    """
    X = np.random.randn(n, m)
    beta = np.random.randn(m)
    epsilon = np.random.randn(n)*0.5
    y = np.dot(X, beta) + epsilon

    return X, y


if __name__=="__main__":
    # test gauss-jordan elimination
    # X = np.random.randn(3, 3)
    X = np.array([[1,3],[2,5]], dtype=np.float64)
    print("running gauss jordan")
    print(np.allclose(gauss_jordan(X), la.inv(X)))

    # test linear regression
    X, y = generate_data(10, 3)
    lr = LinearRegression(fit_intercept=False)
    lr.fit(X, y)
    beta = lr.coef_
    print(np.allclose(linear_regression_inverse(X, y), beta))
    print(np.allclose(linear_regression_moore_penrose(X, y), beta))
