class Cyclus:
    \"\"\"Encapsulates the 6->9->3 sequential SCM logistics flow.\"\"\"
    def __init__(self):
        self.flow = [\"Station 6 (AmRest)\", \"Station 9 (SuperDrob)\", \"Station 3 (Retail)\"]
        self.current_step = 0

    def process_next(self):
        if self.current_step < len(self.flow):
            step = self.flow[self.current_step]
            self.current_step += 1
            return step
        return None

    def reset(self):
        self.current_step = 0
