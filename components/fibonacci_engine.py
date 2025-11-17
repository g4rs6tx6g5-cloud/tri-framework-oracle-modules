import streamlit as st
from utils.calculations import calculate_fibonacci_levels, calculate_timeframe_multiplier

def fibonacci_tab():
    st.header("🧮 Fibonacci Engine - Multi-Timeframe Analysis")
    st.markdown("*Magnifying glass for small timeframes, binoculars for long-term trends*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        high_price = st.number_input(
            "Swing High Price:",
            min_value=0.0,
            value=110000.0,
            step=100.0,
            format="%.2f",
            key="high_price"
        )
        
        low_price = st.number_input(
            "Swing Low Price:",
            min_value=0.0,
            value=109000.0,
            step=100.0,
            format="%.2f",
            key="low_price"
        )
    
    with col2:
        current_price_fib = st.number_input(
            "Current Price:",
            min_value=0.0,
            value=109550.0,
            step=100.0,
            format="%.2f",
            key="current_price_fib"
        )
        
        timeframe = st.selectbox(
            "Analysis Timeframe:",
            options=['1m', '5m', '15m', '30m', '1h', '4h', '1d', '1w'],
            index=4,  # Default to 1h
            key="timeframe"
        )
    
    if st.button("🧮 Calculate Fibonacci Analysis", type="secondary"):
        with st.spinner("Calculating Fibonacci levels..."):
            # Calculate Fibonacci levels
            fib_levels = calculate_fibonacci_levels(high_price, low_price)
            
            st.markdown("### 📐 Fibonacci Retracement Levels:")
            
            # Create columns for Fibonacci levels
            cols = st.columns(5)
            fib_items = list(fib_levels.items())
            
            for i, (level_name, level_value) in enumerate(fib_levels.items()):
                if level_name not in ['support', 'resistance']:
                    with cols[i % 5]:
                        st.metric(label=level_name, value=f"${level_value:,.2f}")
            
            st.markdown("### 📍 Current Price Analysis:")
            
            # Determine which Fibonacci level current price is closest to
            distances = {name: abs(current_price_fib - value) for name, value in fib_levels.items()}
            closest_level = min(distances, key=distances.get)
            closest_distance = distances[closest_level]
            
            st.metric(
                label=f"Closest Level: {closest_level}",
                value=f"${fib_levels[closest_level]:,.2f}",
                delta=f"${closest_distance:.2f} away"
            )
            
            # Fibonacci level interpretation
            st.markdown("### 🎯 Fibonacci Interpretation:")
            
            # Check if price is near specific levels
            for level_name, level_value in fib_levels.items():
                if level_name not in ['support', 'resistance']:
                    distance = abs(current_price_fib - level_value)
                    if distance < 500:  # If within $500 of level
                        st.success(f"🎯 PRICE NEAR {level_name} LEVEL (${level_value:,.2f}) - Potential Support/Resistance")
                    elif distance < 1000:  # If within $1000 of level
                        st.info(f"ℹ️ PRICE APPROACHING {level_name} LEVEL (${level_value:,.2f})")
            
            # Timeframe analysis
            st.markdown(f"### 🕐 Timeframe Analysis: {timeframe}")
            multiplier = calculate_timeframe_multiplier(timeframe)
            st.info(f"Timeframe multiplier: {multiplier} minutes")
            
            if multiplier <= 60:  # Short timeframes (1m-1h)
                st.warning("🔍 MAGNIFYING GLASS MODE: Short-term analysis, higher volatility expected")
            elif multiplier <= 1440:  # Medium timeframes (4h-1d)
                st.info("⚖️ BALANCED VIEW: Medium-term analysis, balanced risk/reward")
            else:  # Long timeframes (1d-1w)
                st.success(" binoculars MODE: Long-term analysis, lower volatility expected")
            
            # Multi-timeframe alignment
            st.markdown("### 🎯 Multi-Timeframe Alignment:")
            if current_price_fib > fib_levels['50.0%']:
                st.success("📈 PRICE ABOVE 50% LEVEL - Bullish bias on multiple timeframes")
            else:
                st.error("📉 PRICE BELOW 50% LEVEL - Bearish bias on multiple timeframes")
            
            if abs(current_price_fib - fib_levels['38.2%']) < 500 or abs(current_price_fib - fib_levels['61.8%']) < 500:
                st.warning("⚠️ PRICE NEAR KEY FIBONACCI LEVEL - High probability reversal zone")
