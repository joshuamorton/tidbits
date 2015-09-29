from collections import defaultdict
from math import sqrt

class CollabFilter():
    def __init__(self):
        self.cf = defaultdict(dict)

    def setRating(self, user, film, rating):
        self.cf[user][film] = float(rating)

    def setUser(self, user):
        self.cf[user] = {}

    def getRating(self, user, film):
        return self.cf[user][film]

    def rate(self, user, film):
        other_users = set(self.cf.keys()) - {user}
        filmsRated = set(self.cf[user].keys())
        films = {other: set(self.cf[other].keys()) & filmsRated for other in other_users}
        top = {other: sum(self.cf[user][film] * self.cf[other][film] for film in films[other]) for other in other_users}
        left = {other: sum(self.cf[other][film] ** 2 for film in films[other]) for other in other_users}
        right = {other: sum(self.cf[user][film] ** 2 for film in films[other]) for other in other_users}
        similarities = {other: top[other] / (sqrt(left[other]) * sqrt(right[other])) for other in other_users}
        k = 1/ sum(similarities.values())
        return k * sum(similarities[other] * self.cf[other][film] for other in other_users)
