from playwright.sync_api import sync_playwright
import pandas as pd
import time

def main():
    
    with sync_playwright() as p:
        #Fechas que se usaran como parametros 
        checkin_date = '2024-11-20'
        checkout_date = '2024-11-24'
        
        page_url = f'https://www.booking.com/searchresults.en-us.html?checkin={checkin_date}&checkout={checkout_date}&selected_currency=USD&ss=Barcelona&ssne=Barcelona&ssne_untouched=Barcelona&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_type=city&group_adults=1&no_rooms=1&group_children=0&sb_travel_purpose=leisure'
        
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(page_url, timeout=60000)

        total_hotels_list = []
        properties_scraped = 0
        required_properties = 100
        
        def scroll_down_page(page, scroll_pause_time=2):
            page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            time.sleep(scroll_pause_time)

        while properties_scraped < required_properties:
            hotels = page.locator('//div[@data-testid="property-card"]').all()
            print(f'Scraping {len(hotels)} hoteles en la página actual.')

            hotels_list = []
            for hotel in hotels:
                hotel_dict = {}
                hotel_dict['hotel'] = hotel.locator('//div[@data-testid="title"]').inner_text()

                try:
                    hotel_dict['price'] = hotel.locator('//span[@data-testid="price-and-discounted-price"]').inner_text()
                    hotel_dict['score'] = hotel.locator('//div[@data-testid="review-score"]/div[1]').inner_text()
                    hotel_dict['avg review'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[1]').inner_text()
                    hotel_dict['reviews count'] = hotel.locator('//div[@data-testid="review-score"]/div[2]/div[2]').inner_text().split()[0]
                    hotel_dict['address'] = hotel.locator('//span[@data-testid="address"]').inner_text()
                    hotel_dict['availability'] = hotel.locator('//div[@data-testid="availability-single"]').inner_text()
                except Exception:
                    hotel_dict['price'] = 'N/A'
                    hotel_dict['score'] = 'N/A'
                    hotel_dict['avg review'] = 'N/A'
                    hotel_dict['reviews count'] = 'N/A'
                    hotel_dict['availability'] = 'N/A'
                hotels_list.append(hotel_dict)

            total_hotels_list.extend(hotels_list)
            properties_scraped = len(total_hotels_list)

            if properties_scraped >= required_properties:
                break

            scroll_down_page(page)

        df = pd.DataFrame(total_hotels_list)
        df.to_csv('data/hotels_list.csv', index=False) 
        
        browser.close()
            
if __name__ == '__main__':
    main()
