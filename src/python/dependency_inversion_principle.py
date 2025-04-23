from abc import ABC, abstractmethod


# Abstraction
class DataSource(ABC):
    @abstractmethod
    def fetch_data(self):
        pass


# Low-level module
class BackendService(DataSource):
    def fetch_data(self):
        print("Getting data from the database...")


# High-level module
class ReportGenerator:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def generate_report(self):
        self.data_source.fetch_data()
        print("Generating report...")


# Usage
service = BackendService()
report = ReportGenerator(service)
report.generate_report()
