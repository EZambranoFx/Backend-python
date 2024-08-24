from ProfessionalSchedule import ProfessionalSchedule
from datetime import datetime

class Profesionales:
  def __init__(self, id, password, profession):
    self.id = id
    self.password = password
    self.profession = profession
    self.timeTable = timeTable
    #self.date = date
    self.dates = []
    
    def create_schedule():
        dt = datetime.today()
        return

    def create_appointment(self, client_name, client_contact, appointment_time):
        appointment = {
            "client_name": client_name,
            "client_contact": client_contact,
            "appointment_time": appointment_time
        }
        if isinstance(self.dates, list):
            self.dates.append(appointment)
        else:
            raise TypeError("self.dates should be a list")
        return appointment