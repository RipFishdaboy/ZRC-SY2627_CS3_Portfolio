class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self._bill_amount * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("Patient Name:", regular_patient.get_name())
print("Original Bill: P", regular_patient.get_bill_amount())
print("Final Bill: P", regular_patient.calculate_bill())
print()

print("Patient Name:", senior_patient.get_name())
print("Original Bill: P", senior_patient.get_bill_amount())
print("Final Bill: P", senior_patient.calculate_bill())
print()

print("Patient Name:", philhealth_patient.get_name())
print("Original Bill: P", philhealth_patient.get_bill_amount())
print("Final Bill: P", philhealth_patient.calculate_bill())
