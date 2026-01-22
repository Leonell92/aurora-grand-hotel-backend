import urllib.request
import json
import ssl

API_URL = "https://aurora-grand-hotel-backend.onrender.com/api/rooms/"

rooms = [
    {
        "name": "Executive Room",
        "room_type": "double",
        "description": "Modern room with premium amenities and city view",
        "price_per_night": "199.99",
        "max_guests": 2,
        "image_url": "https://images.unsplash.com/photo-1590490360182-c33d57733427?w=800",
        "amenities": ["WiFi", "TV", "Work Desk", "City View"],
        "available": True
    },
    {
        "name": "Standard Room",
        "room_type": "single",
        "description": "Cozy room perfect for solo travelers",
        "price_per_night": "129.99",
        "max_guests": 2,
        "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=800",
        "amenities": ["WiFi", "TV"],
        "available": True
    }
]

def add_rooms():
    # Create a context that doesn't verify certificates if needed, though Render has valid SSL
    ctx = ssl.create_default_context()
    
    for room in rooms:
        data = json.dumps(room).encode('utf-8')
        req = urllib.request.Request(API_URL, data=data, headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                print(f"Successfully added: {room['name']} - Status: {response.getcode()}")
                print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Failed to add {room['name']}: {e.code}")
            print(e.read().decode('utf-8'))
        except Exception as e:
            print(f"Error adding {room['name']}: {str(e)}")

if __name__ == "__main__":
    add_rooms()
