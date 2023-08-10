import urllib.request
import json

def convert(amount,start,end):
  #    # Construct the URL to fetch the currency conversion rates for the source currency
    url= f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/2022-11-24/currencies/{start.lower()}.json"
    #    # Send a request to the URL and retrieve the response
    request = urllib.request.urlopen(url)
  #    # Read the response and parse the JSON data
    data = json.loads(request.read())
  #    # Perform the currency conversion using the retrieved rates
    result = amount * data[start][end.lower()]
      # Return the converted amount
    return result
