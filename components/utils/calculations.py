import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_implied_probability(decimal_odds):
    """Calculate implied probability from decimal odds"""
    if decimal_odds <= 0:
        return 0
    return 1 / decimal_odds

def calculate_total_implied_probability(implied_probs):
    """Calculate total implied probability"""
    return sum(implied_probs)

def calculate_stakes(bankroll, implied_probs, total_implied):
    """Calculate stakes for each outcome"""
    stakes = []
    for prob in implied_probs:
        stake = (bankroll * prob) / total_implied
        stakes.append(stake)
    return stakes

def calculate_profit(stake, odds):
    """Calculate profit from a single bet"""
    return (stake * odds) - sum([s for s in calculate_stakes(stake, [1/odds], 1/odds)])

def calculate_pressure_gauge(long_oi, short_oi):
    """Calculate the Pressure Gauge: (Long OI - Short OI) / Total OI"""
    total_oi = long_oi + short_oi
    if total_oi == 0:
        return 0
    return (long_oi - short_oi) / total_oi

def calculate_trend_status(current_price, ma50):
    """Determine trend status based on MA50"""
    if current_price > ma50:
        return "BULLISH (AETOS ACTIVE)", "🟢"
    else:
        return "BEARISH (KHRUSOS ACTIVE)", "🔴"

def calculate_fibonacci_levels(high, low):
    """Calculate Fibonacci retracement levels"""
    diff = high - low
    levels = {
        '23.6%': high - (diff * 0.236),
        '38.2%': high - (diff * 0.382),
        '50.0%': high - (diff * 0.500),
        '61.8%': high - (diff * 0.618),
        '78.6%': high - (diff * 0.786),
        'support': low,
        'resistance': high
    }
    return levels

def calculate_timeframe_multiplier(timeframe):
    """Calculate multiplier for different timeframes"""
    multipliers = {
        '1m': 1,
        '5m': 5,
        '15m': 15,
        '30m': 30,
        '1h': 60,
        '4h': 240,
        '1d': 1440,
        '1w': 10080
    }
    return multipliers.get(timeframe, 60)

def calculate_rsi(prices, period=14):
    """Calculate RSI (Simplified version for demonstration)"""
    if len(prices) < period + 1:
        return 50  # Default to neutral if not enough data
    
    # Calculate simple RSI based on price changes
    gains = 0
    losses = 0
    
    for i in range(1, period + 1):
        change = prices[-i] - prices[-i-1]
        if change > 0:
            gains += change
        else:
            losses += abs(change)
    
    if losses == 0:
        return 100
    if gains == 0:
        return 0
    
    rs = gains / losses
    rsi = 100 - (100 / (1 + rs))
    return min(max(rsi, 0), 100)  # Clamp between 0 and 100

def calculate_dmi(high_prices, low_prices, close_prices, period=14):
    """Calculate DMI components (Simplified version for demonstration)"""
    if len(high_prices) < period + 1:
        return 25, 25  # Default to neutral if not enough data
    
    # Calculate simplified DMI components
    tr_sum = 0
    hd_sum = 0
    ld_sum = 0
    
    for i in range(1, period + 1):
        tr = max(
            high_prices[-i] - low_prices[-i],
            abs(high_prices[-i] - close_prices[-i-1]),
            abs(low_prices[-i] - close_prices[-i-1])
        )
        tr_sum += tr
        
        hd = high_prices[-i] - high_prices[-i-1]
        ld = low_prices[-i-1] - low_prices[-i]
        
        if hd > 0 and hd > ld:
            hd_sum += hd
        if ld > 0 and ld > hd:
            ld_sum += ld
    
    if tr_sum == 0:
        return 0, 0
    
    pdi = (hd_sum / tr_sum) * 100 if tr_sum != 0 else 0
    mdi = (ld_sum / tr_sum) * 100 if tr_sum != 0 else 0
    
    return min(pdi, 100), min(mdi, 100)

def calculate_volume_analysis(current_volume, volume_history):
    """Calculate volume analysis: current vs average, delta, and MA comparison"""
    if len(volume_history) < 2:
        return 50, "NEUTRAL", "NEUTRAL"  # Default values
    
    avg_volume = sum(volume_history) / len(volume_history)
    
    # Volume vs average
    volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
    if volume_ratio > 1.5:
        volume_status = "HIGH"
    elif volume_ratio < 0.7:
        volume_status = "LOW"
    else:
        volume_status = "AVERAGE"
    
    # Volume delta (trend)
    recent_avg = sum(volume_history[-5:]) / min(5, len(volume_history))
    older_avg = sum(volume_history[:5]) / min(5, len(volume_history))
    
    if recent_avg > older_avg * 1.2:
        delta_status = "INCREASING"
    elif recent_avg < older_avg * 0.8:
        delta_status = "DECREASING"
    else:
        delta_status = "STABLE"
    
    return volume_ratio, volume_status, delta_status

def calculate_vwap(prices, volumes):
    """Calculate VWAP (Volume Weighted Average Price)"""
    if len(prices) != len(volumes) or len(prices) == 0:
        return sum(prices) / len(prices) if prices else 0
    
    total_value = sum(p * v for p, v in zip(prices, volumes))
    total_volume = sum(volumes)
    
    return total_value / total_volume if total_volume > 0 else sum(prices) / len(prices)

def process_arbitrage_calculation(odds_list, bankroll):
    """Process the complete arbitrage calculation"""
    try:
        # Log calculation attempt
        logger.info(f"Calculation attempt: odds={odds_list}, bankroll={bankroll}")
        
        # Calculate implied probabilities
        implied_probs = [calculate_implied_probability(odd) for odd in odds_list]
        
        # Calculate total implied probability
        total_implied = calculate_total_implied_probability(implied_probs)
        
        # Check for arbitrage
        is_arb_found = total_implied < 1.0
        
        if is_arb_found:
            # Calculate stakes
            stakes = calculate_stakes(bankroll, implied_probs, total_implied)
            
            # Calculate profit (same for all outcomes in valid arb)
            profit = (stakes[0] * odds_list[0]) - bankroll
            
            return {
                'is_arb_found': True,
                'stakes': stakes,
                'profit': profit,
                'total_implied': total_implied,
                'implied_probs': implied_probs,
                'error': None
            }
        else:
            return {
                'is_arb_found': False,
                'stakes': [],
                'profit': 0,
                'total_implied': total_implied,
                'implied_probs': implied_probs,
                'error': None
            }
    except Exception as e:
        logger.error(f"Calculation error: {str(e)}")
        return {
            'is_arb_found': False,
            'stakes': [],
            'profit': 0,
            'total_implied': 0,
            'implied_probs': [],
            'error': str(e)
        }
