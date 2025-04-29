# test_app.py
from app import create_network, get_mock_erp_data, get_mock_mes_data, get_mock_plm_data, Network

def test_create_network():
    network = create_network()
    assert isinstance(network, Network)
    assert len(network.nodes) == 0  # Verifica se a rede começa vazia

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
    assert isinstance(data["Change Req"], int)
    
def test_show_system_graph():
    from app import show_system_graph  # Import the function
    html = show_system_graph()
    assert "<html>" in html  # Verifica se o HTML contém a tag <html>
    assert "ERP System" in html  # Verifica se o título do nó ERP está presente
    assert "MES System" in html  # Verifica se o título do nó MES está presente
    assert "PLM System" in html  # Verifica se o título do nó PLM está presente
    assert "graph.html" in html  # Verifica se o arquivo graph.html está referenciado
    
def test_app():
    # Simula a execução do aplicativo Streamlit
    import streamlit as st
    from io import StringIO

    # Redireciona a saída para um buffer de string
    buffer = StringIO()
    st.write = buffer.write

    # Executa o aplicativo
    from app import app  # Importa o aplicativo
    app.run()

    # Verifica se o título do aplicativo está presente na saída
    output = buffer.getvalue()
    assert "🏭 Industrial Integration Dashboard (ERP + MES + PLM)" in output
    
    assert "📦 ERP System" in output
    assert "⚙️ MES System" in output
    assert "🧩 PLM System" in output
    assert "🔗 Systems Integration Map" in output
    assert "Dashboard atualizado com sucesso! (Mock Real-Time)" in output

    assert "graph.html" in output  # Verifica se o arquivo graph.html está referenciado
    assert "ERP System" in output  # Verifica se o título do nó ERP está presente

    assert "MES System" in output  # Verifica se o título do nó MES está presente
    assert "PLM System" in output  # Verifica se o título do nó PLM está presente
    
def test_streamlit_app():
    import streamlit as st
    from io import StringIO  # Importa StringIO para redirecionar a saída
    from app import app  # Importa o aplicativo

    # Simula a execução do aplicativo Streamlit
    buffer = StringIO()
    st.write = buffer.write

    # Executa o aplicativo
    app.run()

    # Verifica se o título do aplicativo está presente na saída
    output = buffer.getvalue()
    assert "🏭 Industrial Integration Dashboard (ERP + MES + PLM)" in output
    
    assert "📦 ERP System" in output
    assert "⚙️ MES System" in output
    assert "🧩 PLM System" in output
    assert "🔗 Systems Integration Map" in output
    assert "Dashboard atualizado com sucesso! (Mock Real-Time)" in output
    assert "graph.html" in output  # Verifica se o arquivo graph.html está referenciado
    