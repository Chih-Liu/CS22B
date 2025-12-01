from platform import Platform
from spreading_behavior import will_share


class Twitter(Platform):
    """
    Twitter:
    - Fast & engagement-driven
    - Boosts sharing more than other platforms
    """

    def __init__(self, users):
        super().__init__("Twitter", users)
        self.platform_factor = 1.15

    def seed_news(self, news, initial_users):
        # Twitter pushes breaking news widely
        for user in initial_users:
            self.feed[user.id].append(news)
            self._mark_seen(user, news)

    def step(self):
        for user in self.users:
            if not self.feed[user.id]:
                continue

            feed_copy = self.feed[user.id].copy()
            self.feed[user.id] = []

            for news in feed_copy:
                if will_share(user, news, self.platform_factor):
                    self._share_news(user, news)
