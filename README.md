# Task7_SalesSummary
Basic sales summary using SQLite and Python
# Task 7 – Basic Sales Summary Using SQLite and Python

This project creates a small SQLite database, runs SQL queries to summarize sales, and visualizes revenue by product using a bar chart.

## Files Included
- `sales_summary.py` – Python script that creates DB, runs SQL, and plots chart
- `sales_data.db` – SQLite database with sample sales data
- `sales_chart.png` – Bar chart showing revenue by product

##  Tools Used
- Python 3
- SQLite (via sqlite3)
- pandas
- matplotlib

##  How to Run
1. Open terminal in project folder
2. Install required libraries:
pip install pandas matplotlib   
3. Run the script:
python sales_summary.py

##  Output
- Console summary of sales:
Sales Summary: product total_qty revenue Widget
A 19 189.81 Widget
B 9 179.91 Widget
C 4 119.96
- Chart saved as `sales_chart.png`

##  Learning Outcomes
- Connect Python to SQLite
- Run SQL queries inside Python
- Use pandas to load and display SQL results
- Create bar charts with matplotlib



