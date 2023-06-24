import base64
import io
import time
from urllib import request
import urllib

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
            get_Movies_details(driver, url)
            print(str(len(valid_urls)) + " OUT OF " + str(len(urls)))


def open_Movies_Links():
    url_list = []
    with open("saved_Data/movies_Urls_Corrected.txt", "r") as file:
        url_list = file.readlines()
        file.close()
    return url_list


def get_Movies_details(driver, url):
    try:
        time.sleep(5)
        poster_tag = driver.find_element(By.XPATH,
                                         "/html/body/div/div[2]/main/section[1]/div/div[1]/div[1]/div/div/span/img")
        Poster = poster_tag.get_attribute("src")
        Name = driver.find_element(By.XPATH, "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div/div[1]/h1")
        Data = driver.find_element(By.XPATH,
                                       "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div/div[2]/div[1]/div/span")
        Data = Data.text.split('    ')
        Duration = Data[1]
        Rating = Data[2]
        # Rating = driver.find_element(By.XPATH,
        #                              "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div/div[1]/div/span[2]/span/span")
        Description = driver.find_element(By.XPATH,
                                          "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div[3]")

        print(Duration,Rating, Description.text)


        writers_container = driver.find_elements(By.XPATH,
                                                 "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div/div[4]/div[2]/span/*")  # class vbe90o0 vbe90ot vbe90o1 p8jtyafy
        directors_container = driver.find_elements(By.XPATH,
                                                   "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div[4]/div[1]/span/*")  # class vbe90o0 vbe90ot vbe90o1 p8jtyaf
        studio_container = driver.find_elements(By.XPATH,
                                                "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div[4]/div[2]/span/*")  # class TagList_name__QLHLC
        Genre = driver.find_elements(By.XPATH,
                                     "/html/body/div/div[2]/main/section[1]/div/div[1]/div[2]/div/div[2]/div[2]/span/span/*")
        casts_container = driver.find_elements(By.XPATH,
                                               "//div[@class='FullBleed_fullBleed__9YUNr']/div[@class='_1duebfh12 _1duebfh9 _1duebfh2u _1duebfh1q _1duebfh2m _1duebfh2i _1duebfh2a _1duebfh46 _1duebfh43 _1duebfh3e']/div[1]//img")

        writers = ""
        directors = ""
        studio = ""
        genre = []
        cast_links = []

        for items in writers_container:
            writers += items.text

        for items in directors_container:
            directors += items.text

        for items in studio_container:
            studio += items.text

        for items in Genre:
            genre.append(items.text)

        for item in casts_container:
            a = item.get_attribute('src')
            cast_links.append(a)

        print(cast_links)

        save_data(Name.text, Rating, Duration, Description.text, Poster, writers, directors, studio, genre,
                  len(cast_links))

        with open('saved_Data/completed.txt', 'a') as file:
            file.write("Error in" + f"{url}" + "\n")

    except Exception as e:
        with open('saved_Data/erros.txt', 'a') as file:
            file.write("Error in" + f"{url}" + "\n")
        print(e)


def save_data(name, rating, duration, des, poster, writers, directors, studio, genre, casts_total):
    with open("saved_Data/Names.txt", "a") as file:
        print(name)
        file.write(name + "\n")
        file.close()

    with open("saved_Data/Duration.txt", "a") as file:
        file.write(duration + "\n")
        file.close()

    with open("saved_Data/Rating.txt", "a") as file:
        file.write(rating + "\n")
        file.close()

    with open("saved_Data/Descriptiom.txt", "a") as file:
        file.write(des + "\n")
        file.close()

    with open("saved_Data/Writers.txt", "a") as file:
        file.write(writers + "\n")
        file.close()

    with open("saved_Data/Directors.txt", "a") as file:
        file.write(directors + "\n")
        file.close()

    with open("saved_Data/Studio.txt", "a") as file:
        file.write(studio + "\n")
        file.close()

    with open("saved_Data/Genre.txt", "a") as file:
        gn = ""
        for gen in genre:
            gen = gen.replace(",", "")
            gn += gen + ","
        file.write(gn + "\n")
        file.close()

    with open("saved_Data/Casts.txt", "a") as file:
        cst = ""
        for ct in range(0, casts_total):
            # download_images(poster, "Casts", name)
            ct = f"{name}" + str(ct)
            cst += ct + ", "
        file.write(cst + "\n")
        file.close()

    with open("saved_Data/Posters.txt", "a") as file:
        # download_images(poster, "Posters", name)
        file.write(poster + "\n")
        file.close()


def download_images(url, path, name):
    imgURL = url
    urllib.request.urlretrieve(imgURL, path + "/" + name + ".jpg")


movies_urls = open_Movies_Links()
main_function(movies_urls)
