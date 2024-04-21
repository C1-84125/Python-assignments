from datetime import datetime

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def accept_date(self):
        date_str = input("Enter the date in the format (dd/mm/yyyy): ")
        day, month, year = map(int, date_str.split('/'))
        if self.validate_date(day, month, year):
            self.day = day
            self.month = month
            self.year = year
        else:
            raise Exception("InvalidDate")

    def validate_date(self, day, month, year):
        try:
            datetime(year=year, month=month, day=day)
            return True
        except ValueError:
            return False

    def print_date(self):
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        print(f"Date: {self.day} {months[self.month-1]} {self.year}")

# Create an instance of the Date class
date = Date(0, 0, 0)

# Accept and validate the date
date.accept_date()

# Print the date
date.print_date()
