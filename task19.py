import requests
from bs4 import BeautifulSoup
import csv

url = 'https://lalafo.kg/bishkek/mobilnye-telefony-i-aksessuary/q-htc?currency=KGS'

def get_html():
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')

    pages = soup.find('ul', class_='pagn').find('li', class_='pagn-page').find_all('a')[-1].get('href')
    total_pages = pages.split('=')[-1]
    
    return int(total_pages)

def wriiter_csv(data):
    with open('lalafo.csv', 'a') as f:
        writter = csv.writter(f)
        writter.writerow((data['title'],
                          data['url'],
                          data['price']))

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    wer = soup.find_all('article', class_='listing-item')

    for i in wer:
        try:
            title = i.find('article', class_='listing-item').find('a', id='artice-id').text.strip()
        except:
            title = 'Title'
        try:
            url = i.find('img', class_='listing-item-photo').get('src').strip()
        except:
            url = 'Url'
        try:
            price = i.find('article', class_='listing-item').find('p', class_='listining-item-title').text.strip()
        except:
            price = 'Price'

        data = {'title': title,
                'url': url,
                'price': price}

        write_csv(data)



def main():
    url =  'https://lalafo.kg/bishkek/mobilnye-telefony-i-aksessuary/q-htc?currency=KGS'
    base_url = 'https://lalafo.kg/bishkek/q-htc'
    page_part = '?currency=KGs&page=1'


    for i in range(1, 3 ):
        url_gen = base_url + page_part + str(i)
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)








    if __name__=='__main__':
        main()





























































































# import requests
# from bs4 import BeautifulSoup

# url = 'https://lalafo.kg/bishkek/mobilnye-telefony-i-aksessuary/q-htc?currency=KGS'


# def get_html():
#     r = requests.get(url)
#     return r.text




# def get_content(html):
#     soup = BeautifulSoup(html, "html.parser")
#     bloks = soup.find