#Shovan$Omail8085
#Shovan$Gmail8085
#shovanpaul48edge1@outlook.com


import webbrowser
import random, string
import time
import subprocess

def clear_browser_cache():
    # Clear the cache of the Bing browser using adb command
    subprocess.run(['adb', 'shell', 'pm', 'clear', 'com.microsoft.bing'])

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))



def search_in_bing():
    searchText = randomword(27)

    for j in range(len(searchText)-1,0,-1):
        query = searchText[0:j]
        print(j,"   ", query)   
        # Format the search text for the URL
        formatted_search_text = query.replace(' ', '+')
        # Open the Bing browser and search for the given text
        webbrowser.open('https://www.bing.com/search?q=' + formatted_search_text)
        #time.sleep()
        #clear_browser_cache()


print("Auto Bing search mobile started ")
search_in_bing()