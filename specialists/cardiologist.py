from doctors import Doctors

class Cardiologist(Doctors):
    @staticmethod
    def get_name():
        return "Cardiologist"

    @staticmethod
    def timetable():
        return range(4, 8), "ABCDEG"

