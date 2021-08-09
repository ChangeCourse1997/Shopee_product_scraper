import pandas as pd
import numpy as np
import requests
def shopee(item:str,by:str):
    """This Function takes in the item to search for and the method to sort the output, 
    this will return an excel file of 100 sorted products from shopee.

    Args:
        item (str): The item name like 'table light'
        by (str): method to sort, includes 'Sold','Total Sold','Price','Rating','Number 5 Star Ratings','Total Number of Ratings'
    """
    
    if by not in ['Sold','Total Sold','Price','Rating','Number 5 Star Ratings','Total Number of Ratings']:
        print('Please spell correctly as either Sold, Total Sold, Price,Rating, Number 5 Star Ratings, Total Number of Ratings')
        return
    name, sold, historical_sold, price, price_max, rating, rating_5, rating_4, total_number_rating,official, brand, link=[],[],[],[],[],[],[],[],[],[],[],[]
    shopee_url = 'https://shopee.sg/'
    keyword_search = item
    headers = {
    'User-Agent': 'Chrome',
    'Referer': '{}search?keyword={}'.format(shopee_url, keyword_search)
    }
    #URL to display base on keyword search and limit to 100 listings
    url = f'{shopee_url}api/v2/search_items/?by=relevancy&keyword={keyword_search}&limit=100&newest=0&order=desc&page_type=search'

    # Shopee API request
    r = requests.get(url,headers=headers).json()
    for i in r['items']:
        name.append(i['name'])
        sold.append(i['sold'])
        historical_sold.append(i['historical_sold'])
        price.append(i['price']/100000)
        price_max.append(i['price_max']/100000)
        rating.append(i['item_rating']['rating_star'])
        rating_5.append(i['item_rating']['rating_count'][5])
        rating_4.append(i['item_rating']['rating_count'][4])
        total_number_rating.append(i['item_rating']['rating_count'][0])
        official.append(i['is_official_shop'])
        brand.append(i['brand'])
        shop=i['shopid']
        item=i['itemid']
        # print(f'{shopee_url}product-i.{i['shopid']}')
        link.append(f'{shopee_url}product-i.{shop}.{item}')
    df = pd.DataFrame(name, columns=['Name'])
    df['Sold'] = sold
    df['Total Sold'] = historical_sold
    df['Price'] = price
    df['Price_max'] = price_max
    df['Rating']=rating
    df['Number 5 Star Ratings']=rating_5
    df['Number 4 Star Ratings']=rating_4
    df['Total Number of Ratings']=total_number_rating
    df['Official Shop']=official
    df['Brand']=brand
    df['Link']=link
    df=df.sort_values(by,ascending=False)
    df.to_excel('Shopee_products.xlsx',index=False)
    print('Success! :)')
    return

