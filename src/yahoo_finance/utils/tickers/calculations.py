# src/utils/calculations.py

import math
import numpy as np
import src.yahoo_finance.constants as cons

class UtilsCalculations:
    @staticmethod
    def log_return(final_price, initial_price):
        """Calculate the logarithmic return between two prices."""
        return np.log(final_price / initial_price)

    @staticmethod
    def simple_return(final_price, initial_price):
        """Calculate the simple return between two prices."""
        return (final_price - initial_price) / initial_price

    @staticmethod
    def annualize_return(period_return, frequency=cons.FACTOR_DTY):
        """Annualize a periodic log return (default daily frequency: 252)."""
        return period_return * frequency

    @staticmethod
    def annualize_volatility(period_volatility, frequency=cons.FACTOR_DTY):
        """Annualize a periodic volatility."""
        return period_volatility * math.sqrt(frequency)

    @staticmethod
    def compound_annual_growth_rate(final_value, initial_value, periods):
        """Calculate the Compound Annual Growth Rate (CAGR)."""
        return (final_value / initial_value) ** (1 / periods) - 1

    @staticmethod
    def future_value(present_value, rate, periods):
        """Calculate the future value of a present amount."""
        return present_value * (1 + rate) ** periods

    @staticmethod
    def present_value(future_value, rate, periods):
        """Calculate the present value of a future amount."""
        return future_value / (1 + rate) ** periods

    # ✅ Retornos compuestos (usados cuando retorno es simple, no log)
    @staticmethod
    def annualize_return_from_monthly(monthly_return):
        """Annualize a monthly return using compounding."""
        return monthly_return*cons.FACTOR_MTY

    @staticmethod
    def annualize_return_from_weekly(weekly_return):
        """Annualize a weekly return using compounding."""
        return weekly_return*cons.FACTOR_WTY

    # ✅ Volatilidad anualizada (raíz del número de períodos)
    @staticmethod
    def annualize_volatility_from_monthly(monthly_volatility):
        """Annualize volatility from monthly data."""
        return monthly_volatility * math.sqrt(cons.FACTOR_MTY)

    @staticmethod
    def annualize_volatility_from_weekly(weekly_volatility):
        """Annualize volatility from weekly data."""
        return weekly_volatility * math.sqrt(cons.FACTOR_WTY)

    @staticmethod
    def sharpe_ratio(portfolio_return, risk_free_rate, portfolio_volatility):
        """
        Calculate the Sharpe Ratio.
        
        Parameters:
            portfolio_return (float): Expected return of the portfolio.
            risk_free_rate (float): Risk-free rate (same frequency as return).
            portfolio_volatility (float): Standard deviation of portfolio returns.
        
        Returns:
            float: Sharpe ratio.
        """
        if portfolio_volatility == 0:
            return float('inf')
        return (portfolio_return - risk_free_rate) / portfolio_volatility
    
    @staticmethod
    def monthly_return_from_daily(daily_return, trading_days_per_month=cons.FACTOR_DTM):
        """
        Convert a daily log return into a monthly log return.
    
        Parameters:
            daily_return (float): Average daily return (log or arithmetic).
            trading_days_per_month (int): Default is 21.
        
        Returns:
            float: Estimated monthly return.
        """
        return daily_return * trading_days_per_month

    @staticmethod
    def monthly_volatility_from_daily(daily_volatility, trading_days_per_month=cons.FACTOR_DTM):
        """
        Convert daily volatility to monthly volatility.
    
        Parameters:
            daily_volatility (float): Daily standard deviation.
            trading_days_per_month (int): Default is 21.
        
        Returns:
            float: Monthly volatility.
        """
        return daily_volatility * math.sqrt(trading_days_per_month)

    @staticmethod
    def weekly_return_from_daily(daily_return, trading_days_per_week=cons.FACTOR_DTW):
        """
        Convert a daily log return into a weekly log return.
    
        Parameters:
            daily_return (float): Average daily return.
            trading_days_per_week (int): Default is 5.
        
        Returns:
            float: Estimated weekly return.
        """
        return daily_return * trading_days_per_week

    @staticmethod
    def weekly_volatility_from_daily(daily_volatility, trading_days_per_week=cons.FACTOR_DTW):
        """
        Convert daily volatility to weekly volatility.
    
        Parameters:
            daily_volatility (float): Daily standard deviation.
            trading_days_per_week (int): Default is 5.
        
        Returns:
            float: Weekly volatility.
        """
        return daily_volatility * math.sqrt(trading_days_per_week)

    @staticmethod
    def weekly_return_from_monthly(monthly_return, weeks_per_month=cons.FACTOR_MTW):
        """
    Convert a monthly return into a weekly return.
    
    Parameters:
        monthly_return (float): Average monthly return.
        weeks_per_month (float): Default is 4.2.
        
    Returns:
        float: Estimated weekly return.
        """
        return monthly_return / weeks_per_month

    @staticmethod
    def weekly_volatility_from_monthly(monthly_volatility, weeks_per_month=cons.FACTOR_MTW):
        """
    Convert monthly volatility into weekly volatility.
    
    Parameters:
        monthly_volatility (float): Monthly standard deviation.
        weeks_per_month (float): Default is 4.2.
        
    Returns:
        float: Weekly volatility.
        """
        return monthly_volatility / math.sqrt(weeks_per_month)
