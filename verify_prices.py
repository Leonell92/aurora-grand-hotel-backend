import urllib.request
import json
import ssl

API_URL = "https://aurora-grand-hotel-backend.onrender.com/api/rooms/"

def verify_prices():
    ctx = ssl.create_default_context()
    
    req = urllib.request.Request(API_URL, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            data = json.loads(response.read().decode('utf-8'))
            for room in data:
                print(f"Room {room['id']} ({room['name']}): {room['price_per_night']}")
    except Exception as e:
        print(f"Error fetching rooms: {str(e)}")

if __name__ == "__main__":
    verify_prices()
