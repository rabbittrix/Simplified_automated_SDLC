import streamlit as st
import random
import networkx as nx
from pyvis import Network

def get_mock_erp_data():
    return {"Production Order": f"PO-{random.randint(1000, 9999)}", "Status": random.choice(["Running", "Completed"])}

def get_mock_mes_data():
    return {"Machine Temp": f"{random.randint(70, 120)}°C", "Line Status": random.choice(["Active", "Idle", "Stopped"])}

def get_mock_plm_data():
    return {"Version": f"v{random.randint(1, 10)}.{random.randint(0,9)}", "Change Req": random.randint(1, 20)}

def show_system_graph():
    net = Network(height="300px", width="100%", bgcolor="#222222", font_color="white")
    net.add_node("ERP", title="ERP System", color="#00ff1e")
    net.add_node("MES", title="MES System", color="#ffaa00")
    net.add_node("PLM", title="PLM System", color="#008cba")
    net.add_edge("ERP", "MES")
    net.add_edge("MES", "PLM")
    net.add_edge("ERP", "PLM")
    net.save_graph("graph.html")
    with open("graph.html", "r", encoding="utf-8") as f:
        html = f.read()
    return html

# Função principal do Streamlit
def main():
    st.set_page_config(page_title="Industrial Integration Dashboard", layout="wide")
    st.title("🏭 Industrial Integration Dashboard (ERP + MES + PLM)")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 ERP System")
        erp_data = get_mock_erp_data()
        st.json(erp_data)

    with col2:
        st.subheader("⚙️ MES System")
        mes_data = get_mock_mes_data()
        st.json(mes_data)

    st.subheader("🧩 PLM System")
    plm_data = get_mock_plm_data()
    st.json(plm_data)

    st.subheader("🔗 Systems Integration Map")
    st.components.v1.html(show_system_graph(), height=350)

    st.success("Dashboard atualizado com sucesso! (Mock Real-Time)")

if __name__ == "__main__":
    main()