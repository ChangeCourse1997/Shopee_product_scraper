# Shopee_product_scraper
This is a simple script to obtain product infromation from Shopee using Shopee's API. 

### Usage
Download main.py file and place into a directory. Start a Terminal in the same directory or start an editor.

Example code:

from main import shopee

shopee('playstation controller' , 'Sold')

### Parameters
shopee(item: str, by: str)

item is the keyword search to input 

by is the method to sort the output file. Can be any of the following: 'Sold','Total Sold','Price','Rating','Number 5 Star Ratings','Total Number of Ratings'

### Output
The output consists of an excel file with the following columns.

Name: Name of the listing 

Sold: Number sold a month

Total Sold: Total number of item sold

Price: The Price of the product 

Price_max: The maximum price of a variation of the product

Rating: The rating number from 0-1

Number 5 Star Ratings: Number of 5 star ratings

Number 4 Star Ratings: Number of 4 star ratings

Total Number of Ratings: Total number of ratings of the product

Official Shop: Whether the product is from an official shop

Brand: The Brand of the product listed

Link: The link to the product 
