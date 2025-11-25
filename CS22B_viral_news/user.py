import random

class User:
    def __init__(self, user_id, share_prob):
        self.user_id = user_id
        self.share_prob = share_prob

    def decide_to_share(self, news):
        return random.random() < self.share_prob
        