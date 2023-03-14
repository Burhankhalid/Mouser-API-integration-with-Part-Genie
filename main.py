import requests

url = "https://api.mouser.com/api/v1/search/partnumber?apiKey=a09513df-da5e-47f7-b0f8-d8444d1850da"
  
headers = {
    "Authorization": "a09513df-da5e-47f7-b0f8-d8444d1850da",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# data to be sent to api
data = {
  "SearchByPartRequest": {
    "mouserPartNumber": ""
  }
}

data["SearchByPartRequest"]["mouserPartNumber"] = input("Enter Part Number: ")

  
# sending post request and saving response as response object
response = requests.post(url, headers = headers, json = data)

#print("Status Code: ", response.status_code)  


avail = response.json()['SearchResults']['Parts'][0]['Availability']
desc = response.json()['SearchResults']['Parts'][0]['Description']
man = response.json()['SearchResults']['Parts'][0]['Manufacturer']


print("Availability: ", avail)
print("Description: ", desc)
print("Manufacturer: ", man)

for i in range(len(response.json()['SearchResults']['Parts'][0]['PriceBreaks'])):
    prc = response.json()['SearchResults']['Parts'][0]['PriceBreaks'][i]['Price']
    quan = response.json()['SearchResults']['Parts'][0]['PriceBreaks'][i]['Quantity']
    print("Price of " + str(quan) + " will be " + str(prc) + " per part")
