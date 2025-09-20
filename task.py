from datetime import datetime

class UnitTask():
    def __init__(self, reminder, task_name):
        self.reminder = reminder
        self.task_name = task_name
        self.issubmitted = False

    def remindme(self):
        now = datetime.now()

        exact_time = now.strftime("%I:%M %p")
        if self.reminder == exact_time:
            return True
        return False
    
    def submit(self):
        self.issubmitted = True


