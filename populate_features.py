import urllib.request
import json
import ssl
import time

API_URL = "https://aurora-grand-hotel-backend.onrender.com/api/room-features/"
ROOMS_URL = "https://aurora-grand-hotel-backend.onrender.com/api/rooms/"

features_data = [
    {
        "room_query": "Executive Room",
        "title": "Extra Cozy Bathroom",
        "image_url": "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=800",
        "description": "Relax in our premium spa-inspired bathroom with rainfall shower and soaking tub."
    },
    {
        "room_query": "Deluxe Room",
        "title": "Private Gym Access",
        "image_url": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=800",
        "description": "Exclusive access to our state-of-the-art fitness center."
    },
    {
        "room_query": "Standard Room",
        "title": "Dedicated Workspace",
        "image_url": "https://images.unsplash.com/photo-1516559828984-fb3b99548b21?w=800",
        "description": "Ergonomic desk and chair for your productivity needs."
    }
]

def get_room_id(name_query):
    ctx = ssl.create_default_context()
    try:
        req = urllib.request.Request(ROOMS_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx) as response:
            rooms = json.loads(response.read().decode('utf-8'))
            for room in rooms:
                if name_query.lower() in room['name'].lower():
                    return room['id']
    except Exception as e:
        print(f"Error fetching rooms: {e}")
    return None

def populate():
    ctx = ssl.create_default_context()
    
    print("Fetching room IDs...")
    
    for feature in features_data:
        room_id = get_room_id(feature['room_query'])
        if not room_id:
            print(f"Could not find room matching '{feature['room_query']}'")
            continue
            
        data = {
            "room": room_id,
            "title": feature['title'],
            "image_url": feature['image_url'],
            "description": feature['description']
        }
        
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(API_URL, data=json_data, headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        })
        
        try:
            with urllib.request.urlopen(req, context=ctx) as response:
                print(f"Successfully added feature '{feature['title']}' to Room {room_id}")
        except urllib.error.HTTPError as e:
            print(f"Failed to add feature: {e.code}")
            print(e.read().decode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(1) # Be nice to the API

if __name__ == "__main__":
    populate()
