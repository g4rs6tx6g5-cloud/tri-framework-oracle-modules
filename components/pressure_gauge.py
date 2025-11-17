import streamlit as st
from utils.calculations import calculate_pressure_gauge, calculate_trend_status

def pressure_gauge_tab():
    st.header("📊 Pressure Gauge Protocol")
    st.markdown("*Positioning analysis: (Long OI - Short OI) / Total OI*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        long_oi = st.number_input(
            "Long Open Interest (BTC):",
            min_value=0.0,
            value=5500000.0,
            step=100000.0,
            format="%.0f",
            key="long_oi"
        )
    
    with col2:
        short_oi = st.number_input(
            "Short Open Interest (BTC):",
            min_value=0.0,
            value=4500000.0,
            step=100000.0,
            format="%.0f",
            key="short_oi"
        )
    
    if st.button("📈 Calculate Pressure Gauge", type="secondary"):
        with st.spinner("Analyzing positioning..."):
            pressure_gauge = calculate_pressure_gauge(long_oi, short_oi)
            
            st.markdown("### 📊 Positioning Analysis:")
            
            # Display raw data
            st.metric("Total Open Interest", f"{long_oi + short_oi:,.0f} BTC")
            st.metric("Long OI", f"{long_oi:,.0f} BTC")
            st.metric("Short OI", f"{short_oi:,.0f} BTC")
            
            # Display pressure gauge
            st.markdown(f"### 🎯 Pressure Gauge: {pressure_gauge:.3f}")
            
            # Interpretation
            if pressure_gauge > 0.5:
                st.markdown(
                    f'<div class="pressure-high-container"><h4>🔴 EXTREME LONGS ({pressure_gauge:.1%})</h4><p>Potential for bearish squeeze if market breaks down</p></div>',
                    unsafe_allow_html=True
                )
            elif pressure_gauge < -0.5:
                st.markdown(
                    f'<div class="pressure-low-container"><h4>🟢 EXTREME SHORTS ({abs(pressure_gauge):.1%})</h4><p>Potential for bullish squeeze if market breaks up</p></div>',
                    unsafe_allow_html=True
                )
            elif pressure_gauge > 0.2:
                st.markdown(
                    f'<div class="pressure-high-container"><h4>🟡 HIGH LONGS ({pressure_gauge:.1%})</h4><p>Caution - longs may be crowded</p></div>',
                    unsafe_allow_html=True
                )
            elif pressure_gauge < -0.2:
                st.markdown(
                    f'<div class="pressure-low-container"><h4>🟡 HIGH SHORTS ({abs(pressure_gauge):.1%})</h4><p>Caution - shorts may be crowded</p></div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="neutral-container"><h4>⚪️ BALANCED ({pressure_gauge:.1%})</h4><p>Positioning appears neutral</p></div>',
                    unsafe_allow_html=True
                )
            
            # Analysis interpretation
            st.markdown("### 🔍 Analysis:")
            if pressure_gauge > 0.7:
                st.warning("⚠️ EXTREME LONG CONGESTION - Potential for bearish break if support fails")
            elif pressure_gauge < -0.7:
                st.success("✅ EXTREME SHORT CONGESTION - Potential for bullish break if resistance breaks")
            elif abs(pressure_gauge) > 0.3:
                st.info(f"ℹ️ POSITIONING ASYMMETRY DETECTED - Current bias: {'LONG' if pressure_gauge > 0 else 'SHORT'}")
