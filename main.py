import requests
from send_mail import send_mail


api_key = "9833cb1d8c24473a9679aa208c09dca2"
url = f"https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

email_body = []
# Access the article titles, description and URL
for article in content["articles"]:
    email_body.append(f"{article['title']}\n{article['description']}\n{article['url']}")

email_body = "\n\n".join(email_body)
send_mail(email_body)








