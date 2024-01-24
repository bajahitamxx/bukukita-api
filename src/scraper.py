import requests
from bs4 import BeautifulSoup

def get_html():
    r = requests.get("https://www.bukukita.com/searchresult.php?page=2&id=1&key=anak&match=2")

    #ambil html
    f = open("bukukitaDetail.html", "w", encoding="utf-8")
    f.write(r.text)
    f.close()
    return r.text

def get_detail(url):
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "html.parser")
    #print(soup)
    products = soup.find("div", "row product-info-outer").find_all("div")

    datadic ={}
    for product in products:
        key = product.find("div", "col-xs-5 col-md-3")
        value = product.find("div", "col-xs-7 col-md-9")
        if key and value != None:
            datadic[key.text.strip()] = value.text.strip()
    return datadic

def get_product_link(html_content):
    #r = requests.get("https://www.bukukita.com/searchresult.php?page=2&id=1&key=anak&match=2")

    # f = open("bukukitaAllLink.html", "w", encoding="utf-8")
    # f.write(r.text)
    # f.close()
    source = open("bukukitaAllLink.html", "r")
    soup = BeautifulSoup(html_content, "html.parser")
    
    product_container = soup.find("div",id="pageContent")
    products = soup.find_all("div","product-preview-wrapper")
    #print(products)
    datalink = []
    url = "https://www.bukukita.com/"
    for link in products:
        link_product = url + link.find("div", "ellipsis").find("a")["href"]
        #print(link_product)
        datalink.append(link_product)
    return datalink

def main():
    html_content = get_html()
    links = get_product_link(html_content=html_content)
    for link in links:
        product = get_detail(url=link)
        print(product)
    


if __name__ == "__main__":
    main()



# html_content = get_html()
# result = get_detail(html_content)
# print(result)