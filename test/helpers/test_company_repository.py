import pytest

from carbon_footprint_calculator.helpers.company_repository import CompanyRepository


class TestCompanyRepository:

    @staticmethod
    @pytest.mark.unit
    def test_all_functionalities():
        repository: CompanyRepository = CompanyRepository.get_instance()

        repository.clear()
        assert repository.is_empty()

        repository.add('Company 1', 1, 1, 1, 3)
        assert repository.is_empty() == False
        assert len(repository.get_all()) == 1
        assert repository.get('Company 1')['energy_usage'] == 1
