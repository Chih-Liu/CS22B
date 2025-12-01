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
            interests = {"politics", "health", "meme"}
            gullibility = random.uniform(0.2, 0.8)
            skepticism = random.uniform(0.2, 0.8)
            users.append(User(i, interests, gullibility, skepticism))
        return users


    def create_platforms(self):
        return [
            Twitter(self.users),
            Instagram(self.users),
            Tiktok(self.users)
        ]

    def create_fake_news(self):
        return [
            News(1, "Breaking A", "politics", "some text", "real", 0.5),
            News(2, "Fake B", "health", "fake text", "fake", 0.8),
            News(3, "Meme C", "meme", "funny text", "real", 0.9),
        ]
    
    def run_single_news_on_platform(self, news, platform, steps=5):
        seeds = random.sample(self.users, k=10)
        platform.seed_news(news, seeds)

        for _ in range(steps):
            platform.step()

        total_share = platform.get_total_shares(news.news_id)
        reach = platform.get_reach(news.news_id)
        return total_shares, reach 
        

    def run(self):
        for news in self.news_list:
            print(f"\n=== Spreading: {news.title} ===")
            for platform in self.platforms:
                total_shares, reach = self.run_single_news_on_platform(news, platform)
                print(f"{platform.name} -> Shares: {platform.shares}, Reach: {reach}")


if __name__ == "__main__":
    sim = NewsSimulator()
    sim.run()
