import unittest
from unittest.mock import patch, mock_open
from utils.functions import successful_operations


class TestFunctions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 667307132, "state": "EXECUTED", '
                                                              '"date": "2019-07-13T18:51:29.313309", '
                                                              '"operationAmount": {"amount": "97853.86", '
                                                              '"currency": {"name": "руб.", "code": "RUB"}}, '
                                                              '"description": "Перевод с карты на счет", '
                                                              '"from": "Maestro 1308795367077170", '
                                                              '"to": "Счет 96527012349577388612"}]')
    def test_successful_operation(self, files):
        result = successful_operations()
        expected_result = [{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
                            'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170',
                            'to': 'Счет 96527012349577388612'}]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
