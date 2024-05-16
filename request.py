import requests

# Replace 'YOUR_API_TOKEN' with your actual Scraper API token
api_token = 'sk-proj-8kc88RmgC2Q7efjXXW4yT3BlbkFJKRYu6MqAv6d0iYwwTMDz'

# Replace 'YOUR_TARGET_URL' with the URL of the webpage you want to scrape
target_url = 'https://www.bigo.tv/fr/petitlion18'

# Construct the API endpoint URL
api_endpoint = f'https://api.crawlbase.com/scraper?token={api_token}&url={target_url}'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON response
    json_response = response.json()
    print(json_response)
else:
    print(f'Request failed with status code {response.status_code}')
