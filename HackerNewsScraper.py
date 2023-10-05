#HackerNews Scraper Part 2
import requests
import json
import datetime

#inits
newStories =[]
goodStories = []
## fetch IDs of new stories
fireBaseTop = requests.get("https://hacker-news.firebaseio.com/v0/newstories.json")
newList = fireBaseTop.json() #put them in a newList

#the datetime for today
today = datetime.date.today()

def fetchInfo(): #a function to convert the IDs into actual json vals
    for each in newList[0:int(input("Input maximum number of stories to fetch: "))]: #I've limited this to 51 stories for speeed
        tempVar = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{each}.json")
        newStories.append(tempVar.json()) #put it in the list
def purgeInfo(z): #how we purge the stories so it's only high-quality
    z = input("Welcome to Lux HackerNews Scraper. What is the score threshold you'd like to set for display? ")
    z = int(z) #so the function works, it doesn't work with z as a string
    newStories.sort(key =lambda y: y['score']) #sort by score, this suddenly broke but then unbroke ??
    newStories.reverse() #so it's descending
    for each in newStories:
        if each['score'] > z:
            goodStories.append(each) #I have no idea why it works now but it does
def beautifyInfo(): #make this actually readable in the CLI
    counter = 0
    for each in goodStories[counter]: #iterate through list
        print("\n")
        print(f"Title : {goodStories[counter]['title']}") #prints the info
        print(f"Score : {goodStories[counter]['score']}")
        timeOfPosting = goodStories[counter]['time'] #get time from each item
        timeOfPosting = datetime.date.fromtimestamp(timeOfPosting) #convert timestamp to date obj
        timeOfPosting = timeOfPosting.strftime("%a %b %d %Y at %H:%M") #using that we can string-ify the time
        print(f"Time of Posting : {timeOfPosting}")
        try:
            print(f"URL : {goodStories[counter]['url']}") #apparently this doesn't work if it doesn't have an url
        except: #so if any item has no link it doesn't break
            print("This one has no URL.") #I do not want to write the code to actually output a hyperlink; try using a different Terminal application if it doesn't work
        print("\n")
        counter += 1
        if counter == len(goodStories): #prevents an error where it tries to keep counting and then iterating
            break
    print("\n")
    print("\n")
    print("\n")
    print(f"Data fetched on {today}")

fetchInfo()
purgeInfo(2)
beautifyInfo()
