Certainly! Here are **clear Python examples** (using `statsmodels`, `seaborn`, and `pandas`) for commonly recommended linear regression diagnostic checks. Each example is annotated to clarify what you’re checking.

## 1. **Visual Check: Residuals vs. Fitted Plot**

*Checks linearity and homoscedasticity (equal error spread).*

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Example synthetic data
np.random.seed(0)
X = np.random.rand(100)
y = 2.5 * X + np.random.randn(100) * 0.3

# Fit linear regression
X_const = sm.add_constant(X)  # Adds intercept
model = sm.OLS(y, X_const)
results = model.fit()

# Get fitted values and residuals
fitted_vals = results.fittedvalues
residuals = results.resid

# Plot: Residuals vs Fitted
plt.figure(figsize=(8, 5))
sns.scatterplot(x=fitted_vals, y=residuals)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residuals vs. Fitted Values")
plt.show()
```

**Interpretation:**
If the dots are randomly scattered around 0, assumptions are likely satisfied. Patterns/fanning indicate problems.[^1][^2][^3]

## 2. **Normal Q-Q Plot of Residuals**

*Checks if residuals are roughly normally distributed (bell-shaped).*

```python
import scipy.stats as stats

# qqplot
sm.qqplot(residuals, line='45')
plt.title("Normal Q-Q")
plt.show()
```

**Interpretation:**
Points should closely follow the 45-degree line. Large departures or curves imply non-normality.[^4][^3]

## 3. **Scale-Location Plot**

*Checks for homoscedasticity (constant variance).*

```python
standardized_resid = residuals / np.std(residuals)

plt.figure(figsize=(8, 5))
plt.scatter(fitted_vals, np.sqrt(np.abs(standardized_resid)))
plt.xlabel('Fitted values')
plt.ylabel('Sqrt(Standardized Residuals)')
plt.title('Scale-Location')
plt.axhline(0, color='red', linestyle='--')
plt.show()
```

**Interpretation:**
A horizontal scatter suggests variance is constant. Patterns or fanning mean variance is changing with fitted values.[^3][^4]

## 4. **Cook’s Distance \& Leverage Plot**

*Identifies influential or outlier points.*

```python
from statsmodels.graphics.regressionplots import influence_plot

influence_plot(results)
plt.title("Outliers and Influential Points (Cook's Distance)")
plt.show()
```

**Interpretation:**
Points outside the dotted contours or far right/left could be unduly influencing the model.[^4]

## 5. **Check for Multicollinearity (Variance Inflation Factor, VIF)**

*If you have several predictors (multiple regression):*

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Example with multiple predictors
df = pd.DataFrame({
    "x1": np.random.rand(100),
    "x2": np.random.rand(100),
    "x3": np.random.rand(100)
})

# Add a constant for intercept
X_vif = sm.add_constant(df)

# Calculate VIF for each feature
vif_data = pd.DataFrame()
vif_data["feature"] = X_vif.columns
vif_data["VIF"] = [variance_inflation_factor(X_vif.values, i) for i in range(X_vif.shape[^1])]
print(vif_data)
```

**Interpretation:**
VIF > 5 or 10 suggests problematic multicollinearity.[^5][^6][^7]

## 6. **Quick Visual with seaborn’s residplot (Optional, for fast check)**

```python
import seaborn as sns
sns.residplot(x=X, y=y)
plt.xlabel("X")
plt.ylabel("Residuals")
plt.title("Seaborn Residual Plot")
plt.show()
```

**Interpretation:**
No clear pattern = good; pattern/fan shape = revisit model.[^2]

### **Notes and Further Reading**

- You may automate all diagnostic plots with `statsmodels`’s `plot_regress_exog()` or `plot_partregress_grid()` methods, especially for multiple regression.[^8]
- Statsmodels offers more diagnostic recipes and example notebooks if you want contextual guides.[^9][^3]

<div style="text-align: center">⁂</div>

[^1]: https://www.statology.org/residual-plot-python/

[^2]: https://www.geeksforgeeks.org/python/how-to-create-a-residual-plot-in-python/

[^3]: https://www.statsmodels.org/stable/examples/notebooks/generated/linear_regression_diagnostics_plots.html

[^4]: https://www.geeksforgeeks.org/machine-learning/residual-leverage-plot-regression-diagnostic/

[^5]: https://stackoverflow.com/questions/42658379/variance-inflation-factor-in-python

[^6]: https://www.geeksforgeeks.org/python/detecting-multicollinearity-with-vif-python/

[^7]: https://www.statology.org/how-to-calculate-vif-in-python/

[^8]: https://www.codecademy.com/resources/docs/python/statsmodels/diagnostic-plots

[^9]: https://www.statsmodels.org/dev/examples/notebooks/generated/linear_regression_diagnostics_plots.html

[^10]: https://nirpyresearch.com/diagnostic-plots-for-linear-regression/

[^11]: https://www.sfu.ca/~mjbrydon/tutorials/BAinPy/09_regression.html

[^12]: https://scikit-learn.org/1.5/auto_examples/linear_model/plot_ols.html

[^13]: https://stackoverflow.com/questions/46607831/python-linear-regression-diagnostic-plots-similar-to-r

[^14]: https://stackoverflow.com/questions/62681388/residual-plot-for-residual-vs-predicted-value-in-python

[^15]: http://zhiyzuo.github.io/Linear-Regression-Diagnostic-in-Python/

[^16]: https://www.codecademy.com/learn/linear-regression-mssp/modules/simple-linear-regression-mssp/cheatsheet

[^17]: https://etav.github.io/python/vif_factor_python.html

[^18]: https://www.numberanalytics.com/blog/diagnostic-plots-linear-regression

[^19]: https://www.projectpro.io/recipes/check-multicollinearity-python

[^20]: https://robert-alvarez.github.io/2018-06-04-diagnostic_plots/

