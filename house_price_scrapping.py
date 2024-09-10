from bs4 import BeautifulSoup
import json
import numpy as np
import requests
import pandas as pd

with open("CauGiay_house_price.html", "r", encoding="utf-8") as file:
    webpage = file.read()

# Parse the HTML content with BeautifulSoup 
soup = BeautifulSoup(webpage, 'html.parser')


links = soup.find_all("a", attrs={'class': ''})
links
data = []


for link in links:
    # địa chỉ
    add = link.find("span", class_="text-om-t16 text-om-ink-400s line-clamp-1 overflow-ellipsis")
    address = add.text if add else ''
    
    # Tên Nhà
    Property_name = link.find("h3", class_="flex-1")
    Name_of_Property = Property_name.text if Property_name else ''
    
    # Số tầng
    floor = link.find("div", class_="text-om-t14 om-dsm:text-om-t16 text-om-ink-400s ml-1 whitespace-nowrap")
    floor_num = floor.text if floor else ''
    # Diện tích
    Area = link.find("div", class_="text-om-t14 om-dsm:text-om-t16 text-om-ink-400s ml-1")
    Area_m2 = Area.text if Area else ''
    # Giá
    Price_raw = link.find("strong", class_="font-medium text-om-t20 om-xl:text-om-t24 text-om-blue-500")
    Price = Price_raw.text if Price_raw else ''
    # Hướng
    lol = link.find("div", class_="text-om-t14 om-dsm:text-om-t16 text-om-ink-400s ml-1 overflow-ellipsis line-clamp-1")
    Direction = lol.text if lol else ''
    # Collect the data
    data.append({
        "Địa chỉ": address,
        "Tên Nhà": Name_of_Property ,
        "Số tầng": floor_num,
        "Diện tích đất (m2)": Area_m2,
        "Giá": Price,
        "Hướng":Direction
        
    })
# clean data and save to csv
housing_df = pd.DataFrame.from_dict(data)
housing_df['Tên Nhà'].replace('', np.nan, inplace=True)
housing_df = housing_df.dropna(subset=['Tên Nhà'])
housing_df['Giá'].replace('', np.nan, inplace=True)
housing_df = housing_df.dropna(subset=['Giá'])
housing_df.to_csv("CauGiay_house_price.csv", header=True, index=False)


        
        



