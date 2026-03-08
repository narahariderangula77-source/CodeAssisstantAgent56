class Memory:

    def __init__(self):
        self.history = []

    def add(self, user, response):
        self.history.append({
            "user": user,
            "response": response
        })

    def get(self):
        return self.history