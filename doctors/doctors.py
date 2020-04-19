class Doctors:

    def visit_details(self):
        offices, numbers = self.timetable()
        return len(offices) * len(numbers)
