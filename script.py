import requests

# virtualenv.step4
print(requests.__version__)

# curl.step5
response = requests.get("http://www.google.com")
print("google home page response: ", response.content)
