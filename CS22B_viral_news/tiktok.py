from platform import Platform
from spreading_behavior import will_share


class TikTok(Platform):
    """
    TikTok:
    - Highest virality boost
    - Algorithm pushes content aggressively
    """

    def __init__(self, users):
        super().__init__("TikTok", users)
        self.platform_factor = 1.30

    def seed_news(self, news, initial_users):
        # TikTok spreads news widely right away
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
