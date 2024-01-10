"""
Currency Converter
This script takes user input for base and target currencies along with an amount,
makes a request to a currency conversion API, and prints the converted amount.

Author: Mahmoud Khalil
Date: 08-12-2023
"""

import requests

# User input for base and target currencies
base = input("Enter a base currency: ")
target = input("Enter a target currency: ")

# Validate and get the amount to convert
while True:
    try:
        amount = float(input("Enter the amount you want to convert: "))
    except ValueError:
        print("Invalid input. The amount should be float")
        continue

    if amount <= 0:
        print("The amount should be a positive number.")
        continue
    else:
        break

# Construct the API URL for currency conversion
url = f"https://api.apilayer.com/fixer/convert?to={target}&from={base}&amount={amount}"

with open('OpenWeather_API_Key.txt', 'r') as file:
    api_key = file.read()

# Headers for the API request, including the API key
headers = {
    "apikey": api_key
}

try:
    # Make the API request
    response = requests.request("GET", url, headers=headers)

    # Get the HTTP status code from the response
    status_code = response.status_code

    # Check if the request was successful (status code 200)
    if status_code == 200:
        # Parse the JSON response to extract the conversion result
        result = response.json()['result']
        print(f"{amount} {base} = {result} {target}")
    else:
        # Handle errors for non-successful HTTP status codes
        print(f"Error: {status_code}. Unable to fetch conversion rates.")

except requests.exceptions.RequestException as e:
    # Handle exceptions related to the API request (e.g., network issues)
    print(f"Error: {e}. Unable to make the API request.")
