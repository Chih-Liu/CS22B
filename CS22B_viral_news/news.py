class News:
    def __init__(self, news_id, title, category, text, is_fake, base_virality):
        self.news_id = news_id
        self.title = title
        self.text = text
        self.is_fake = is_fake
        self.base_virality = base_virality

    def __str__(self):
        return f"[{self.news_id}] {self.title} (fake = {self.is_fake})"