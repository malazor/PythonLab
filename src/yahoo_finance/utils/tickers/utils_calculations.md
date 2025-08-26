
# 📊 UtilsCalculations – Financial and Statistical Utilities

## ✅ Overview

`UtilsCalculations` is a utility class containing static methods for essential financial and statistical calculations. It is designed for integration into Python-based academic or professional projects, especially in areas like investment analysis, financial modeling, and data science.

Located in:
```
src/utils/calculations.py
```

---

## 📦 Features

The class includes the following capabilities:

### 🔹 Return Calculations

| Method | Description |
|--------|-------------|
| `log_return(final_price, initial_price)` | Calculates the logarithmic return between two prices |
| `simple_return(final_price, initial_price)` | Calculates the simple return as a percentage |

---

### 🔹 Return Annualization

| Method | Description |
|--------|-------------|
| `annualize_return(period_return, frequency=252)` | Annualizes a periodic log return (default frequency: daily) |
| `annualize_return_from_monthly(monthly_return)` | Annualizes a monthly simple return using compounding |
| `annualize_return_from_weekly(weekly_return)` | Annualizes a weekly simple return using compounding |

---

### 🔹 Volatility Annualization

| Method | Description |
|--------|-------------|
| `annualize_volatility(period_volatility, frequency=252)` | Annualizes volatility from periodic data |
| `annualize_volatility_from_monthly(monthly_volatility)` | Annualizes volatility from monthly data |
| `annualize_volatility_from_weekly(weekly_volatility)` | Annualizes volatility from weekly data |

---

### 🔹 Financial Value Calculations

| Method | Description |
|--------|-------------|
| `compound_annual_growth_rate(final_value, initial_value, periods)` | Calculates the Compound Annual Growth Rate (CAGR) |
| `future_value(present_value, rate, periods)` | Calculates the future value of a present amount |
| `present_value(future_value, rate, periods)` | Calculates the present value of a future amount |

---

## 💻 Usage Example

```python
from utils.calculations import UtilsCalculations

# Logarithmic return
log_ret = UtilsCalculations.log_return(120, 100)

# Annualized return from monthly return
annual_ret = UtilsCalculations.annualize_return_from_monthly(0.02)

# Annualized volatility from weekly volatility
annual_vol = UtilsCalculations.annualize_volatility_from_weekly(0.015)

# CAGR calculation
cagr = UtilsCalculations.compound_annual_growth_rate(final_value=1800, initial_value=1000, periods=5)
```

---

## 📁 Requirements

- Python 3.7+
- Libraries: `math`, `numpy`

---

## 🧩 Usage Tips

- This class is ideal for reuse in financial scripts or analysis tools.
- You can extend it by including more advanced metrics like Sharpe ratio, NPV, IRR, etc.

---

## ✍️ Author

Created by **Manuel Antonio Lazo Reyes** for academic and professional use in Python-based financial projects.
