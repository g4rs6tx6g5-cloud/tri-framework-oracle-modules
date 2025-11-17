import streamlit as st
from utils.calculations import (
    calculate_implied_probability, 
    calculate_total_implied_probability, 
    calculate_stakes, 
    calculate_profit,
    process_arbitrage_calculation
)

def arbitrage_tab():
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        num_outcomes = st.radio(
            "Number of Outcomes:",
            options=[2, 3],
            index=0,
            horizontal=True
        )
        
        st.markdown("---")
        st.markdown("**Example Setup:**")
        st.markdown("- Odds: 2.0, 3.0, 4.0")
        st.markdown("- Bankroll: £100")
        st.markdown("- Expected: Arbitrage found!")
        
        st.markdown("---")
        st.markdown("*Personal Learning Tool*")
        st.markdown("For educational purposes only")
    
    # Main input area
    col1, col2, col3 = st.columns([1, 1, 1])
    
    # Get odds inputs based on selection
    odds_inputs = []
    
    with col1:
        odd1 = st.number_input(
            "Outcome A Odds:",
            min_value=0.01,
            max_value=100.0,
            value=2.0,
            step=0.01,
            format="%.2f",
            key="odd1"
        )
        odds_inputs.append(odd1)
    
    with col2:
        odd2 = st.number_input(
            "Outcome B Odds:",
            min_value=0.01,
            max_value=100.0,
            value=3.0,
            step=0.01,
            format="%.2f",
            key="odd2"
        )
        odds_inputs.append(odd2)
    
    if num_outcomes == 3:
        with col3:
            odd3 = st.number_input(
                "Outcome C Odds:",
                min_value=0.01,
                max_value=100.0,
                value=4.0,
                step=0.01,
                format="%.2f",
                key="odd3"
            )
            odds_inputs.append(odd3)
    else:
        odds_inputs.append(None)  # Placeholder for 2-outcome case
    
    # Remove None values for 2-outcome case
    if num_outcomes == 2:
        odds_inputs = [odd for odd in odds_inputs if odd is not None]
    
    # Bankroll input
    bankroll = st.number_input(
        "Total Bankroll (£):",
        min_value=0.01,
        value=100.0,
        step=1.0,
        format="%.2f",
        key="bankroll"
    )
    
    # Calculate button
    if st.button("🔮 Calculate Arbitrage", type="secondary"):
        with st.spinner("Processing mathematical calculations..."):
            result = process_arbitrage_calculation(odds_inputs, bankroll)
            
            if result['error']:
                st.markdown(
                    f'<div class="error-container"><strong>Error:</strong> {result["error"]}</div>',
                    unsafe_allow_html=True
                )
            else:
                # Display results
                if result['is_arb_found']:
                    st.markdown(
                        '<div class="success-container"><h3>✅ ARBITRAGE OPPORTUNITY FOUND!</h3></div>',
                        unsafe_allow_html=True
                    )
                    
                    st.markdown("### 📊 Results:")
                    
                    # Display implied probabilities
                    st.markdown("#### Implied Probabilities:")
                    prob_cols = st.columns(len(odds_inputs))
                    for i, (odd, prob) in enumerate(zip(odds_inputs, result['implied_probs'])):
                        with prob_cols[i]:
                            st.metric(
                                label=f"Outcome {chr(65+i)}",
                                value=f"{prob:.2%}",
                                delta=f"Odds: {odd}"
                            )
                    
                    # Display total implied probability
                    st.markdown(f"**Total Implied Probability:** {result['total_implied']:.2%}")
                    st.markdown(f"**Market Efficiency:** {(1 - result['total_implied']):.2%} potential profit")
                    
                    # Display stakes and profit
                    st.markdown("#### Recommended Stakes:")
                    stake_cols = st.columns(len(odds_inputs))
                    for i, (stake, odd) in enumerate(zip(result['stakes'], odds_inputs)):
                        with stake_cols[i]:
                            st.metric(
                                label=f"Stake on {chr(65+i)}",
                                value=f"£{stake:.2f}",
                                delta=f"Odds: {odd}"
                            )
                    
                    st.markdown(
                        f"### 💰 Guaranteed Profit: £{result['profit']:.2f} ({(result['profit']/bankroll)*100:.2f}%)"
                    )
                    
                else:
                    st.markdown(
                        f'<div class="error-container"><h3>❌ NO ARBITRAGE FOUND</h3><p>Total Implied Probability: {result["total_implied"]:.2%}</p></div>',
                        unsafe_allow_html=True
                    )
                    
                    # Show why no arb exists
                    if result['total_implied'] > 1.0:
                        inefficiency = (result['total_implied'] - 1.0) * 100
                        st.info(f"This market has {inefficiency:.2f}% overround - bookmaker's edge")
