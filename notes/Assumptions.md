<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Can you explain the assumptions of linear regression please?

Great question! Linear regression makes some key assumptions about the data. These are like “ground rules” that help ensure its results and predictions are trustworthy. Here’s a simple, layman’s explanation for each:

### 1. **Linearity**

- **What it means:** The relationship between your input(s) and what you’re trying to predict should be roughly a straight line.
- **Simple example:** If you double the input, the output should (roughly) double, too.
- **Why it matters:** If the relationship is curved or more complex, a straight line won’t fit well, and predictions will be off.[^2][^5]


### 2. **Homoscedasticity** (Equal Variance)

- **What it means:** The scatter (spread) of the errors—how far off the predictions are from the actual data—should stay about the same, no matter whether the input is small or large.
- **Simple example:** Imagine mistakes in your predictions are always about ±5 units, whether the input is 1 or 100. But if for small inputs the errors are ±2, and for large inputs they’re ±20, this assumption is broken.
- **Why it matters:** If this doesn’t hold, your line may fit some parts of the data well and do badly on others, and your uncertainty estimates become misleading.[^5][^2]


### 3. **Normality of Errors**

- **What it means:** After fitting the line, the leftover errors (differences between predicted and actual values) should look like a “bell curve” (normal distribution)—mostly small errors, with big errors rare and balanced above and below zero.
- **Simple example:** Imagine you ask a friend to guess your age. If most of their guesses are close, with fewer guesses way too high or too low, that’s “normality.”
- **Why it matters:** This especially helps when you want to test hypotheses and build confidence intervals around your predictions.[^2][^5]


### 4. **Independence of Errors**

- **What it means:** The leftover errors (residuals) for each data point should be independent. If you know the error for one prediction, it should tell you nothing about the next.
- **Simple example:** If you weigh apples in a batch and your scale drifts over time making every next apple a bit more wrong, errors aren’t independent.
- **Why it matters:** If errors are connected, the model can underestimate overall uncertainty and make misleading inferences—especially in time series data.[^5][^2]


### 5. **No (or Little) Multicollinearity** (for multiple inputs only)

- **What it means:** If you have several input features, they shouldn’t be almost the same as each other. Each should add new, unique information.
- **Simple example:** Suppose you use both “height in cm” and “height in inches” as features—they give nearly identical information, which confuses the model.
- **Why it matters:** Too-similar features can make the calculations unstable and make it hard to know what each feature really “contributes”.[^6][^5]

**In short:**

- The relationship should be roughly straight,
- Errors should have equal spread everywhere, form a bell curve, and be unrelated to each other,
- Features should all provide new information—not be almost copies.

Let me know if you want a deep dive into any of these, or practical checks/visualizations for them!

<div style="text-align: center">⁂</div>

[^1]: https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/assumptions-of-linear-regression/

[^2]: https://www.geeksforgeeks.org/machine-learning/assumptions-of-linear-regression/

[^3]: https://people.duke.edu/~rnau/testing.htm

[^4]: https://en.wikipedia.org/wiki/Linear_regression

[^5]: https://www.jmp.com/en/statistics-knowledge-portal/what-is-regression/simple-linear-regression-assumptions

[^6]: https://www.youtube.com/watch?v=sDrAoR17pNM

[^7]: https://online.stat.psu.edu/stat500/lesson/9/9.2/9.2.3

[^8]: https://statistics.laerd.com/spss-tutorials/linear-regression-using-spss-statistics.php

