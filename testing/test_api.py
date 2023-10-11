import requests

url = "https://pythonfootball.azurewebsites.net/"  # Replace with your actual URL

response = requests.get(url)

if response.status_code == 200:
    print("GET request was successful")
    print("Response content:", response.text)
else:
    print("GET request failed with status code:", response.status_code)