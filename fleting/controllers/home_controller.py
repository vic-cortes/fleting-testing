class HomeController:
    def __init__(self, model=None):
        self.model = model

    def get_title(self):
        return "Home"
