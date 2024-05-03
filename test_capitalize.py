import pytest
from capitalize import *

def test_capital_case():
    assert capital_case('elvebakken') == 'Elvebakken'

def test_capital_case_lowercase():
    assert capital_case('elvebakken') != 'elvebakken'