import console
import get

if __name__ == '__main__':

    all_products = []
    url_brand = [
        'https://search.rakuten.co.jp/search/mall/-/565210/tg1000741/',        # Hermes
        'https://search.rakuten.co.jp/search/mall/-/565210/tg1002727/?p=150',        # Louis Vuitton
        'https://search.rakuten.co.jp/search/mall/-/565210/tg1000751/',        # Gucci
        'https://search.rakuten.co.jp/search/mall/-/565210/tg1000768/',        # Chanel
        'https://search.rakuten.co.jp/search/mall/-/565210/tg1000797/',        # Prada
        'https://search.rakuten.co.jp/search/mall/-/110934/tg1000741-tg'\
        '1000751-tg1000768-tg1000797-tg1002727/']                               # All brands


    console.get_argument(all_products, url_brand)
    #url_brand[7] = get.info_from_url(url_brand[7], all_products, 5, 0)
    #debug_aff(all_products)
