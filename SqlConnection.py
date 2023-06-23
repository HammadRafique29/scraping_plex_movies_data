import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-T1QLR7U;'
                      'Database=MoviesSite;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

names = []
dur = []
rating = []
des = []
writers = []
directors = []
studio = []
genre = []

try:
    with open("saved_Data/Names.txt", "r") as file:
        names = file.readlines()
        file.close()
    with open("saved_Data/Duration.txt", "r") as file:
        dur = file.readlines()
        file.close()
    with open("saved_Data/Rating.txt", "r") as file:
        rating = file.readlines()
        file.close()
    with open("saved_Data/Descriptiom.txt", "r") as file:
        des = file.readlines()
        file.close()
    with open("saved_Data/Directors.txt", "r") as file:
        directors = file.readlines()
        file.close()
    with open("saved_Data/Writers.txt", "r") as file:
        writers = file.readlines()
        file.close()
    with open("saved_Data/Studio.txt", "r") as file:
        studio = file.readlines()
        file.close()
    with open("saved_Data/Genre.txt", "r") as file:
        genre = file.readlines()
        file.close()
except Exception as e:
    print(e)
    pass

# query = "INSERT INTO MOVIES VALUES ("
#
# for i in range(150, len(names)): #
#     try:
#         query += str(i) + ", "
#         query += "'" + names[i].replace("\n", "").replace("'", "") + "', "
#         query += "'" + dur[i].replace("\n", "").replace("'", "") + "', "
#         query += "'" + rating[i].replace("\n", "").replace("%", "") + "', "
#         query += "'" + des[i].replace("\n", "").replace("'", "") + "', "
#         query += "'" + writers[i].replace("\n", "").replace("'", "") + "', "
#         query += "'" + directors[i].replace("\n", "").replace("'", "") + "', "
#         query += "'" + studio[i].replace("\n", "").replace("'", "") + "', "
#         query += "'img/Posters/" + names[i].replace("\n", "").replace("'", "") + str(i) + ".jpg', "
#         query += "'img/Posters/" + names[i].replace("\n", "").replace("'", "") + ".jpg', "
#         query += "'video/trailers/" + names[i].replace("\n", "").replace("'", "") + ".mp4') "
#         print(query)
#         cursor.execute(query)
#         cursor.commit()
#         query = "INSERT INTO MOVIES VALUES ("
#     except Exception as e:
#         print(e)
#         pass


action = 1
adventure = 2
horror = 3
mystery = 4
drama = 5
comedy = 6
anime = 7
crime = 8
family = 9
martialArts = 10
Thriller = 11
Western = 12

def insert(query):
    cursor.execute(query)
    cursor.commit()

query2 = ""
for i in range(0, len(names)):
    try:
        item = genre[i].replace("\n", "").split(",")
        for val in item:
            if val == "Action":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(action) + ")"
                print(query2)
                insert(query2)
            if val == "Adventure":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(adventure) + ")"
                print(query2)
                insert(query2)
            if val == "Horror":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(horror) + ")"
                print(query2)
                insert(query2)
            if val == "Mystery":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(mystery) + ")"
                print(query2)
                insert(query2)
            if val == "Drama":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(drama) + ")"
                print(query2)
                insert(query2)
            if val == "Comedy":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(comedy) + ")"
                print(query2)
                insert(query2)
            if val == "Animation":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(anime) + ")"
                print(query2)
                insert(query2)
            if val == "Crime":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(crime) + ")"
                print(query2)
                insert(query2)
            if val == "Family":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(family) + ")"
                print(query2)
                insert(query2)
            if val == "Martial Arts":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(martialArts) + ")"
                print(query2)
                insert(query2)
            if val == "Thriller":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(Thriller) + ")"
                print(query2)
                insert(query2)
            if val == "Western":
                query2 += "INSERT INTO GENRE_RELATION VALUES (" + str(i) + ", " + str(Western) + ")"
                print(query2)
                insert(query2)
            else:
                query2 = ""
    except Exception as e:
        print(e)
        pass




