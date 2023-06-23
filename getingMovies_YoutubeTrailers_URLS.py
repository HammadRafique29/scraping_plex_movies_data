import time
from urllib import request
import urllib

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import win32clipboard
import pyodbc
from selenium.common import NoSuchElementException
#'The+Gold+Rush+Trailer', 'Sherlock+Jr+Trailer', 'Spun+Trailer', 'Dark+Star+Trailer', 'Hick+Trailer', 'The+Little+Shop+of+Horrors+Trailer', 'Bottle+Shock+Trailer', 'The+Slumber+Party+Massacre+Trailer', 'Cat+Ballou+Trailer', 'Swiped+Trailer', 'Meet+John+Doe+Trailer', 'Hobgoblins+Trailer', 'Popeye+the+Sailor+Trailer', 'Outsourced+Trailer', "Rock+'n'+Roll+High+School+Trailer", 'Electric+Dreams+Trailer', 'My+One+and+Only+Trailer', 'Harvie+Krumpet+Trailer', 'All+Nighter+Trailer', 'Kenny+Trailer', 'A+Night+in+Casablanca+Trailer', 'Slumber+Party+Massacre+II+Trailer', 'Deep+End+Trailer', 'The+Brother+from+Another+Planet+Trailer', 'Visioneers+Trailer', 'The+Grand+Trailer', 'Already+Tomorrow+in+Hong+Kong+Trailer', 'Bodied+Trailer', 'Royal+Wedding+Trailer', 'The+Maladjusted+Trailer', 'Watch+Out+for+the+Automobile+Trailer', 'Escape+to+Athena+Trailer', 'Light+from+the+Tower+Trailer', 'Almost+Friends+Trailer', 'F+the+Prom+Trailer', 'Carpool+Trailer', 'Suburban+Gothic+Trailer', 'The+Fearless+Hyena+Trailer', 'Hard+Ticket+to+Hawaii+Trailer', "They're+Watching+Trailer", 'Permission+Trailer', "Children+Shouldn't+Play+with+Dead+Things+Trailer", 'Deal+Trailer', 'Saturday+the+14th+Trailer', 'Jesus+Christ+Vampire+Hunter+Trailer', 'Sex+and+Breakfast+Trailer', 'The+Devil+and+Miss+Jones+Trailer', 'The+10+Year+Plan+Trailer', 'Lady+for+a+Day+Trailer', "The+Men+Who+Tread+on+the+Tiger's+Tail+Trailer", "Father's+Little+Dividend+Trailer", 'Putney+Swope+Trailer', 'Zorro+Trailer', 'Made+for+Each+Other+Trailer', 'Grand+Theft+Parsons+Trailer', 'Bourek+Trailer', 'The+Amazing+Bulk+Trailer', 'Baby+on+Board+Trailer', 'Acrylic+Trailer', 'The+Inspector+General+Trailer', "It's+a+Wonderful+Life+Trailer", 'The+Girl+with+the+Dragon+Tattoo+Trailer', 'The+Man+from+Earth+Trailer', 'Metropolis+Trailer', 'Rashomon+Trailer', 'M+Trailer', 'The+Girl+Who+Played+with+Fire+Trailer', "The+Girl+Who+Kicked+the+Hornet's+Nest+Trailer", 'Diabolique+Trailer', 'Repulsion+Trailer', 'Candy+Trailer', 'Zulu+Trailer', 'Fitzcarraldo+Trailer', 'Pather+Panchali+Trailer', 'The+Chosen+Trailer', 'Elevator+to+the+Gallows+Trailer', 'Terminal+Trailer', 'A+Christmas+Carol+Trailer', 'Jesus+of+Nazareth+Trailer', 'Dark+Crimes+Trailer', 'The+Man+Who+Knew+Too+Much+Trailer', 'The+Red+Balloon+Trailer', 'A+Boy+and+His+Dog+Trailer', 'Stray+Dog+Trailer', 'Late+Spring+Trailer', 'Scarlet+Street+Trailer', 'And+Then+There+Were+None+Trailer', 'Aparajito+Trailer', 'Family+Business+Trailer', 'Letter+from+an+Unknown+Woman+Trailer', 'Drunken+Angel+Trailer', 'Fear+and+Desire+Trailer', 'One-Eyed+Jacks+Trailer', 'Tales+from+the+Crypt+Trailer', 'Alexander+Nevsky+Trailer', 'The+Man+with+the+Golden+Arm+Trailer', 'Two+Women+Trailer', 'Turnabout+Trailer', 'Death+of+a+Salesman+Trailer', 'Scrooge+Trailer', "Journey's+End+Trailer", 'Love+Songs+Trailer', 'The+Secret+of+Roan+Inish+Trailer', 'Diary+of+a+Chambermaid+Trailer', 'Broken+Arrow+Trailer', 'Othello+Trailer', 'And+God+Created+Woman+Trailer', 'Bomb+City+Trailer', 'The+Naked+Kiss+Trailer', 'The+Big+Combo+Trailer', 'The+Penitent+Man+Trailer', 'Kansas+City+Confidential+Trailer', 'Penny+Serenade+Trailer', 'Macbeth+Trailer', 'Rockaway+Trailer', 'Night+of+the+Living+Dead+Trailer', 'Nosferatu+Trailer', 'Invasion+of+the+Body+Snatchers+Trailer', 'Black+Christmas+Trailer', 'The+Last+House+on+the+Left+Trailer', 'House+on+Haunted+Hill+Trailer', 'Carnival+of+Souls+Trailer', 'Terror+Train+Trailer', 'The+Beast+of+Yucca+Flats+Trailer', 'White+Zombie+Trailer', 'Demon+Seed+Trailer', 'Four+Flies+on+Grey+Velvet+Trailer', 'The+Tingler+Trailer', 'Hell+Night+Trailer', 'The+Terror+Trailer', 'Jug+Face+Trailer', 'Girl+Next+Trailer', 'Bride+of+the+Monster+Trailer', 'The+Girl+Who+Got+Away+Trailer', "The+Brain+That+Wouldn't+Die+Trailer", "Dr+Terror's+House+of+Horrors+Trailer", '13+Ghosts+Trailer', 'Laserblast+Trailer', 'Son+of+Dracula+Trailer', 'Forbidden+World+Trailer', 'Chain+Letter+Trailer', 'The+Bat+Trailer', 'The+Killer+Shrews+Trailer',
list = ['The+Gold+Rush+Trailer', 'Sherlock+Jr+Trailer', 'Spun+Trailer', 'Dark+Star+Trailer', 'Hick+Trailer', 'The+Little+Shop+of+Horrors+Trailer', 'Bottle+Shock+Trailer', 'The+Slumber+Party+Massacre+Trailer', 'Cat+Ballou+Trailer', 'Swiped+Trailer', 'Meet+John+Doe+Trailer', 'Hobgoblins+Trailer', 'Popeye+the+Sailor+Trailer', 'Outsourced+Trailer', "Rock+'n'+Roll+High+School+Trailer", 'Electric+Dreams+Trailer', 'My+One+and+Only+Trailer', 'Harvie+Krumpet+Trailer', 'All+Nighter+Trailer', 'Kenny+Trailer', 'A+Night+in+Casablanca+Trailer', 'Slumber+Party+Massacre+II+Trailer', 'Deep+End+Trailer', 'The+Brother+from+Another+Planet+Trailer', 'Visioneers+Trailer', 'The+Grand+Trailer', 'Already+Tomorrow+in+Hong+Kong+Trailer', 'Bodied+Trailer', 'Royal+Wedding+Trailer', 'The+Maladjusted+Trailer', 'Watch+Out+for+the+Automobile+Trailer', 'Escape+to+Athena+Trailer', 'Light+from+the+Tower+Trailer', 'Almost+Friends+Trailer', 'F+the+Prom+Trailer', 'Carpool+Trailer', 'Suburban+Gothic+Trailer', 'The+Fearless+Hyena+Trailer', 'Hard+Ticket+to+Hawaii+Trailer', "They're+Watching+Trailer", 'Permission+Trailer', "Children+Shouldn't+Play+with+Dead+Things+Trailer", 'Deal+Trailer', 'Saturday+the+14th+Trailer', 'Jesus+Christ+Vampire+Hunter+Trailer', 'Sex+and+Breakfast+Trailer', 'The+Devil+and+Miss+Jones+Trailer', 'The+10+Year+Plan+Trailer', 'Lady+for+a+Day+Trailer', "The+Men+Who+Tread+on+the+Tiger's+Tail+Trailer", "Father's+Little+Dividend+Trailer", 'Putney+Swope+Trailer', 'Zorro+Trailer', 'Made+for+Each+Other+Trailer', 'Grand+Theft+Parsons+Trailer', 'Bourek+Trailer', 'The+Amazing+Bulk+Trailer', 'Baby+on+Board+Trailer', 'Acrylic+Trailer', 'The+Inspector+General+Trailer', "It's+a+Wonderful+Life+Trailer", 'The+Girl+with+the+Dragon+Tattoo+Trailer', 'The+Man+from+Earth+Trailer', 'Metropolis+Trailer', 'Rashomon+Trailer', 'M+Trailer', 'The+Girl+Who+Played+with+Fire+Trailer', "The+Girl+Who+Kicked+the+Hornet's+Nest+Trailer", 'Diabolique+Trailer', 'Repulsion+Trailer', 'Candy+Trailer', 'Zulu+Trailer', 'Fitzcarraldo+Trailer', 'Pather+Panchali+Trailer', 'The+Chosen+Trailer', 'Elevator+to+the+Gallows+Trailer', 'Terminal+Trailer', 'A+Christmas+Carol+Trailer', 'Jesus+of+Nazareth+Trailer', 'Dark+Crimes+Trailer', 'The+Man+Who+Knew+Too+Much+Trailer', 'The+Red+Balloon+Trailer', 'A+Boy+and+His+Dog+Trailer', 'Stray+Dog+Trailer', 'Late+Spring+Trailer', 'Scarlet+Street+Trailer', 'And+Then+There+Were+None+Trailer', 'Aparajito+Trailer', 'Family+Business+Trailer', 'Letter+from+an+Unknown+Woman+Trailer', 'Drunken+Angel+Trailer', 'Fear+and+Desire+Trailer', 'One-Eyed+Jacks+Trailer', 'Tales+from+the+Crypt+Trailer', 'Alexander+Nevsky+Trailer', 'The+Man+with+the+Golden+Arm+Trailer', 'Two+Women+Trailer', 'Turnabout+Trailer', 'Death+of+a+Salesman+Trailer', 'Scrooge+Trailer', "Journey's+End+Trailer", 'Love+Songs+Trailer', 'The+Secret+of+Roan+Inish+Trailer', 'Diary+of+a+Chambermaid+Trailer', 'Broken+Arrow+Trailer', 'Othello+Trailer', 'And+God+Created+Woman+Trailer', 'Bomb+City+Trailer', 'The+Naked+Kiss+Trailer', 'The+Big+Combo+Trailer', 'The+Penitent+Man+Trailer', 'Kansas+City+Confidential+Trailer', 'Penny+Serenade+Trailer', 'Macbeth+Trailer', 'Rockaway+Trailer', 'Night+of+the+Living+Dead+Trailer', 'Nosferatu+Trailer', 'Invasion+of+the+Body+Snatchers+Trailer', 'Black+Christmas+Trailer', 'The+Last+House+on+the+Left+Trailer', 'House+on+Haunted+Hill+Trailer', 'Carnival+of+Souls+Trailer', 'Terror+Train+Trailer', 'The+Beast+of+Yucca+Flats+Trailer', 'White+Zombie+Trailer', 'Demon+Seed+Trailer', 'Four+Flies+on+Grey+Velvet+Trailer', 'The+Tingler+Trailer', 'Hell+Night+Trailer', 'The+Terror+Trailer', 'Jug+Face+Trailer', 'Girl+Next+Trailer', 'Bride+of+the+Monster+Trailer', 'The+Girl+Who+Got+Away+Trailer', "The+Brain+That+Wouldn't+Die+Trailer", "Dr+Terror's+House+of+Horrors+Trailer", '13+Ghosts+Trailer', 'Laserblast+Trailer', 'Son+of+Dracula+Trailer', 'Forbidden+World+Trailer', 'Chain+Letter+Trailer', 'The+Bat+Trailer', 'The+Killer+Shrews+Trailer', 'Boo+Trailer', 'Night+of+the+Lepus+Trailer', 'Choke+Trailer', 'Empire+of+the+Ants+Trailer', 'The+Wasp+Woman+Trailer', 'Messiah+of+Evil+Trailer', 'Willard+Trailer', 'Attack+of+the+Giant+Leeches+Trailer', 'Vampire+Circus+Trailer', 'Without+Warning!+Trailer', 'The+Food+of+the+Gods+Trailer', 'The+Giant+Gila+Monster+Trailer', 'The+Baby+Trailer', 'Bonehill+Road+Trailer', 'Track+of+the+Moon+Beast+Trailer', 'The+Screaming+Skull+Trailer', 'Night+Tide+Trailer', 'Sorority+House+Massacre+Trailer', "Blood+from+the+Mummy's+Tomb+Trailer", 'Attack+of+the+Crab+Monsters+Trailer', 'Gargoyles+Trailer', "Don't+Look+in+the+Basement+Trailer", 'The+Corpse+Vanishes+Trailer', 'The+Dead+Next+Door+Trailer', 'Creature+from+the+Haunted+Sea+Trailer', 'Charade+Trailer', 'The+Lady+Vanishes+Trailer', 'Freeway+Trailer', 'Shock+Corridor+Trailer', 'Le+Doulos+Trailer', 'The+Alphabet+Killer+Trailer', 'The+Ninth+Configuration+Trailer', 'The+Woman+in+Green+Trailer', 'Terror+by+Night+Trailer', 'Forget+Me+Not+Trailer', 'Sherlock+Holmes+and+the+Secret+Weapon+Trailer', 'Alienated+Trailer', 'Suburbia+Trailer', 'The+Tall+T+Trailer', 'Wildlike+Trailer', 'Brain+Dead+Trailer', 'Sherlock+Holmes+Faces+Death+Trailer', 'Kill+Plan+Trailer', 'Woman+on+the+Run+Trailer', 'American+Satan+Trailer', 'Caught+Trailer', 'The+Frame+Trailer', 'The+Holcroft+Covenant+Trailer', 'Bayou+Caviar+Trailer', 'Pursued+Trailer', 'Ben+Trailer', 'The+Case+of+the+Bloody+Iris+Trailer', 'Hollow+Triumph+Trailer', 'Evening+Installation+Trailer', 'Warriors+of+the+Wasteland+Trailer', 'The+Killing+Jar+Trailer', 'Quarantine+Girl+Trailer', 'Sinful+Trailer', 'Rituals+Trailer', 'Tormented+Trailer', 'The+Incubus+Trailer', 'The+Amazing+Transparent+Man+Trailer', 'The+Man+Who+Cheated+Himself+Trailer', "At+Granny's+House+Trailer", 'Wither+Trailer', 'Camp+Hell+Trailer', 'Kiss+Tomorrow+Goodbye+Trailer', 'Tower+Trailer', 'Sintel+Trailer', 'Coonskin+Trailer', 'The+Mechanical+Monsters+Trailer', 'Blood+Tea+and+Red+String+Trailer', 'The+Arctic+Giant+Trailer', 'The+Hunchback+of+Notre+Dame+Trailer', 'Anastasia+Trailer', 'Anina+Trailer', 'The+Magnetic+Telescope+Trailer', 'Electric+Earthquake+Trailer', 'Gift+Wrapped+Trailer', 'Volcano+Trailer', "Noah's+Ark+Trailer", 'Terror+on+the+Midway+Trailer', 'Japoteurs+Trailer', 'The+Night+Before+Christmas+Trailer', 'Tarzan+of+the+Apes+Trailer', "Dante's+Hell+Animated+Trailer", 'The+Mummy+Strikes+Trailer', 'Eleventh+Hour+Trailer', 'Jungle+Drums+Trailer', 'The+New+Adventures+of+Peter+Rabbit+Trailer', 'Beauty+and+the+Beast+Trailer', 'The+Underground+World+Trailer', 'Vampire+Princess+Miyu+Trailer', 'Secret+Agent+Trailer', 'Hercules+Trailer', 'Goat+Story+Trailer', 'Otaku+No+Video+Trailer', 'The+Magic+Pudding+Trailer', 'The+Hunting+of+the+Snark+Trailer', 'Mars+Trailer', 'Lung+do+kei+yuen+Trailer', 'The+Prince+and+the+Pauper+Trailer', 'Ogre+Trailer', 'From+Inside+Trailer', 'Fishtales+Trailer', 'The+Puppetoon+Movie+Trailer', 'Tom+Thumb+Meets+Thumbelina+Trailer', 'The+Misty+Green+Sky+Trailer', 'Alice+Through+the+Looking+Glass+Trailer', 'The+Legend+of+Su-Ling+Trailer', 'Sherlock+Holmes+and+the+Baskerville+Curse+Trailer', 'Once+Upon+a+Time+Trailer', 'El+Crazy+Che+Trailer', 'Beetle+Bailey+Trailer', 'Sherlock+Holmes+and+a+Study+in+Scarlet+Trailer', 'Jurassic+Bark+Trailer', 'The+Christmas+Elves+Trailer', 'The+Wrong+Rock+Trailer', 'A+Tale+of+Egypt+Trailer', 'Bee+Team+2+Trailer', 'You+Only+Live+Once+Trailer', 'Force+of+Evil+Trailer', 'Suddenly+Trailer', 'The+Harder+They+Come+Trailer', 'Dressed+to+Kill+Trailer', 'He+Walked+by+Night+Trailer', 'Walking+Tall+Trailer', 'The+Street+Fighter+Trailer', 'Too+Late+for+Tears+Trailer', 'Impact+Trailer', 'Lured+Trailer', 'Teenagers+from+Outer+Space+Trailer', "Another+Man's+Poison+Trailer", 'Indestructible+Man+Trailer', 'The+Big+Bird+Cage+Trailer', 'Jail+Bait+Trailer', 'The+Young+Savages+Trailer', 'The+Penalty+Trailer', 'They+Made+Me+a+Criminal+Trailer', 'Sweet+Karma+Trailer', 'Return+of+the+Street+Fighter+Trailer', 'Beast+from+Haunted+Cave+Trailer', 'Women+in+Cages+Trailer', 'Dick+Tracy+Meets+Gruesome+Trailer', 'Death+Valley+Trailer', 'Man+in+the+Attic+Trailer', 'Eyes+in+the+Night+Trailer', 'Mad+Dog+Morgan+Trailer', 'Death+House+Trailer', 'Big+Money+Hustlas+Trailer', 'On+the+Doll+Trailer', 'The+St+Louis+Bank+Robbery+Trailer', 'Stripped+to+Kill+Trailer', 'Sister+Street+Fighter+Trailer']
error_iframes = [9, 18, 64, 74, 100, 144, 146, 168, 284]
error_value = ["Meet+John+Doe+Trailer","Kenny+Trailer","M+Trailer","Elevator+to+the+Gallows+Trailer","Love+Songs+Trailer","Choke+Trailer","The+Wasp+Woman+Trailer","The+Lady+Vanishes+Trailer","Women+in+Cages+Trailer"]

