import requests
import csv

# Import the necessary libraries
import requests
import csv

# Define the API endpoint and parameters
url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
querystring = {"lat": "35.5", "lon": "-78.5"}

headers = {
    "X-RapidAPI-Key": "07c652e4bcmsh79d638ce38187d6p1c70eajsnf74aebad9585",
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com",
}

# Send a GET request to the API
response = requests.get(url, headers=headers, params=querystring)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()

    # Extract the relevant data you want to save to the CSV file
    # For example, if you want to save the 'data' key from the JSON response:
    data_to_save = weather_data.get("data", [])

    # Define the CSV file name
    csv_file_name = "weather_data.csv"

    # Write the data to a CSV file
    with open(csv_file_name, mode="w", newline="") as csv_file:
        fieldnames = data_to_save[0].keys()  # Assuming all dictionaries in the list have the same keys
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data_to_save:
            writer.writerow(item)

    print(f"Data saved to {csv_file_name}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
