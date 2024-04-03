from selenium import webdriver
import csv
from selenium.webdriver.common.by import By


textdata=[]
# CSV dosyasını oku
with open('links.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Her satırı dolaş
    for row in reader:
        category = row['Category']
        title = row['Title']
        subtitle= row['Sub_Title']
        link = row['Sub_Href']
        
        print(f"Opening: {title} in category: {category}")
        
        # Selenium kullanarak tarayıcıyı aç
        driver = webdriver.Chrome()  # Chrome kullanıyorsanız, tarayıcıya uygun sürümü yükleyin
        driver.maximize_window()
        driver.get(link)


        content_div = driver.find_element(By.CLASS_NAME, "contents")
        content_text = content_div.text
        try:
            see_also_heading = content_div.find_element(By.ID, "see-also")
            content_text = content_text.split(see_also_heading.text)[0].strip()
                        
        except:
             pass
                    
        textdata.append((category, title, subtitle, link, content_text))    
        print(textdata)            
                   
                    
        # Tarayıcıyı kapat
driver.quit()
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Başlık satırını yaz
    writer.writerow(['Category', 'Title', 'Link', 'Subtitle', 'SubHref', 'Content'])
    # Her veriyi yaz
    for data in textdata:
        writer.writerow(data)

print("CSV dosyası oluşturuldu.")
