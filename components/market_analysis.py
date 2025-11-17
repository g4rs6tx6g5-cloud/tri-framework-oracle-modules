import streamlit as st
from utils.calculations import calculate_fibonacci_levels, calculate_trend_status

def market_analysis_tab():
    st.header("📈 Market Analysis Dashboard")
    st.markdown("*Tri-Framework integration with Fibonacci alignment*")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_price = st.number_input(
            "Current BTC/USDT Price:",
            min_value=0.0,
            value=109550.0,
            step=100.0,
            format="%.2f",
            key="current_price"
        )
        
        ma50 = st.number_input(
            "MA50 Value:",
            min_value=0.0,
            value=109400.0,
            step=100.0,
            format="%.2f",
            key="ma50"
        )
    
    with col2:
        recent_high = st.number_input(
            "Recent Swing High:",
            min_value=0.0,
            value=110000.0,
            step=100.0,
            format="%.2f",
            key="recent_high"
        )
        
        recent_low = st.number_input(
            "Recent Swing Low:",
            min_value=0.0,
            value=109000.0,
            step=100.0,
            format="%.2f",
            key="recent_low"
        )
    
    if st.button("🎯 Analyze Market Structure", type="secondary"):
        with st.spinner("Analyzing market structure..."):
            # Calculate Fibonacci levels
            fib_levels = calculate_fibonacci_levels(recent_high, recent_low)
            
            # Trend analysis
            trend_status, trend_emoji = calculate_trend_status(current_price, ma50)
            
            st.markdown("### 📊 Market Structure Analysis:")
            
            # Display current market status
            st.metric("Current Price", f"${current_price:,.2f}")
            st.metric("MA50", f"${ma50:,.2f}")
            st.metric("Swing High", f"${recent_high:,.2f}")
            st.metric("Swing Low", f"${recent_low:,.2f}")
            
            # Trend analysis
            st.markdown(f"### 🎯 Trend Status: {trend_emoji} {trend_status}")
            
            # Fibonacci levels
            st.markdown("### 📐 Fibonacci Levels:")
            for level_name, level_value in fib_levels.items():
                if level_name not in ['support', 'resistance']:
                    color = "🟢" if abs(current_price - level_value) < 1000 else "⚪️"
                    st.markdown(f"<div class='fib-level'>{color} **{level_name}: ${level_value:,.2f}**</div>", unsafe_allow_html=True)
            
            # Price position relative to Fibonacci levels
            st.markdown("### 📍 Price Positioning:")
            closest_fib = min(fib_levels.values(), key=lambda x: abs(x - current_price))
            fib_distance = abs(current_price - closest_fib)
            st.info(f"Closest Fibonacci level: ${closest_fib:,.2f} (Distance: ${fib_distance:,.2f})")
            
            # Framework integration
            st.markdown("### 🔮 Tri-Framework Status:")
            if current_price > ma50:
                st.success("✅ AETOS PROTOCOL ACTIVE - Trading with primary trend")
                st.info("🎯 Strategy: Look for entries above key Fibonacci levels")
            else:
                st.warning("⚠️ KHRUSOS PROTOCOL ACTIVE - Capital preservation mode")
                st.info("🎯 Strategy: Look for entries below key Fibonacci levels")
            
            # Compression analysis
            compression_distance = recent_high - recent_low
            if compression_distance < 1000:  # Less than $1000 range
                st.warning(f"⚠️ COMPRESSION DETECTED: Only {compression_distance:.2f} points between swing high and low")
                st.info("🎯 ALPHA COMPRESSION SPRING - High probability setup when compression breaks")
            else:
                st.info(f"📊 Current Range: {compression_distance:.2f} points")
