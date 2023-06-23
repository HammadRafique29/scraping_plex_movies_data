from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url_for_driver = ["https://watch.plex.tv/movies-and-shows/category/comedy",
                  "https://watch.plex.tv/movies-and-shows/category/drama",
                  "https://watch.plex.tv/movies-and-shows/category/horror",
                  "https://watch.plex.tv/movies-and-shows/category/thriller",
                  "https://watch.plex.tv/movies-and-shows/category/animation",
                  "https://watch.plex.tv/movies-and-shows/category/crime"]


def get_Urls(driver):
    url_template = "https://watch.plex.tv/movie/"

    movie_Names = driver.find_elements(By.XPATH, "/html/body/div/div[2]/main/section[2]/*")
    movies_Links = []

    for item in movie_Names:
        names = item.text.split("\n")
        for name in names:
            name = name.lower()
            name = name.replace(" ", "-").replace(".", "").replace("'", "")
            url = url_template + name
            movies_Links.append(url)

    with open("movies_Urls_Corrected.txt", "a") as file:
        for link in movies_Links:
            file.write(link + "\n")


for genre_url in url_for_driver:
    driver = webdriver.Chrome()
    driver.get(genre_url)
    get_Urls(driver)

