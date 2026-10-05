# 🌍 Global Energy Consumption Analysis (1965 - 2023)

## 📌 Project Overview
This Python project analyzes historical global energy consumption data spanning from 1965 to 2023. The project involves data reshaping, data cleaning, automated trend visualizations, and country-level growth rate calculations.

## 📊 Visualizations

### Top Energy Consumers in 2023
![Top Energy Consumers](top_consumers_2023.png)

### Global Energy Consumption Over Time
![Global Energy Trend](GEC%20over%20time.png)

### China vs US Energy Consumption
![China vs US Comparison](china_vs_USA_gec_over_time.png)

## 🔑 Key Features & Technical Implementation

* **Data Reshaping & Unpivoting (`pandas.melt`):** Transformed wide-format time-series matrix data into clean long-format structure for structured analysis.
* **Data Cleaning & Type Conversion:** Handled non-numeric values and missing entries (`errors="coerce"`, `dropna()`).
* **Exploratory Data Analysis & Visualizations (`seaborn` / `matplotlib`):**
  * **Top Energy Consumers (2023):** Bar chart highlighting the highest energy-consuming nations.
  * **Global Consumption Trend:** Line plot tracking total world energy trends over decades.
  * **Comparative Analysis (China vs. US):** Multi-line plot analyzing historical consumption trajectories between leading economies.
* **Automated Growth Calculation Function:** Custom Python function calculating historical growth percentage between the initial and latest available record.

## 🛠️ Tools & Technologies Used
* **Python 3**
* **Pandas:** Data manipulation, transformation, and numerical conversion.
* **Seaborn & Matplotlib:** Data visualization and plot styling.

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/jgou17/world-energy-consumption-analysis.git](https://github.com/jgou17/world-energy-consumption-analysis.git)
