def aplicar_estilo():
    import streamlit as st
    st.markdown("""
        <style>
            @keyframes fadeInDown {
                from { opacity: 0; transform: translateY(-30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0.4); }
                70% { box-shadow: 0 0 0 15px rgba(46, 204, 113, 0); }
                100% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0); }
            }
            @keyframes shimmer {
                0% { background-position: -200% center; }
                100% { background-position: 200% center; }
            }

            [data-testid="stSidebar"] {
                background-color: #0f0f0f;
                border-right: 1px solid #1a1a1a;
            }
            [data-testid="stSidebar"] * {
                color: #ffffff !important;
            }
            [data-testid="stAppViewContainer"] {
                background: linear-gradient(135deg, #0a0a0a 0%, #111111 50%, #0d1a12 100%);
            }
            .metric-card {
                background: linear-gradient(135deg, #141414, #1a1a1a);
                border: 1px solid #222;
                border-radius: 16px;
                padding: 24px 20px;
                text-align: center;
                transition: all 0.3s ease;
                animation: fadeInUp 0.6s ease;
            }
            .metric-card:hover {
                border-color: #2ECC71;
                transform: translateY(-4px);
                box-shadow: 0 8px 30px rgba(46, 204, 113, 0.15);
            }
            .metric-value {
                font-size: 1.8em;
                font-weight: bold;
                margin: 8px 0;
            }
            .metric-label {
                font-size: 0.85em;
                color: #888888;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .verde { color: #2ECC71; }
            .vermelho { color: #E74C3C; }
            .page-header {
                padding: 30px 0 20px 0;
                animation: fadeInDown 0.6s ease;
            }
            .page-title {
                margin: 0;
                font-size: 2em;
                font-weight: 800;
                color: #fff;
            }
            .page-subtitle {
                margin: 4px 0 0 0;
                color: #888;
            }
        </style>
    """, unsafe_allow_html=True)

def aplicar_sidebar():
    import streamlit as st
    st.sidebar.markdown("""
        <div style="padding: 24px 16px 16px 16px;">
            <p style="margin: 0; font-size: 0.75em; color: #555; text-transform: uppercase; letter-spacing: 2px;">Gerenciador Financeiro</p>
            <h1 style="margin: 4px 0 0 0; font-size: 2em; color: #2ECC71; font-weight: 800;">Finity</h1>
        </div>
        <hr style="border: none; border-top: 1px solid #222; margin: 0 16px 16px 16px;">
    """, unsafe_allow_html=True)