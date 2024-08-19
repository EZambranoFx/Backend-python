from datetime import datetime
import csv
import hashlib

from Profesional import Profesionales
from reports import AppointmentReport


# Suponiendo que Profesionales y AppointmentReport ya están definidos en el contexto

class TestAppointmentReport:
    def __init__(self):
        self.professionals_list = []

    def create_fake_professional(self):
        # Crear un profesional ficticio
        id = '1234567890'
        password = 'password'
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        profession = 'Engineer'
        date_string = datetime.now().strftime("%B %d, %Y")
        professional = Profesionales(id, hash_value, profession, date_string)
        self.professionals_list.append(professional)
        print("Pofesional que agendara la cita")
        print(professional)
        return professional

    def create_fake_appointments(self, professional):
        # Crear citas ficticias para el profesional
        appointments = [
            {'client_name': 'John Doe', 'client_contact': '555-1234', 'appointment_time': datetime.now().strftime("%B %d, %Y")},
            {'client_name': 'Jane Smith', 'client_contact': '555-5678', 'appointment_time': datetime.now().strftime("%B %d, %Y")},
            {'client_name': 'Emily Johnson', 'client_contact': '555-8765', 'appointment_time': datetime.now().strftime("%B %d, %Y")}
        ]
        print("Citas a guardar")
        for appointment in appointments:
            print(appointment)
            professional.create_appointment(appointment['client_name'], appointment['client_contact'], appointment['appointment_time'])
        return appointments

    def test_generate_csv_report(self):
        professional = self.create_fake_professional()
        appointments = self.create_fake_appointments(professional)
        report = AppointmentReport(appointments)
        report.generate_csv_report('test_report.csv')

        print("Test completado revisa 'test_report.csv'")

if __name__ == "__main__":
    test_report = TestAppointmentReport()
    test_report.test_generate_csv_report()
