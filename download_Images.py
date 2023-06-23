import urllib.request

casts_url = []
movies_posters_urls = []
movie_Name = []

with open("saved_Data/Posters.txt", "r") as file:
    movies_posters_urls = file.readlines()
    file.close()

with open("saved_Data/Casts.txt", "r") as file:
    casts_url = file.readlines()
    file.close()
with open("saved_Data/Names.txt", "r") as file:
    movie_Name = file.readlines()
    file.close()

i = 89
for url in movies_posters_urls:
    imgURL = url
    name = movie_Name[i].replace("\n", "")
    urllib.request.urlretrieve(imgURL, f"Posters/{name}.jpg")
    print(f"{i} OUT OF [{len(movie_Name)}]")
    i += 1
