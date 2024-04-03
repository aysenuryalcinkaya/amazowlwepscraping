import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Tarayıcı sürücüsünün yolu
driver_path = "chromedriver"

# URL'leri bir sözlükte depolayalım
urls = {
    "Amazon Foundations": "https://wiki.amazowl.com/sop/amazon-foundations",
    "Amazon Seller Central": "https://wiki.amazowl.com/sop/seller-central/SOPs",
    "Amazon Vendor Central": "https://wiki.amazowl.com/sop/vendor-central",
    "Amazon Content": "https://wiki.amazowl.com/sop/amazon-content",
    "Amazon Advertising": "https://wiki.amazowl.com/sop/amazon-advertising",
    "Walmart Foundations": "https://wiki.amazowl.com/sop/walmart/walmart-foundations",
    "Instacart Foundations": "https://wiki.amazowl.com/sop/instacart/foundations",
    "Ecommerce Foundations": "https://wiki.amazowl.com/sop/core/ecommerce-foundations"
}
category=[]
# Chrome tarayıcısını başlat
driver = webdriver.Chrome()

for key, value in urls.items():
        # URL'yi aç
    driver.get(value)
    # Contents class'ına sahip div'i bul
    contents_div = driver.find_element(By.CLASS_NAME, "contents")
        # H1 başlıklarını bul
    h1_elements = contents_div.find_elements(By.TAG_NAME, "h1")
    for h1 in h1_elements:
            # H1 başlığını al
        title = h1.text.strip()
            # H1 başlığına ait olan linkleri bul
        links = h1.find_elements(By.XPATH, "./following-sibling::ul[1]//a")
            # Her link için başlık ve linki CSV'ye yaz
        for link in links:
            href = link.get_attribute("href")
            category.append((key, title, href))
            
for data in category:
    driver.get(data[2])
    contents_div = driver.find_element(By.CLASS_NAME, "contents")
    if contents_div.find_element(By.CLASS_NAME, 
# Tarayıcıyı kapat
driver.quit()
