class CompanyRepository:
    __INSTANCE = None

    @staticmethod
    def get_instance():
        if CompanyRepository.__INSTANCE is None:
            CompanyRepository()
        return CompanyRepository.__INSTANCE

    def __init__(self):
        if CompanyRepository.__INSTANCE is not None:
            raise Exception('CompanyRepository class is singleton and can be instantiated only once!')
        else:
            CompanyRepository.__INSTANCE = self
            self.__storage = {}

    def add(self,
            company_name: str,
            energy_usage: float,
            generated_waste: float,
            business_travel_usage: float,
            total_usage: float):
        self.__storage[company_name] = {
            'energy_usage': energy_usage,
            'generated_waste': generated_waste,
            'business_travel_usage': business_travel_usage,
            'total_usage': total_usage
        }

    def get_all(self) -> dict:
        return self.__storage

    def get(self, company_name: str) -> dict:
        return self.__storage[company_name]

    def is_empty(self):
        return len(self.__storage) == 0

    def clear(self):
        self.__storage.clear()
