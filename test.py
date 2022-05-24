import requests

print("Kanye West appears and offers you some wisdom: \n") 
response = requests.get("https://api.kanye.rest")
wisdom = response.json()
print("Kanye says: " + wisdom["quote"])
print("\nWTH......okay?  Moving on...")
