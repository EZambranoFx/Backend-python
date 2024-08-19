import csv

class AppointmentReport:
    def __init__(self, appointments):
        self.appointments = appointments

    def generate_csv_report(self, file_name='reporteDeCitas'):
        headers = ['Nombre del cliente', 'Numero de contacto', 'Fecha de la cita']

        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)

            for appointment in self.appointments:
                writer.writerow([
                    appointment['client_name'],
                    appointment['client_contact'],
                    appointment['appointment_time']
                ])

        print(f'Reporte generado: {file_name}')