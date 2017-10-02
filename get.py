import requests
import sys
from lxml import html
import time
from fake_useragent import UserAgent


# Display result in stdout
def debug_aff(all_products):

    i = 0
    for product in all_products:
        i += 1
        for key, value in product.items():
            print (key, ": ", value)
        print("\n")
    print ("Number of products:", i, "\n")


#Check the mode and put data
def output_mode(
        mode, all_products, max_items, next_url):

    if (mode == "2" and max_items == 0):
        with open("results.txt", "a") as result:
            for product in all_products:
                if product["Writed"] == "0":
                    product["Writed"] = "1"
                    for key, value in product.items():
                        result.write(key)
                        result.write(": ")
                        result.write(value + "\n")
                    result.write("\n\n")
            result.close()
    elif (mode == "1") and (max_items == 0 or not next_url):
        debug_aff(all_products)
    elif (mode == "1") and max_items != 0:
        sys.stdout.write(' ' * 50)
        print("Products remaining to be loaded:" , max_items, end ="       \r")


# Fill info_products with current item
def put_in_data(
        all_infos, info_products, i):

    info_products.append({
                "Seller name": all_infos[0][i], "Seller URL" : all_infos[1][i],
                "Price" : all_infos[2][i], "Item URL" : all_infos[3][i],
                "Image URL": all_infos[4][i], "Description" : all_infos[5][i],
                "Writed" : "0"
                        })

# Check current item is not already in all_products
def not_in_allproducts(
        all_infos, all_products, i):

    for product in all_products:
        if product["Item URL"] == all_infos[3][i]:
            return (0)
    return (1)


def pop_first_elmt(items, number):

    shop        = '#SHOPNAME#'
    shop_url    = '#SHOPURL#'
    price       = '#ITEMPRICE#'                                                 #TO DO: find other way to get infos without first elmt
    img_url     = '#IMGURL#'
    for i in range(number):
        if items[i][0] in {shop, shop_url, price, img_url}:
            items[i].pop(0)

# Group all_infos lists on info_product
def fill_items(
        all_infos, info_products, source, max_items, mode, url):

    pop_first_elmt(all_infos, 4)
    for i in range(len(all_infos[0])):
        if max_items == 0:
            break
        all_infos[0][i] = ''.join(all_infos[0][i].split())                     # Clear seller name string (\t\n)
        if not_in_allproducts(all_infos, info_products, i):
            put_in_data(all_infos, info_products, i)
            if max_items > 0:
                max_items -= 1
    next_url = source.xpath('//div[@class="nextPage"]/a/@href')
    output_mode(mode, info_products, max_items, next_url)
    if next_url and (max_items == -1 or max_items != 0):
        url = 'https://search.rakuten.co.jp' + next_url[0]
        url = info_from_url(url, info_products, max_items, mode)
    return (url)


# Parse xml, fill array with different infos of the product
def get_all_info(url, all_infos):
    ua = UserAgent()
    header = {'UserAgent' : str(ua.chrome)}
    page = requests.get(url, headers=header)
    source = html.fromstring(page.content)
    all_infos.append(source.xpath('//span[@class="txtIconShopName"]/a/text()'))         # Seller Name
    all_infos.append(source.xpath('//span[@class="txtIconShopName"]/a/@href'))          # Seller URL
    all_infos.append(source.xpath('//p[@class="price"]/a/text()'))                      # Price
    all_infos.append(source.xpath('//div[@class="rsrSResultPhoto"]/a/@href'))           # URL item
    all_infos.append(source.xpath('//div[@class="rsrSResultPhoto"]/a/img/@src'))        # URL image
    all_infos.append(source.xpath('//div[@class="rsrSResultPhoto"]/a/img/@alt'))        # Description
    return (source)

def info_from_url(
        url, info_products, max_items, mode):

    all_infos = []
    source = get_all_info(url, all_infos)
    while len(all_infos[0]) == 0:
        if (mode != 0):
            print ("Error: the information couldn't be recovered")
            print ("Number of unloaded products: ", max_items)
            print ("New attempt ...")
        time.sleep(2)
        all_infos = []
        source = get_all_info(url, all_infos)
    url = fill_items(all_infos, info_products, source, max_items, mode, url)
    return (url)
