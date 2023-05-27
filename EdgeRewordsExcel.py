import subprocess
import csv
import time
import psutil
import random
import string
from msedge.selenium_tools import Edge, EdgeOptions

from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.webdriver import WebDriver

def close_edge_browser():
    subprocess.run(["taskkill", "/im", "msedge.exe", "/f"])

def run_command(command):
    try:
        # Open command prompt and run the command
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def get_rewards_from_profile(profile_id):
    options = Options()
    options.add_argument(f"--profile-directory={profile_id}")  # Use the specified profile ID
    driver = WebDriver(service=Service("C:\edgedriver_win64\msedgedriver.exe"), options=options)
    # Replace <path_to_edge_driver> with the path to the downloaded Edge WebDriver executable

    driver.get("https://rewards.bing.com/?signin=1&FORM=ANSRW1")

    # Extract the rewards points element
    rewards_element = driver.find_element("xpath", "//div[@class='moe-taskcard-piecontent']/h2")

    rewards_points = rewards_element.text
    driver.quit()

    return rewards_points

def main(profileNo):
    # Bing daily reward system
    profile_ids = [f"Profile {i}" if i != 0 else "Default" for i in range(profileNo)]
    csv_file = r'C:\Users\shova\OneDrive\Desktop\AutoEDGE\AutoEDGESearch\Edge_Rewords.csv'

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Profile Number", "Rewards Points"])

        for i, profile_id in enumerate(profile_ids):
            command = f'start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" https://rewards.bing.com/?signin=1&FORM=ANSRW1  --profile-directory="{profile_id}"'
            run_command(command)

            rewards_points = get_rewards_from_profile(profile_id)
            profile_number = i + 1

            writer.writerow([profile_number, rewards_points])

            close_edge_browser()

    print("Rewards data saved to CSV successfully!")

def clean_edge_cache():
    try:
        # Execute the command to clear Edge cache
        subprocess.run(['cmd', '/c', 'start', 'msedge', '--clear-achievements'], check=True)
        print("Edge cache cleaned successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred while cleaning Edge cache:", e)

if __name__ == "__main__":
    profileNo = int(input("Number of profiles you have (including Default): "))
    main(profileNo)
    # Call the function to clean the Edge cache
    clean_edge_cache()
