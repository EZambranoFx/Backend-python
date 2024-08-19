class Profesionales:
  def __init__(self, id, password, profession, date):
    self.id = id
    self.password = password
    self.profession = profession
    self.date = date
    self.dates = []

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