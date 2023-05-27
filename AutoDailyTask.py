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
    # Bing daily reword system


    for i in range(0,profileNo):
        if i != 0 :
            profile = "Profile " + str(i)
        else : 
            profile = "Default"
        print(profile)

        task = "https://www.bing.com/search?q=Quote+of+the+day&OCID=ML2BFU&PUBL=RewardsDO&PROGRAMNAME=QuoteOfTheDay&CREA=ML2BFU&FORM=ANNRW1"
        command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" {task}  --profile-directory="{profile}"'  
        run_command(command)

        time.sleep(5)
        close_edge_browser()


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