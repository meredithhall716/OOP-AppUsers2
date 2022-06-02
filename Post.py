class Post:
    def __init__(self, title, body, time):
        self.title = title
        self.body = body
        self.time = time
    
    def __str__(self):
        return f"title:{self.title}\n{self.body}\n{self.time}"