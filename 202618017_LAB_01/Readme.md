DS605: Fundamentals of Machine Learning

Lab Assignment - 1
Data Scraping and Preprocessing using Python and Scrapy

Name: Aarushi Rana
Student Id: 202618017

Lab_01
├── book_spider.py       # Scrapy spider script
├── books_raw.csv        # Raw scraped data (140 records)
├── books_cleaned.csv    # Cleaned dataset with engineered features
├── plots_overview.jpg   # Overview visualizations
├── wordcloud.jpg        # Product description word cloud
└── LAB_01.ipynb         # Data cleaning & EDA notebook

Workflow
1. Scraping (book_spider.py): Traverses catalog pagination and product detail pages to collect titles, prices, ratings, stock status, descriptions, UPCs, and categories.
2. Data Cleaning (LAB_01.ipynb): Converts currency strings to float, maps rating text to integers (1–5), and parses stock quantities.
3. Feature Engineering: Adds stock_count, description_word_count, price_band (Budget, Average, Premium), and value_score (Rating/ Price).

Installation
pip install scrapy pandas matplotlib seaborn wordcloud

Run Scraper
scrapy runspider book_spider.py -o books_raw.csv

Run Analysis
Open and execute LAB_01.ipynb in Jupyter Notebook or Google Colab to process the raw dataset and generate visualization plots.