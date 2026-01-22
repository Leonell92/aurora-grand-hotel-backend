import urllib.request
import json
import ssl

API_URL = "https://aurora-grand-hotel-backend.onrender.com/api/rooms/"

updates = [
    {"id": 1, "price_per_night": "400000.00"}, # Deluxe
    {"id": 2, "price_per_night": "250000.00"}, # Executive
    {"id": 3, "price_per_night": "100000.00"}  # Standard
]

def update_prices():
    ctx = ssl.create_default_context()
    
    for item in updates:
        url = f"{API_URL}{item['id']}/"
        data = json.dumps({"price_per_night": item["price_per_night"]}).encode('utf-8')
        
        # Using PATCH for partial update
        req = urllib.request.Request(url, data=data, method='PATCH', headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                print(f"Successfully updated Room {item['id']} to {item['price_per_night']}")
        except urllib.error.HTTPError as e:
            print(f"Failed to update Room {item['id']}: {e.code}")
            print(e.read().decode('utf-8'))
        except Exception as e:
            print(f"Error updating Room {item['id']}: {str(e)}")

if __name__ == "__main__":
    update_prices()
