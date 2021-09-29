class timesheet:
      def __init__(self, date ,hrs,activity,description,status):
          self.date = date
          self.hrs  = hrs
          self.activity = activity
          self.description = description
          self.status = status


      def display(self):
          print(self.hrs)
t=timesheet("2/5/2021", "10hrs","testing","idk","active")
t.display()


