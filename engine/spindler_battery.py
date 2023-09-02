from car import Battery
from abc import ABC


class SpindlerBattery(Battery,ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def battery_should_be_serviced(self):
        return self.current_date - self.last_service_date > 2

    