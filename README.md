# Flask Flipkart Review scraper app

Welcome to our Flask web application repository! This application allows you to scrape reviews from the filpkart . User needs to provide the link of review page and number of pages he wants to scrape.

## Table of Contents

- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Hosted App](#Hosted-App)

## Getting Started

These instructions will help you set up a local copy of the project on your machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 
- pip 

### Installing

1. Clone this repository:

   ssh
   git clone git@github.com:Mahi-29/review_Scraper_project_flask.git

2. Navigate to the project directory:
    cd review_Scraper_project_flask

3. Install the required dependencies:
    pip install -r requirements.txt

### Usage

1. Run the application:
    python application.py

2. Open your web browser and go to http://localhost:5000.

3. once form is open provide a filpkart review page link like : https://www.flipkart.com/samsung-galaxy-s22-plus-5g-phantom-black-128-gb/product-reviews/itm4001e68fda319?pid=MOBGBKQF3QM4GHWN&lid=LSTMOBGBKQF3QM4GHWNJ56YXY&marketplace=FLIPKART

4. enter number of pages you want to scrape
5. now application will show thee table of all review

### Hosted App

Here is the hosted app link : http://reviewscraper-env-2.eba-j4gd6epd.us-east-1.elasticbeanstalk.com

App is hosted using AWS code pipeline and Elastic Beanstalk


