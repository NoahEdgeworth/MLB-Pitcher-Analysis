# 🎯 Pitch Count vs Performance in MLB

This project explores the impact of pitch count on pitcher performance in Major League Baseball (MLB) using the [pybaseball](https://github.com/jldbc/pybaseball) Python package.

---

## 🔍 Objective

To analyze whether and how a pitcher's effectiveness changes as their pitch count increases over the course of a game. The analysis uses historical per-game pitching data and groups performances into pitch count buckets to identify potential trends.

---

## 📦 Project Structure

```
pitch_count_analysis/
│
├── data/
│   ├── raw/            # Raw data pulled from pybaseball
│   └── processed/      # Cleaned and feature-engineered datasets
│
├── notebooks/
│   └── 01_eda.ipynb    # Exploratory data analysis and visualizations
│
├── src/
│   ├── data_loader.py  # Data extraction from pybaseball and saving to disk
│   ├── analysis.py     # Functions for grouping and calculating metrics
│   └── viz.py          # Visualization functions (matplotlib, seaborn)
│
├── output/             # Final visualizations, plots, or CSVs
│
├── requirements.txt    # Python packages used
└── README.md           # This file
```

---

## 🧪 Methodology

1. **Data Collection**  
   Use `pybaseball` to fetch game-by-game pitching stats for selected MLB pitchers.

2. **Grouping by Pitch Count**  
   Aggregate performance metrics by pitch count buckets (e.g., ≤75, 76–100, >100).

3. **Metrics Tracked**  
   - ERA (Earned Run Average)  
   - WHIP (Walks + Hits per Inning Pitched)  
   - Strikeout rate  
   - Opponent batting average

4. **Analysis**  
   Compare trends in performance across pitch count groups to evaluate potential signs of fatigue or decline.

---

## 📈 Sample Questions to Explore

- Do pitchers allow more runs or baserunners as pitch counts rise?
- Is there a noticeable drop in strikeout or velocity after 100 pitches?
- Are some pitchers more resilient than others at high pitch counts?

---

## 🛠️ Requirements

Install dependencies via pip:

```bash
pip install -r requirements.txt
```

---

## 📚 Data Source

Data is retrieved using the [pybaseball](https://github.com/jldbc/pybaseball) package, which accesses public MLB stats including Statcast.

---

## 🤝 Contributions

Pull requests are welcome if you have ideas for improving the analysis, adding visualizations, or expanding to in-game pitch-by-pitch data.

---

## 📌 License

This project is for educational purposes only and uses publicly available data.
