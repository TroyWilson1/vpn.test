#!/usr/bin/python3
import requests

def get_ip_and_geo_location():
    try:
        # URL for the IP info API
        url = "https://ipinfo.io/json"

        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract IP address and geo-location info
        ip_address = data.get("ip")
        hostname = data.get("hostname")
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        location = data.get("loc")  # Latitude and longitude in "lat,lon" format

        # Print the results
        print(f"IP Address: {ip_address}")
        print(f"Hostname: {hostname}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Location: {location}")

    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_ip_and_geo_location()

