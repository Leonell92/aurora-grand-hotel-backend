import urllib.request
import time
import sys

URL = "https://aurora-grand-hotel-backend.onrender.com/api/room-features/"

print("Monitoring deployment...")
while True:
    try:
        req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                print("\nDeployment complete! Endpoint is up.")
                break
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            print(f"\nUnexpected error: {e.code}")
    except Exception as e:
        print(f"\nConnection error: {e}")
    
    time.sleep(10)
