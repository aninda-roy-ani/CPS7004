import numpy as np

X_train = np.array([
    [5, 3, 0, 2],
    [4, 0, 0, 5],
    [2, 5, 0, 3],
    [0, 3, 4, 0]
])

Y_train = np.array([
    'user1',
    'user2',
    'user3',
    'user4'
])

X_test = np.array([
    [5, 3, 0, 2],
    [4, 0, 2, 0]
])


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))


def knn_recommend(X_train, Y_train, X_test, k):
    predictions = []
    for test in X_test:
        distances = [euclidean_distance(test, train) for train in X_train]
        k_nearest_neighbours = np.argsort(distances)[:k]
        k_nearest_users = Y_train[k_nearest_neighbours]
        unique, counts = np.unique(k_nearest_users, return_counts=True)
        most_common_user = unique[np.argmax(counts)]
        predictions.append(most_common_user)

    return predictions


reco = knn_recommend(X_train, Y_train, X_test, 2)
print(reco)

