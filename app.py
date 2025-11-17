import streamlit as st
from components.arbitrage_calculator import arbitrage_tab
from components.pressure_gauge import pressure_gauge_tab
from components.market_analysis import market_analysis_tab
from components.fibonacci_engine import fibonacci_tab
from components.technical_indicators import technical_indicators_tab
from components.volume_analysis import volume_analysis_tab
from components.data_integration_dashboard import data_integration_tab
 
def main():
    # Configure Streamlit page
    st.set_page_config(
        page_title="Tri-Framework Oracle - Trading Mastery",
        page_icon="🔮",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for dark mode and styling
    st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #202938;
        color: #ffffff;
        border: 1px solid #374151;
    }
    .stNumberInput > div > div > input {
        background-color: #202938;
        color: #ffffff;
        border: 1px solid #374151;
    }
    .stSelectbox > div > div {
        background-color: #202938;
        color: #ffffff;
        border: 1px solid #374151;
    }
    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #1d4ed8;
    }
    .metric-container {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #2563eb;
    }
    .success-container {
        background-color: #166534;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #22c55e;
    }
    .error-container {
        background-color: #991b1b;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #ef4444;
    }
    .pressure-high-container {
        background-color: #dc2626;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #ef4444;
    }
    .pressure-low-container {
        background-color: #16a34a;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #22c55e;
    }
    .neutral-container {
        background-color: #f59e0b;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #fbbf24;
    }
    .fib-level {
        background-color: #1f2937;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #8b5cf6;
    }
    .indicator-bullish {
        background-color: #16a34a;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #22c55e;
    }
    .indicator-bearish {
        background-color: #dc2626;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #ef4444;
    }
    .indicator-neutral {
        background-color: #f59e0b;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #fbbf24;
    }
    .volume-high {
        background-color: #16a34a;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #22c55e;
    }
    .volume-low {
        background-color: #dc2626;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #ef4444;
    }
    .volume-neutral {
        background-color: #f59e0b;
        padding: 8px;
        border-radius: 5px;
        margin: 2px 0;
        border-left: 2px solid #fbbf24;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # App title
    st.title("🔮 Tri-Framework Oracle - Trading Mastery")
    st.markdown("*Mathematical precision for BTC/USDT trading mastery*")
    
    # Navigation
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Arbitrage Calculator", 
        "Pressure Gauge", 
        "Market Analysis", 
        "Fibonacci Engine", 
        "Technical Indicators", 
        "Volume Analysis",
        "Quantum Confluence"
    ])
    
    with tab1:
        arbitrage_tab()
    
    with tab2:
        pressure_gauge_tab()
    
    with tab3:
        market_analysis_tab()
    
    with tab4:
        fibonacci_tab()
    
    with tab5:
        technical_indicators_tab()
    
    with tab6:
        volume_analysis_tab()
    
    with tab7:
        data_integration_tab()

if __name__ == "__main__":
    main()