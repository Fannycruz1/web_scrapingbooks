# Web Scraping Project

## Overview

This project demonstrates how to scrape data from the "Books to Scrape" website using Python. The script collects information on books such as titles, prices, and stock availability and stores the data in an Excel file. This project serves as a foundation for understanding web scraping techniques and will be used as a precursor to learning how to use web scraping for interacting with eBay's API to track arcade machine prices.

## Features

- Scrapes book titles, prices, links, and stock information from multiple pages.
- Handles "404 Not Found" errors to stop scraping when no more pages are available.
- Saves the collected data in an Excel file for easy analysis.

## Technologies Used

- **Python**: Programming language used for scripting.
- **Requests**: Library for making HTTP requests.
- **BeautifulSoup**: Library for parsing HTML and extracting data.
- **Pandas**: Library for data manipulation and saving data to Excel.

## Getting Started

### Prerequisites

Make sure you have Python installed. You will also need the following libraries:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl` (for saving to Excel)
