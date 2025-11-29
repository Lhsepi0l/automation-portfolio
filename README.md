# Automation Portfolio (Web Scraping, Excel Automation, API Integration)

This repository contains three small but practical Python automation demos:

- Web Scraping Demo
- Excel Automation Demo
- API Integration Demo

They are designed as portfolio pieces for freelance work (Fiverr / Upwork) and can be easily customized for real clients.


## 1. Web Scraping Demo

Folder: `web_scraping_demo/`  
Script: `scrape.py`

A simple web scraper that:

- Fetches product data from a demo website
- Extracts book titles and prices
- Saves the results to a CSV file: `books_YYYYMMDD.csv`

### How to run

```bash
cd web_scraping_demo
python scrape.py
```

## 2. Excel Automation Demo

Folder: excel_automation_demo/
Script: excel_auto.py

A small Excel automation script that:

Creates sample sales data

Calculates total and average amount

Exports everything to an Excel file with:

Raw sheet (original data)

Summary sheet (metrics)

Output file name: excel_report_YYYYMMDD.xlsx

How to run

```bashcd
cd excel_automation_demo
python excel_auto.py
```

## 3. API Integration Demo

Folder: api_integration_demo/
Script: api_report.py

A lightweight API integration example that:

Fetches live FX rates (USD → EUR / KRW) from a public API

Generates a simple text report

Saves it to api_report.txt

How to run

```
cd api_integration_demo
python api_report.py
```

Installation

Clone the repository and install dependencies:

git clone https://github.com/Lhsepi0l/automation-portfolio.git
cd automation-portfolio
pip install -r requirements.txt

