# start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q=hello  --profile-directory="Profile 1"

"""
    The function opens Microsoft Edge browser with different profiles and searches for a decreasing
    substring in Bing search engine.
"""
import subprocess
import time
# from jax import jit
import numba
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




def close_edge_browser():
    subprocess.run(["taskkill", "/im", "msedge.exe", "/f"])



# @jit(nopython=True)
def run_command(command):
    try:
        # Open command prompt and run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# @jit(nopython=True)
def main(profileNo):

    for i in range(0,profileNo):
        if i != 0 :
            profile = "Profile " + str(i)
        else : 
            profile = "Default "
        print(profile)

        searchText = randomword(32)

        for j in range(len(searchText)-1,-1,-1):
            query = searchText[0:j]
            print(j,"   ", query)

            command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q={query}  --profile-directory="{profile}"'  
            run_command(command)
            time.sleep(1.5)
            if (j % 7 == 0):
                close_edge_browser()
            time.sleep(2)


def clean_edge_cache():
    try:
        # Execute the command to clear Edge cache
        subprocess.run(['cmd', '/c', 'start', 'msedge', '--clear-achievements'], check=True)
        print("Edge cache cleaned successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while cleaning Edge cache:", e)


if __name__ == "__main__":
    profileNo = int(input("Number of profiles you have (include Default) : "))
    # skipProfile = input("If search is complete for any profile enter those profile no (coma separated or enter NA ) : ")
    main(profileNo)

    # Call the function to clean the Edge cache
    clean_edge_cache()