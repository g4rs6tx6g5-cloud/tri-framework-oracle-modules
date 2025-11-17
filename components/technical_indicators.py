import streamlit as st
from utils.calculations import calculate_rsi, calculate_dmi

def technical_indicators_tab():
    st.header("📊 Technical Indicators - DMI & RSI Integration")
    st.markdown("*Trend strength and momentum analysis for 99.99% certainty*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("DMI (Directional Movement Index)")
        st.markdown("*Trend strength validation*")
        
        # Timeframe selector for DMI
        dmi_timeframe = st.selectbox(
            "DMI Timeframe:",
            options=['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w'],
            index=4,  # Default to 1h
            key="dmi_timeframe"
        )
        
        # Simulated price data for DMI calculation (will be replaced by API data)
        high_prices = st.text_input("High Prices (comma separated, last 15 values):", 
                                   "110000,110100,110200,110150,110250,110300,110200,110100,110150,110200,110100,110050,110000,109950,109900")
        low_prices = st.text_input("Low Prices (comma separated, last 15 values):", 
                                  "109500,109600,109700,109650,109750,109800,109700,109600,109650,109700,109600,109550,109500,109450,109400")
        close_prices = st.text_input("Close Prices (comma separated, last 15 values):", 
                                    "109800,109900,110000,109950,110050,110100,110000,109900,109950,110000,109900,109850,109800,109750,109700")
    
    with col2:
        st.subheader("RSI (Relative Strength Index)")
        st.markdown("*Momentum analysis*")
        
        # Timeframe selector for RSI
        rsi_timeframe = st.selectbox(
            "RSI Timeframe:",
            options=['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w'],
            index=4,  # Default to 1h
            key="rsi_timeframe"
        )
        
        # Simulated price data for RSI calculation (will be replaced by API data)
        prices = st.text_input("Price Data (comma separated, last 15 values):", 
                              "109550,109600,109650,109700,109750,109800,109850,109900,109950,110000,110050,110100,110150,110200,110250")
    
    if st.button("📊 Calculate Technical Indicators", type="secondary"):
        with st.spinner("Calculating DMI and RSI..."):
            # Parse the input data
            try:
                high_list = [float(x.strip()) for x in high_prices.split(',')]
                low_list = [float(x.strip()) for x in low_prices.split(',')]
                close_list = [float(x.strip()) for x in close_prices.split(',')]
                price_list = [float(x.strip()) for x in prices.split(',')]
            except:
                st.error("Please enter valid comma-separated numbers")
                return
            
            # Calculate DMI
            pdi, mdi = calculate_dmi(high_list, low_list, close_list)
            
            # Calculate RSI
            rsi = calculate_rsi(price_list)
            
            st.markdown("### 📊 Technical Analysis Results:")
            
            # Display selected timeframes
            st.info(f"DMI Timeframe: {dmi_timeframe} | RSI Timeframe: {rsi_timeframe}")
            
            # DMI Analysis
            st.markdown("#### 📈 DMI Analysis:")
            col_dmi1, col_dmi2 = st.columns(2)
            
            with col_dmi1:
                st.metric("PDI (Positive Directional Indicator)", f"{pdi:.2f}")
            
            with col_dmi2:
                st.metric("MDI (Negative Directional Indicator)", f"{mdi:.2f}")
            
            # DMI Interpretation
            if pdi > mdi + 10:
                st.markdown(
                    f'<div class="indicator-bullish"><h4>🟢 BULLISH TREND STRENGTH</h4><p>PDI ({pdi:.2f}) significantly stronger than MDI ({mdi:.2f})</p></div>',
                    unsafe_allow_html=True
                )
            elif mdi > pdi + 10:
                st.markdown(
                    f'<div class="indicator-bearish"><h4>🔴 BEARISH TREND STRENGTH</h4><p>MDI ({mdi:.2f}) significantly stronger than PDI ({pdi:.2f})</p></div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="indicator-neutral"><h4>🟡 NEUTRAL TREND STRENGTH</h4><p>PDI ({pdi:.2f}) and MDI ({mdi:.2f}) are balanced</p></div>',
                    unsafe_allow_html=True
                )
            
            # RSI Analysis
            st.markdown("#### 📊 RSI Analysis:")
            st.metric("RSI (14-period)", f"{rsi:.2f}")
            
            # RSI Interpretation
            if rsi > 70:
                st.markdown(
                    f'<div class="indicator-bearish"><h4>🔴 OVERBOUGHT ({rsi:.2f})</h4><p>Potential for reversal down</p></div>',
                    unsafe_allow_html=True
                )
            elif rsi < 30:
                st.markdown(
                    f'<div class="indicator-bullish"><h4>🟢 OVERSOLD ({rsi:.2f})</h4><p>Potential for reversal up</p></div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f'<div class="indicator-neutral"><h4>🟡 NEUTRAL ({rsi:.2f})</h4><p>Market in balanced state</p></div>',
                    unsafe_allow_html=True
                )
            
            # Combined Analysis
            st.markdown("### 🔮 Combined Technical Analysis:")
            
            if pdi > mdi + 10 and rsi < 70 and rsi > 30:
                st.success("✅ BULLISH CONFLUENCE: Strong trend + Neutral momentum = AETOS PROTOCOL OPTIMAL")
            elif mdi > pdi + 10 and rsi < 70 and rsi > 30:
                st.warning("⚠️ BEARISH CONFLUENCE: Strong trend + Neutral momentum = KHRUSOS PROTOCOL OPTIMAL")
            elif pdi > mdi + 10 and rsi < 30:
                st.info("ℹ️ BULLISH DIVERGENCE: Strong trend + Oversold = Potential reversal")
            elif mdi > pdi + 10 and rsi > 70:
                st.info("ℹ️ BEARISH DIVERGENCE: Strong trend + Overbought = Potential reversal")
            else:
                st.info("📊 Mixed signals - Wait for clearer confluence")
            
            # Framework Integration
            st.markdown("### 🎯 Framework Integration:")
            st.info("DMI + RSI analysis now feeds into your 99.99% certainty stack")
            st.info("Perfect foundation for AI agent data quantification")
