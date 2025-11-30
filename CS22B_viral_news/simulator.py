from user import User
from news import News
from twitter import Twitter
from instagram import Instagram
from tiktok import Tiktok

import random

class NewsSimulator:
    def __init__(self):
        self.users = self.create_users()
        self.platforms = self.create_platforms()
        self.news_list = self.create_fake_news()

    def create_users(self):
        users = []
        for i in range(500):
            share_prob = random.uniform(0.05, 0.3)
            credulity = random.random()
            users.append(User(i, share_prob, credulity))
        return users

    def create_platforms(self):
        return [
            Twitter(self.users),
            Instagram(self.users),
            Tiktok(self.users)
        ]

    def create_fake_news(self):
        return [
            News(1, "Breaking A", "politics", "some text", False, 0.5),
            News(2, "Fake B", "health", "fake text", True, 0.8),
            News(3, "Meme C", "meme", "funny text", False, 0.9)
        ]

    def run(self):
        for news in self.news_list:
            print(f"\n=== Spreading: {news.title} ===")
            for platform in self.platforms:
                platform.spread_news(news)
                print(f"{platform.name} -> Views: {platform.views}, Shares: {platform.shares}")


if __name__ == "__main__":
    sim = NewsSimulator()
    sim.run()
