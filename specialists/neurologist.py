from doctors import Doctors

class Neurologist(Doctors):
    @staticmethod
    def get_name():
        return "Neurologist"

    @staticmethod
    def timetable():
        return range(1, 4), "ABCDEGHI"
