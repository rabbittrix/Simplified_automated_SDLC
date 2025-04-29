import pytest
from app import get_mock_erp_data, get_mock_mes_data, get_mock_plm_data, show_system_graph
from pyvis.network import Network

def test_get_mock_erp_data():
    data = get_mock_erp_data()
    assert "Production Order" in data
    assert "Status" in data
    assert isinstance(data["Production Order"], str)
    assert data["Status"] in ["Running", "Completed"]

def test_get_mock_mes_data():
    data = get_mock_mes_data()
    assert "Machine Temp" in data
    assert "Line Status" in data
    assert isinstance(data["Machine Temp"], str)
    assert data["Line Status"] in ["Active", "Idle", "Stopped"]

def test_get_mock_plm_data():
    data = get_mock_plm_data()
    assert "Version" in data
    assert "Change Req" in data
    assert isinstance(data["Version"], str)
    assert isinstance(data["Change Req"], int)

def test_show_system_graph():
    html = show_system_graph()
    assert "<html>" in html  
    assert "ERP System" in html  
    assert "MES System" in html  
    assert "PLM System" in html  
    assert "graph.html" in html  

def test_pyvis_network_creation():
    net = Network(height="300px", width="100%", bgcolor="#222222", font_color="white")
    net.add_node("TestNode", title="Test Node", color="#ff0000")
    assert len(net.nodes) == 1  
    assert net.nodes[0]["label"] == "TestNode"