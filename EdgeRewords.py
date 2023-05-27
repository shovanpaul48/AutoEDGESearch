import requests
import pandas as pd

# Get the list of profile names
profile_names = ["Profile1", "Profile2", "Profile3"]

# Get the rewards points for each profile
rewards_points = []
for profile_name in profile_names:
    # Get the URL for the rewards page for the given profile
    url = "https://rewards.microsoft.com/en-us/bing/profiles/" + profile_name

    # Make a request to the URL
    response = requests.get(url)

    # Parse the response and get the rewards points
    rewards_points.append(response.json()["rewardsPoints"])

# Create an Excel sheet with the profile number and rewards points
df = pd.DataFrame({"Profile Number": profile_names, "Rewards Points": rewards_points})
df.to_excel("rewards_points.xlsx")
