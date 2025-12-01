from platform import Platform
from spreading_behavior import will_share


class Instagram(Platform):
    """
    Instagram:
    - More curated, slower spread
    - Reduces fake news via a smaller platform factor
    """

    def __init__(self, users):
        super().__init__("Instagram", users)
        self.platform_factor = 0.85  # more selective, less viral

    def seed_news(self, news, initial_users):
        # Instagram shows news to a smaller initial audience
        cutoff = int(len(initial_users) * 0.6)
        for user in initial_users[:cutoff]:
            self.feed[user.id].append(news)
            self._mark_seen(user, news)

    def step(self):
        # Each user checks their feed and decides whether to reshare
        for user in self.users:
            if not self.feed[user.id]:
                continue

            feed_copy = self.feed[user.id].copy()
            self.feed[user.id] = []  # clear after reading

            for news in feed_copy:
                if will_share(user, news, self.platform_factor):
                    self._share_news(user, news)
