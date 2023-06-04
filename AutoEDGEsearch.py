# start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q=hello  --profile-directory="Profile 1"

"""
    The function opens Microsoft Edge browser with different profiles and searches for a decreasing
    substring in Bing search engine.
"""
import subprocess
import time
# from jax import jit
# import numba
import psutil

import random, string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# testing variable 
''' 
RandomText30 = "abcdefghijklmnopqrstuvwxyz123456"
RandomText10 = "uhbueehjdeaw"
ProfileIDs = ["Default","1","2","3","4","5","7","8","9","10","11","12","13","14","15"]
'''


# search90 = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,19,22,23]


# @jit(nopython=True)
def run_command(command):
    try:
        # Open command prompt and run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# @jit(nopython=True)
def main(profileNo):
    # Bing daily reword system
    clean_edge_cache()

    for i in range(0,profileNo):
        # if i in search90:
        #     strlength = 35
        # else:
        #     strlength = 12
        if i != 0 :
            profile = "Profile " + str(i)
        else : 
            profile = "Default"
        print(profile)

        strlength = 35
        searchText = randomword(strlength)

        # command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/spotlight/imagepuzzle?OCID=ML2BF0&PUBL=RewardsDO&PROGRAMNAME=BingDailyOfferIN&CREA=ML2BF0&FORM=ANSRW1  --profile-directory="{profile}"'  
        # run_command(command)

        for j in range(len(searchText)-1,0,-1):
            query = searchText[0:j]
            print(j,"   ", query)

            command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q={query}  --profile-directory="{profile}"'  
            run_command(command)
            # time.sleep(1)
            if (j % 18 == 0):
                time.sleep(12)
                clean_edge_cache()
            elif(j==1):
                time.sleep(7)
                clean_edge_cache()
            time.sleep(0.5)

def clean_edge_cache():
    run_command("taskkill /f /im msedge.exe")

if __name__ == "__main__":
    profileNo = int(input("Number of profiles you have (include Default) : "))
    # skipProfile = input("If search is complete for any profile enter those profile no (coma separated or enter NA ) : ")
    main(profileNo)

    # Call the function to clean the Edge cache
    clean_edge_cache()