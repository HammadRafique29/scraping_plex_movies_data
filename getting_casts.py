import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


valid_urls = []

def main_function(urls):
    for url in urls:
        url = url.replace("\n", "")
        print(f"Going through {url}")
        if url not in valid_urls:
            valid_urls.append(url)
            driver = webdriver.Chrome()
            driver.minimize_window()
            driver.get(url)
            time.sleep(20)
            get_movie_casts(driver)
            print(str(len(valid_urls)) + " OUT OF " + str(len(urls)))

def get_movie_casts(driver):
    cast_links = []
    casts_container = driver.find_elements(By.XPATH,
                                           "//div[@class='p8jtya12 p8jtya9 p8jtya2u p8jtya1m p8jtya2m p8jtya2i p8jtya2a p8jtya4e p8jtya4b p8jtya48 p8jtya3e']/div[@class='CardRow_scrollerItem__AZfK2']/div[@class='p8jtya12 p8jtya9 p8jtya4m p8jtya1q p8jtya2e p8jtya2m']/div[@class='hhxvr12 p8jtya3 p8jtya7 p8jtyam p8jtyak2 p8jtyafi']/span/img")

    for item in casts_container:
        a = item.get_attribute('src')
        cast_links.append(a)

    print(cast_links)


def open_Movies_Links():
    url_list = []
    with open("saved_Data/movies_Urls_Corrected.txt", "r") as file:
        url_list = file.readlines()
        file.close()
    return url_list


movies_urls = open_Movies_Links()
main_function(movies_urls)