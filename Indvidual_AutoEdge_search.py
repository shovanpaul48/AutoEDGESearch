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




# @jit(nopython=True)
def run_command(command):
    try:
        # Open command prompt and run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# @jit(nopython=True)
def main(profileNo):
    clean_edge_cache()
    searchText = randomword(33)
    profile ="Profile " + str(profileNo)
    for j in range(len(searchText)-1,0,-1):
        query = searchText[0:j]
        print(j,"   ", query)

        command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://www.bing.com/search?q={query}  --profile-directory="{profile}"'  
        run_command(command)
            # time.sleep(1)
        if (j % 20== 0):
            time.sleep(5)
            clean_edge_cache()
        time.sleep(1.5)

def clean_edge_cache():
    run_command("taskkill /f /im msedge.exe")
    
if __name__ == "__main__":
    profileNo = int(input("Profile No to search with : "))
    # skipProfile = input("If search is complete for any profile enter those profile no (coma separated or enter NA ) : ")
    main(profileNo)

    # Call the function to clean the Edge cache
    clean_edge_cache()