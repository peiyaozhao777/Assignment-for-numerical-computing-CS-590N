import numpy as np
import math
import random
from collections import Counter
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans


def select_most_common_label(label_list):
    # Counter creates a dictionary that maps each value to the number of times it appears
    count_of_each_label = Counter(label_list)

    # Sort the labels in reverse order of frequency, breaking ties by selecting the larger label.
    labels = list([(x[1], x[0]) for x in count_of_each_label.items()])
    labels.sort(reverse=True)

    # Return the label only, for the label with the highest frequency
    return labels[0][1]


class KNNModel:
    def __init__(self, train_data, valid_data, test_data):
        # The final column contains the labels
        self.train_inputs = train_data[:, :-1]
        self.train_labels = train_data[:, -1]
        self.valid_inputs = valid_data[:, :-1]
        self.valid_labels = valid_data[:, -1]
        self.test_inputs = test_data[:, :-1]
        self.test_labels = test_data[:, -1]

    def make_predictions(self, inputs, k):
        # cdist returns an m x n matrix,
        # where m is the number of rows in ``inputs'' and
        # n is the number of rows in self.train_inputs.
        # dists[i, j] is the Euclidean distance from row i of ``inputs''
        # to row j of self.train_inputs.
        dists = cdist(inputs, self.train_inputs)
        all_predicted_labels = []
        for i in range(inputs.shape[0]):
            nn_idxs = ## TODO: Find the top k neighbors for inputs[i] (hint: use np.argsort on row i of ``dists'') ##
            nn_labels = ## TODO: Find the labels for the k nearest neighbors ##
            all_predicted_labels.append(select_most_common_label(nn_labels))

        return np.array(all_predicted_labels)

    def evaluate(self, inputs, true_labels, k):
        ## TODO: Call self.make_predictions for these inputs and k value to obtain the predicted labels ##
        ## TODO: Return the accuracy of the predicted labels (the fraction of predicted labels that match the ground truth labels in ``true_labels'') ##
        pass

    def select_k(self, k_options):
        ## TODO: For each k in k_options, call self.evaluate for the validation data ##
        ## TODO: Return the k value that gave the highest accuracy on the validation set ##
        pass


def get_kmeans_clusters(data, k):
    ## TODO: Create a kmeans model with n_clusters=k and random_state=0, then call fit on ``data'' ##
    ## TODO: return the labels_ from the kmeans model you just fit ##
    pass


###########################################
# Testing Code
###########################################
def load_iris_splits():
    random.seed(8)
    data = np.loadtxt("iris.csv", delimiter=',', skiprows=1)
    data_idxs = sorted([i for i in range(data.shape[0])], key=lambda x: random.random())
    num_train = math.floor(.7 * len(data_idxs))
    num_valid = math.floor(.15 * len(data_idxs))
    return data[data_idxs[:num_train]], \
           data[data_idxs[num_train:num_train+num_valid]], \
           data[data_idxs[num_train+num_valid:]]


if __name__=="__main__":
    train_data, valid_data, test_data = load_iris_splits()
    my_knn_model = KNNModel(train_data, valid_data, test_data)

    predictions_test = my_knn_model.make_predictions(my_knn_model.test_inputs, 5)
    print("Predictions on test set for k=5")
    print(predictions_test)

    acc_on_test = my_knn_model.evaluate(my_knn_model.test_inputs, my_knn_model.test_labels, 5)
    print("Accuracy on test set for k=5")
    print(acc_on_test)

    k = my_knn_model.select_k([3,5,7,9,11])
    print("Decided to use k=%d" % k)

    print("Test set performance with best k "
          "is %.4f" % my_knn_model.evaluate(my_knn_model.test_inputs, my_knn_model.test_labels, k))

    kmeans_data = train_data[:, :-1]
    print("K-means cluster assignments on iris:")
    print(get_kmeans_clusters(kmeans_data, 5))


