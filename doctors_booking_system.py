from pprint import pprint
from visit import Visit
# from doctors import Neurologist, Cardiologist
from specialists import *
from helpers import *


def get_doctors_visit():
    neurologist = Neurologist()
    # print(neurologist.visit_details())
    cardiologist = Cardiologist()
    # print(cardiologist.visit_details())
    f = Visit("FRI1203", neurologist)
    f.allocate_patient("Jan M.", "2B")
    f.allocate_patient("Alina Z.", "3E")
    f.relocate_patient("2B", "2E")
    f.relocate_patient("3E", "2D")
    # print(f.visit_time)
    # print(f.get_day())
    # print(f.get_date())
    # print(f.get_specialist())
    pprint(f.numbers)
    print(f.get_empty_terms())
    printer("Jan Kowal", "6C", "Cardiologist", "FRI1203")
    f.print_visit_details(printer)


get_doctors_visit()
