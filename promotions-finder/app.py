import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Alex — AI Deal Finder",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: #0a0a0f;
    }
    .block-container {
        padding-top: 2rem !important;
        max-width: 1100px;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 3rem 1rem 2rem;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(99,102,241,0.15);
        color: #818cf8;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 6px 16px;
        border-radius: 20px;
        letter-spacing: 0.5px;
        margin-bottom: 1.2rem;
        font-family: 'Inter', sans-serif;
    }
    .hero h1 {
        font-family: 'Inter', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        color: #ffffff;
        line-height: 1.15;
        margin: 0 0 1rem;
    }
    .hero h1 span {
        background: linear-gradient(135deg, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        font-size: 1.15rem;
        max-width: 600px;
        margin: 0 auto 2rem;
        line-height: 1.6;
    }

    /* CTA section */
    .cta-area {
        text-align: center;
        margin: 1.5rem 0 3rem;
    }
    .cta-label {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 0.6rem;
    }
    .cta-arrow {
        display: inline-block;
        font-size: 2rem;
        color: #818cf8;
        animation: bounce 1.5s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(8px); }
    }
    .cta-hint {
        font-family: 'Inter', sans-serif;
        color: #475569;
        font-size: 0.82rem;
        margin-top: 0.5rem;
    }

    /* Feature cards */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
        margin: 0 auto 3rem;
    }
    @media (max-width: 768px) {
        .features-grid { grid-template-columns: 1fr; }
        .hero h1 { font-size: 2rem; }
    }
    .feature-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.8rem;
        transition: border-color 0.3s;
    }
    .feature-card:hover {
        border-color: rgba(129,140,248,0.4);
    }
    .feature-icon {
        font-size: 1.8rem;
        margin-bottom: 0.8rem;
    }
    .feature-card h3 {
        font-family: 'Inter', sans-serif;
        color: #e2e8f0;
        font-size: 1.05rem;
        font-weight: 600;
        margin: 0 0 0.5rem;
    }
    .feature-card p {
        font-family: 'Inter', sans-serif;
        color: #94a3b8;
        font-size: 0.88rem;
        line-height: 1.55;
        margin: 0;
    }

    /* Example prompts */
    .prompts-section {
        text-align: center;
        margin: 0 auto 3rem;
    }
    .prompts-section h2 {
        font-family: 'Inter', sans-serif;
        color: #e2e8f0;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 1.2rem;
    }
    .prompt-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.7rem;
        justify-content: center;
    }
    .prompt-chip {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        color: #cbd5e1;
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        padding: 10px 18px;
        border-radius: 12px;
        cursor: default;
        transition: background 0.2s;
    }
    .prompt-chip:hover {
        background: rgba(129,140,248,0.12);
    }

    /* Footer */
    .app-footer {
        text-align: center;
        padding: 2rem 0 1rem;
        border-top: 1px solid rgba(255,255,255,0.06);
    }
    .app-footer p {
        font-family: 'Inter', sans-serif;
        color: #475569;
        font-size: 0.82rem;
        margin: 0;
    }
    .app-footer a {
        color: #818cf8;
        text-decoration: none;
    }

    /* Hide streamlit defaults */
    #MainMenu, footer, .stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──
st.markdown("""
<div class="hero">
    <div class="hero-badge">ANY CITY &nbsp;·&nbsp; VOICE-POWERED &nbsp;·&nbsp; REAL-TIME PRICES</div>
    <h1>Meet <span>Alex</span>, Your<br>AI Deal Finder</h1>
    <p>Just say what you want and where you are — any city, any neighborhood. Alex searches the web instantly and comes back with real promotions, exact prices, and specific addresses.</p>
</div>
""", unsafe_allow_html=True)

# ── Voice widget ──
elevenlabs_widget = """
<style>
    body { margin: 0; background: transparent !important; }
</style>
<elevenlabs-convai agent-id="agent_4701kmkdvpagek8t3szf3a2bhmkh"></elevenlabs-convai>
<script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
"""
components.html(elevenlabs_widget, height=500)

st.markdown("""
<div class="cta-area">
    <p class="cta-hint">Talk to Alex — just say what you're looking for and where</p>
</div>
""", unsafe_allow_html=True)

# ── Features ──
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3>Instant Search</h3>
        <p>Say "hamburgers in Galán Bogotá" or "pizza deals in Austin" and Alex immediately searches for current promotions with real prices.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">💰</div>
        <h3>Exact Prices</h3>
        <p>Every result includes the actual price in local currency — $28,000 COP, $9.99 USD, €12.50 — not vague descriptions.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📍</div>
        <h3>Specific Addresses</h3>
        <p>Get the exact street or address wherever possible — not just the city name.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🎙️</div>
        <h3>Voice-First</h3>
        <p>Just talk. Say what you want and where you are. Alex responds in seconds with the best deals.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🌐</div>
        <h3>Multilingual</h3>
        <p>Ask in any language — Alex adapts the search to your city’s local language automatically.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <h3>Always Current</h3>
        <p>Powered by Firecrawl live web search. Results are from today, not cached or outdated data.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Example prompts ──
st.markdown("""
<div class="prompts-section">
    <h2>Just say something like</h2>
    <div class="prompt-chips">
        <div class="prompt-chip">🍔 "Hamburguesas en Galán, Bogotá"</div>
        <div class="prompt-chip">🍕 "Pizza deals in Austin, Texas"</div>
        <div class="prompt-chip">👟 "Ropa en Chapinero, Bogotá"</div>
        <div class="prompt-chip">📱 "Electronics near Oxford Street, London"</div>
        <div class="prompt-chip">☕ "Cafés con ofertas en Roma"</div>
        <div class="prompt-chip">🛒 "Supermercados en Suba, Bogotá"</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ──
st.markdown("""
<div class="app-footer">
    <p>Built with <a href="https://elevenlabs.io/agents" target="_blank">ElevenLabs Agents</a> &amp; <a href="https://firecrawl.dev" target="_blank">Firecrawl Search</a></p>
</div>
""", unsafe_allow_html=True)
