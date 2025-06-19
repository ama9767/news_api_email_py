import requests


api_key = "9833cb1d8c24473a9679aa208c09dca2"
url = f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])






