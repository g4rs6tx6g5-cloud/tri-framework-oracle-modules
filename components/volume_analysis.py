import streamlit as st
from utils.calculations import calculate_volume_analysis, calculate_vwap

def volume_analysis_tab():
    st.header("📊 Volume Analysis - MA50 Aligned")
    st.markdown("*Volume vs MA50, Delta Analysis, and VWAP for Institutional Levels*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Volume Analysis")
        st.markdown("*Current vs Average Volume, Buy/Sell Pressure*")
        
        # Volume data input
        current_volume = st.number_input(
            "Current Candle Volume:",
            min_value=0.0,
            value=1500.0,
            step=100.0,
            format="%.2f",
            key="current_volume"
        )
        
        volume_history = st.text_input(
            "Volume History (comma separated, last 20 values):",
            "1200,1300,1400,1250,1350,1450,1300,1200,1300,1400,1250,1350,1450,1300,1200,1300,1400,1250,1350,1450"
        )
    
    with col2:
        st.subheader("VWAP Calculation")
        st.markdown("*Institutional level identification*")
        
        # Price and volume data for VWAP
        prices = st.text_input(
            "Price Data (comma separated, last 20 values):",
            "109550,109600,109650,109700,109750,109800,109850,109900,109950,110000,110050,110100,110150,110200,110250,110300,110350,110400,110450,110500"
        )
        
        vwap_volumes = st.text_input(
            "Volume Data for VWAP (comma separated, last 20 values):",
            "1200,1300,1400,1250,1350,1450,1300,1200,1300,1400,1250,1350,1450,1300,1200,1300,1400,1250,1350,1450"
        )
    
    if st.button("📊 Calculate Volume Analysis", type="secondary"):
        with st.spinner("Analyzing volume data..."):
            # Parse volume history
            try:
                vol_history = [float(x.strip()) for x in volume_history.split(',')]
            except:
                st.error("Please enter valid comma-separated volume numbers")
                return
            
            # Parse price and volume data for VWAP
            try:
                price_list = [float(x.strip()) for x in prices.split(',')]
                vol_list = [float(x.strip()) for x in vwap_volumes.split(',')]
            except:
                st.error("Please enter valid comma-separated price and volume numbers")
                return
            
            # Calculate volume analysis
            volume_ratio, volume_status, delta_status = calculate_volume_analysis(current_volume, vol_history)
            
            # Calculate VWAP
            vwap = calculate_vwap(price_list, vol_list)
            
            st.markdown("### 📊 Volume Analysis Results:")
            
            # Current volume vs average
            st.metric(
                "Volume Ratio (Current/Average)",
                f"{volume_ratio:.2f}x",
                delta=f"{volume_status} volume"
            )
            
            # Volume status
            if volume_status == "HIGH":
                st.markdown(
                    f'<div class="volume-high"><h4>📈 HIGH VOLUME ({volume_status})</h4><p>Significant market interest, potential for trend continuation</p></div>',
                    unsafe_allow_html=True
                )
            elif volume_status == "LOW":
                st.markdown(
                    f'<div class="volume-low"><h4>📉 LOW VOLUME ({volume_status})</h4><p>Low market interest, potential for consolidation</p></div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="volume-neutral"><h4>⚖️ AVERAGE VOLUME ({volume_status})</h4><p>Normal market activity</p></div>',
                    unsafe_allow_html=True
                )
            
            # Volume delta (trend)
            st.markdown(f"### 📈 Volume Delta: {delta_status}")
            if delta_status == "INCREASING":
                st.success("📈 Volume is increasing - potential for trend acceleration")
            elif delta_status == "DECREASING":
                st.warning("📉 Volume is decreasing - potential for trend exhaustion")
            else:
                st.info("⚖️ Volume is stable - maintaining current trend strength")
            
            # VWAP Analysis
            st.markdown("### 🎯 VWAP Analysis:")
            st.metric("VWAP (Institutional Level)", f"${vwap:,.2f}")
            
            # VWAP vs Current Price (assuming current price is from Market Analysis)
            current_price = st.session_state.get('current_price', 109550.0)
            price_vwap_diff = current_price - vwap
            price_vwap_ratio = (current_price / vwap - 1) * 100
            
            st.metric(
                "Price vs VWAP",
                f"${price_vwap_diff:,.2f}",
                delta=f"{price_vwap_ratio:.2f}%"
            )
            
            if current_price > vwap:
                st.success(f"✅ PRICE ABOVE VWAP: {price_vwap_ratio:.2f}% - Bullish bias, institutional support below")
            else:
                st.error(f"❌ PRICE BELOW VWAP: {price_vwap_ratio:.2f}% - Bearish bias, institutional resistance above")
            
            # Volume Framework Integration
            st.markdown("### 🎯 Framework Integration:")
            if volume_status == "HIGH" and delta_status == "INCREASING":
                st.info("🚀 HIGH INCREASING VOLUME - Potential for 'Mountain Climb/Drop' - Monitor for breakouts")
            elif volume_status == "LOW" and delta_status == "DECREASING":
                st.warning("⏸️ LOW DECREASING VOLUME - Potential for consolidation - Wait for volume confirmation")
            
            st.info("Volume analysis now feeds into your positioning and entry timing decisions")
