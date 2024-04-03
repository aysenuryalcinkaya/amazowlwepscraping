from selenium import webdriver
import csv
from selenium.webdriver.common.by import By

# CSV dosyasını oku
with open('links1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # Her satırı dolaş
    for row in reader:
        category = row['Category']
        title = row['Title']
        link = row['Link']
        
        print(f"Opening: {title} in category: {category}")
        
        # Selenium kullanarak tarayıcıyı aç
        driver = webdriver.Chrome()  # Chrome kullanıyorsanız, tarayıcıya uygun sürümü yükleyin
        
        driver.get(link)
         # Subtitle'ı bul
        subtitle = driver.find_element(By.CLASS_NAME, "headline.grey--text.text--darken-3").text.strip()
        print(subtitle)
        if subtitle.startswith("SOP"):
           pass
            # content_div = driver.find_element(By.CLASS_NAME, "contents")
            # content_text = content_div.text
            
            # # İçeriği see-also id'sine sahip olan h3'e kadar al
            # try:
            #     see_also_heading = content_div.find_element(By.ID, "see-also")
            #     content_text = content_text.split(see_also_heading.text)[0].strip()
            # except:
            #     pass
            
       
                          
            
                
            
        else:
            content_links = driver.find_element(By.CLASS_NAME, "contents")
            sub_links = content_links.find_elements(By.TAG_NAME, "a")
            sub_link_list = []
            for sub_link in sub_links:
                sub_link_dict = {}
                sub_link_dict['href'] = sub_link.get_attribute("href")
                sub_link_dict['text'] = sub_link.text
                sub_link_list.append(sub_link_dict)
               
                    
                    
                



            # Linkleri CSV dosyasına kaydet
            with open('sub_links1.csv', mode='w', newline='') as csvfile:
                fieldnames = ['Category', 'Title', 'Sub_Title', 'Sub_Href', 'Content']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for sub_link in sub_link_list:
                    writer.writerow({'Category': category, 'Title': title, 'Sub_Title': sub_link['text'], 'Sub_Href': sub_link['href']})
                                        
                       
        
        # Tarayıcıyı kapat
        driver.quit()
