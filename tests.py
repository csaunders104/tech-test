# from utils import loop_dates
from datetime import date
from mock import patch

import unittest
import globals as g

@patch('utils.loop_dates')
def test_loop_dates(self, mock_loop_dates):

    test_date_pass  = date(2023, 5, 5)
    test_date_error = date(2024, 1, 1)

    mock_loop_dates.assert_called_with(test_date_pass)
    # assert the functions returns true
    mock_loop_dates.assert_called_with(test_date_error)
    # assert the functions returns true