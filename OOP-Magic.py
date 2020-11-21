class Title:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"-= {self.title.upper()} =-"


t1 = Title("Programming in Python 3")

print(t1)