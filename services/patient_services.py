from models.patient import Patient
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print(patient.address.city)
    print(patient.calculate_bmi)
