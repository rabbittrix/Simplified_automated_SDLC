import pytest
from app import *

def test_get_mock_erp_data():
    data = get_mock_erp_data()
    assert "Production Order" in data
    assert "Status" in data
    assert isinstance(data["Production Order"], str)

def test_get_mock_mes_data():
    data = get_mock_mes_data()
    assert "Machine Temp" in data
    assert "Line Status" in data
    assert isinstance(data["Machine Temp"], str)

def test_get_mock_plm_data():
    data = get_mock_plm_data()
    assert "Version" in data
    assert "Change Req" in data
    assert isinstance(data["Version"], str)
