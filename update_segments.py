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


def filterSegmentsById(segments, segment_ids):
    res = []
    
    for segment in segments:
        if segment["id"] in segment_ids:
            res.append(segment)
    
    return res


def createFreemiumCopyOfSegment(segment):
    new_description = f"{segment['description']}_freemium"
    rolloutPercent = 100

    url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/segments"

   
    body = {
        "description": new_description,
        "rolloutPercent": rolloutPercent
    }
    response = requests.post(url, json=body)
    print(f"createFreemiumCopyOfsegment: description: {segment['description']} =>", response.status_code, response.text)

    if response.status_code != 200:
        print("failed in creating segment")
        return
    
    created_segment = response.json()

    new_seg_id = created_segment["id"]

    constraints_url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/segments/{new_seg_id}/constraints"

    body = {
        "description": new_description,
        "rolloutPercent": rolloutPercent
    }
    
    for constraint in segment["constraints"]:
        body = {
            "operator": constraint["operator"],
            "property": constraint["property"],
            "value": constraint["value"]
        }
        response = requests.post(constraints_url, json=body)
        print(f"postConstraint: description: {constraint} =>", response.status_code, response.text)

    

if __name__ == "__main__":
    segments = getAllSegments()
    
    segment_ids_to_filter = [30,32]

    filtered_segments = filterSegmentsById(segments = segments, segment_ids = segment_ids_to_filter)

    for seg in filtered_segments:
        createFreemiumCopyOfSegment(seg)
   