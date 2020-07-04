class Visit:
    def __init__(self, visit_time, doctors_room):
        self.visit_time = visit_time
        self.doctors_room = doctors_room

        offices, letters = self.doctors_room.timetable()
        self.numbers = [None] + [{letter: None for letter in letters} for __ in offices]

    def get_day(self):
        return self.visit_time[:3]

    def get_date(self):
        return self.visit_time[3:]

    def get_specialist(self):
        return self.doctors_room.get_name()

    def _parse_numbers(self, number="3B"):
        offices, letters = self.doctors_room.timetable()

        letter = number[-1]

        if letter not in letters:
            raise ValueError(f"Invalid letter {letter}")

        office_text = number[:-1]
        try:
            office = int(office_text)
        except ValueError:
            raise ValueError(f"Invalid office number {office_text}")

        if office not in offices:
            raise ValueError(f"Office {office} is out of range")

        return office, letter

    def allocate_patient(self, patient="Anna Z.", number="3B"):
        office, letter = self._parse_numbers(number)

        if self.numbers[office][letter] is not None:
            raise ValueError(f"Term {number} is already taken")

        self.numbers[office][letter] = patient

    def relocate_patient(self, number_from, number_to):
        office_from, letter_from = self._parse_numbers(number_from)

        if self.numbers[office_from][letter_from] is None:
            raise ValueError(f"No person on {number_from} seat.")

        office_to, letter_to = self._parse_numbers(number_to)

        if self.numbers[office_to][letter_to] is not None:
            raise ValueError(f"Seat {number_to} is already taken.")

        self.numbers[office_to][letter_to] = self.numbers[office_from][letter_from]
        self.numbers[office_from][letter_from] = None

    def get_empty_terms(self):
        return sum(sum(1 for number in office.values() if number is None)
                   for office in self.numbers
                   if office is not None)

    def print_visit_details(self, printer):
        patients = self.get_list_of_patients()

        for patient, number in patients:
            printer(patient, number, self.get_specialist(), self.visit_time)

    def get_list_of_patients(self):
        patients = []
        offices, letters = self.doctors_room.timetable()

        for office in offices:
            for letter in letters:
                patient = self.numbers[office][letter]
                if patient is not None:
                    patient_data = patient, f"{office}{letter}"
                    patients.append(patient_data)

        return patients
