import tweepy
import random
import requests

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET_KEY"
bearer_token = "YOUR_BEARER_TOKEN"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

filename = "image.jpeg" # Filename where image will be saved locally

response = requests.get('https://zenquotes.io/api/random')
data = response.json()[0]
quote = data['q'] + ' - ' + data['a'] # Random quote from ZenQuotes api

access_key = "UNSPLASH_API_KEY"
base_url = 'https://api.unsplash.com/'

# Set the endpoint and parameters
endpoint = 'search/photos'
query = quote  # Your search query
order_by="relevant"
orientation="landscape"
per_page=2
# Construct the request URL
url = f'{base_url}{endpoint}?query={query}&client_id={access_key}&order_by={order_by}&orientation={orientation}&per_page={per_page}'

image_url_first = "" # This will store the url of image
#print(quote)
response = requests.get(url)
#print("Response status code:", response.status_code)
#print("Response content:", response.content)
#If eveerything is working fine, then get fetch the url of the required image
if response.status_code == 200:
    data = response.json()
    photos = data["results"]
    for photo in photos:
        image_url_first = photo["urls"]["regular"]
        #print("image_url_first",image_url_first)
else:
    print("Request failed with status code:", response.status_code)


image_url = image_url_first
save_path = "C:/Users/Swapnil/Desktop/Twitter Bot/image.jpeg"
response = requests.get(image_url)
#print("image_url:",image_url)
# Download image and save it locally
if response.status_code == 200:
    with open(save_path, "wb") as f:
        f.write(response.content)
    #print("Image downloaded successfully.")
else:
    print("Failed to download the image.")
                     # Playing with the twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)
media = api.media_upload(filename)
 # creating final tweet and posting
tweet = client.create_tweet(text = quote,media_ids= [media.media_id_string])




