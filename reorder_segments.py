import requests
import json
from pprint import pprint

FLAGR_API_URL = "https://flagr.allen-stage.in/api/v1"
FLAG_ID = 16

def getAllSegments():
    url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/segments"
    
    response = requests.get(url)
    segments = response.json()
    # pprint(res)
    with open("all_segments.json", 'w') as json_file:
        json.dump(segments, json_file, indent=4)
    return segments


def reorderSegments(order):
    url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/segments/reorder"

    body = {
        "segmentIDs": order
    }

    response = requests.put(url=url,json=body)
    print(f"reorderSegments: ", response.status_code, response.text)


if __name__ == "__main__":
    segments_new_order = [30,34,29,33,31,32]
    reorderSegments(segments_new_order)
