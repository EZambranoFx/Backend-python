from datetime import datetime

class ProfessionalSchedule:
    def __init__(self, profession, professional, begin_time, end_time):
        self.profession = profession
        self.professional = professional
        self.begin_time = self._parse_time(begin_time)
        self.end_time = self._parse_time(end_time)

    def _parse_time(self, time_str):
        """Convert a time string to a datetime object."""
        try:
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Time must be in 'YYYY-MM-DD HH:MM:SS' format")

    def get_duration(self):
        """Calculate the duration between begin_time and end_time."""
        if self.end_time < self.begin_time:
            raise ValueError("End time must be after begin time")
        duration = self.end_time - self.begin_time
        return duration

    def display_info(self):
        """Display information about the professional schedule."""
        print(f"Profession: {self.profession}")
        print(f"Professional: {self.professional}")
        print(f"Begin Time: {self.begin_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"End Time: {self.end_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Duration: {self.get_duration()}")

# Example usage:
if __name__ == "__main__":
    schedule = ProfessionalSchedule(
        profession="Software Developer",
        professional="Alice Johnson",
        begin_time="2024-08-24 09:00:00",
        end_time="2024-08-24 17:00:00"
    )
    schedule.display_info()