valid_list = []

class TrailerURLS:
    def __init__(self):
        pass

    def Main(self):
        i = 0
        for query in list:
            try:
                if query not in valid_list:
                    valid_list.append(query)
                    url = "https://www.youtube.com/results?search_query="
                    driver = webdriver.Chrome()
                    time.sleep(4)
                    driver.get(url + query)
                    thumbnail = driver.find_elements(By.XPATH,
                                                     "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail")
                    if thumbnail is not None:
                        thumbnail[0].click()
                    else:
                        continue
                    time.sleep(2)
                    driver.implicitly_wait(10)
                    video_section = driver.find_element(By.XPATH,
                                                        "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video")

                    time.sleep(8)
                    try:
                        driver.find_element(By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']").click()
                    except NoSuchElementException:
                        pass

                    action = ActionChains(driver)
                    action.context_click(video_section).perform()
                    driver.implicitly_wait(10)
                    driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]").click()
                    win32clipboard.OpenClipboard()
                    data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()
                    self.write_Data(str(data).replace("></iframe>",
                                                      " id=\"Youtube_iframe\" style=\"visibility:hidden\"></iframe>"))  # id="Youtube_iframe" style="visibility:hidden"></iframe>
                    i += 1
                    print(f"{i} OUT OF {len(self.searchQuery())}")
                    driver.close()
            except Exception as e:
                self.write_Data("Error\n")
                continue


    def MovieNames(self):
        with open("saved_Data/Names.txt", "r") as file:
            return file.readlines()

    def searchQuery(self):
        names = self.MovieNames()
        searchQueries = []
        for name in names:
            str = ""
            for x in name.replace("\n", "").replace(".", "").split(" "):
                if str == "":
                    str += x
                else:
                    str += "+" + x
            searchQueries.append(str + "+Trailer")
        return searchQueries

    def write_Data(self, value):
        with open("saved_Data/MoviesTrailers_Iframe.txt", "a") as file:
            file.write(value + "\n")
            file.close()

    def updateSQL(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-T1QLR7U;'
                              'Database=MoviesSite;'
                              'Trusted_Connection=yes;')
        cursor = conn.cursor()
        iframes = []
        try:
            with open("saved_Data/MoviesTrailers_Iframe.txt", "r") as file:
                iframes = file.readlines()
                file.close()

            query = "UPDATE MOVIES SET TRAILER = '"
            #
            for i in range(0, 292): #
                try:
                    if i != 38:
                        data = iframes[i].replace("></iframe>", " runat=\"server\"></iframe>").replace("width=\"864\" height=\"648\"", "")
                        query = f"UPDATE MOVIES SET TRAILER = '{data}' WHERE MID = {i}"
                        print(query)
                        cursor.execute(query)
                        cursor.commit()

                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            print(e)
            pass












t1 = TrailerURLS()
t1.updateSQL()