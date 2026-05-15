import sys
from operator import itemgetter 
import numpy as np

class KNN:
    def __init__(self, data):
        self.data = data

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def calculate_distance_between_users(self, user1, user2):
        """
        return euclidean distance between two users

        :param user1: string
        :param user2: string
        :return int - distance
        """
        return round(
            float(
                self.euclidean_distance(
                    np.array(self.data[user1]),
                    np.array(self.data[user2])
                )
            ),
            3
        )
    
    def add_user(self, name, coords):
        """
        :param name: String
        :param coords: List[int]
        """
        self.data[name] = coords
        print(self.data)

    def find_k_closest_neighbours(self, k, username):
        """
        :param k: Int
        :param username: String
        :return List[String]
        """
        distances = []
        for user in self.data:
            if user == username:
                continue
            distances.append(
                (
                    user,
                    self.calculate_distance_between_users(username, user)
                )
            )
        distances.sort(key=itemgetter(1))
        return distances[:k]
    
user_preferences = dict([
    ("Priyanka", [3, 4, 4, 1, 4]),
    ("Justine", [4, 3, 5, 1, 5]),
    ("Morpheus", [2, 5, 1, 3, 1]),
    ("Alina", [2, 3, 1, 5, 3])
])

knn = KNN(user_preferences)

username, k = sys.argv[1:]

if username is not None and k is not None:
    print(f'Closest {k} neightbors of the user {username} are:', knn.find_k_closest_neighbours(int(k), username))
