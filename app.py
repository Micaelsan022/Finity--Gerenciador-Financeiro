import streamlit as st

st.set_page_config(
    page_title="Finity - Gerenciador Financeiro",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        @keyframes countUp {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
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

        .hero-container {
            text-align: center;
            padding: 60px 20px 40px 20px;
            animation: fadeInDown 0.8s ease;
        }
        .hero-badge {
            display: inline-block;
            background: rgba(46, 204, 113, 0.1);
            border: 1px solid rgba(46, 204, 113, 0.3);
            color: #2ECC71;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 0.75em;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }
        .hero-title {
            font-size: 5em;
            font-weight: 900;
            background: linear-gradient(90deg, #2ECC71, #27AE60, #2ECC71);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s linear infinite;
            margin: 0;
            line-height: 1;
        }
        .hero-subtitle {
            font-size: 1.2em;
            color: #888;
            margin: 16px 0 0 0;
            font-weight: 300;
            letter-spacing: 1px;
        }

        .features-container {
            display: flex;
            gap: 16px;
            margin: 40px 0;
            animation: fadeInUp 0.8s ease 0.3s both;
        }
        .feature-card {
            flex: 1;
            background: linear-gradient(135deg, #141414, #1a1a1a);
            border: 1px solid #222;
            border-radius: 16px;
            padding: 28px 20px;
            text-align: center;
            transition: all 0.3s ease;
            cursor: default;
        }
        .feature-card:hover {
            border-color: #2ECC71;
            transform: translateY(-4px);
            box-shadow: 0 8px 30px rgba(46, 204, 113, 0.15);
        }
        .feature-icon {
            font-size: 2.2em;
            margin-bottom: 12px;
        }
        .feature-title {
            font-size: 1em;
            font-weight: 700;
            color: #fff;
            margin-bottom: 8px;
        }
        .feature-desc {
            font-size: 0.82em;
            color: #666;
            line-height: 1.5;
        }

        .stats-container {
            display: flex;
            gap: 16px;
            margin: 20px 0;
            animation: fadeInUp 0.8s ease 0.5s both;
        }
        .stat-card {
            flex: 1;
            background: linear-gradient(135deg, #0d1a12, #111);
            border: 1px solid rgba(46, 204, 113, 0.2);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            animation: pulse 2s infinite;
        }
        .stat-number {
            font-size: 2em;
            font-weight: 800;
            color: #2ECC71;
            animation: countUp 0.8s ease;
        }
        .stat-label {
            font-size: 0.78em;
            color: #555;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 4px;
        }

        .cta-container {
            text-align: center;
            padding: 30px 0;
            animation: fadeInUp 0.8s ease 0.7s both;
        }
        .cta-text {
            color: #444;
            font-size: 0.85em;
            margin-bottom: 12px;
        }
        .cta-arrow {
            color: #2ECC71;
            font-size: 1.5em;
            animation: fadeInDown 1s ease infinite alternate;
        }

        .footer-text {
            text-align: center;
            color: #222;
            font-size: 0.75em;
            padding: 20px 0;
            border-top: 1px solid #1a1a1a;
            margin-top: 20px;
        }
    </style>

    <div class="hero-container">
        <div class="hero-badge">Gerenciador Financeiro Pessoal</div>
        <h1 class="hero-title">Finity</h1>
        <p class="hero-subtitle">Controle suas finanças com inteligência e estilo</p>
    </div>

    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">💰</div>
            <div class="stat-label">Controle de Receitas</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">📊</div>
            <div class="stat-label">Dashboard Interativo</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">🎯</div>
            <div class="stat-label">Metas Financeiras</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">⚠️</div>
            <div class="stat-label">Alertas Inteligentes</div>
        </div>
    </div>

    <div class="features-container">
        <div class="feature-card">
            <div class="feature-icon">💰</div>
            <div class="feature-title">Receitas</div>
            <div class="feature-desc">Registre e acompanhe todas as suas entradas de dinheiro por categoria</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">💸</div>
            <div class="feature-title">Gastos</div>
            <div class="feature-desc">Monitore seus gastos e receba alertas quando ultrapassar os limites</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Metas</div>
            <div class="feature-desc">Defina objetivos financeiros e acompanhe seu progresso em tempo real</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Relatórios</div>
            <div class="feature-desc">Visualize gráficos e relatórios detalhados das suas finanças</div>
        </div>
    </div>

    <div class="cta-container">
        <p class="cta-text">Use o menu lateral para começar</p>
        <div class="cta-arrow">←</div>
    </div>

    <div class="footer-text">
        Finity v1.0.0 — Projeto Acadêmico
    </div>
""", unsafe_allow_html=True)