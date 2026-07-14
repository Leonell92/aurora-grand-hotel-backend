import urllib.request
import json
import ssl

API_URL = "https://aurora-grand-hotel-backend.onrender.com/api/rooms/"

def delete_room(room_id):
    ctx = ssl.create_default_context()
    url = f"{API_URL}{room_id}/"
    req = urllib.request.Request(url, method='DELETE', headers={
        'User-Agent': 'Mozilla/5.0'
    })
    
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            print(f"Successfully deleted Room {room_id}")
    except Exception as e:
        print(f"Error deleting Room {room_id}: {e}")

def cleanup():
    # Delete the known duplicates
    for i in range(4, 7):
        delete_room(i)

if __name__ == "__main__":
    cleanup()
