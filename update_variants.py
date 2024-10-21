import requests
import json
from pprint import pprint

FLAGR_API_URL = "https://flagr.allen-stage.in/api/v1"
FLAG_ID = 16

JEE_AND_NEET_STREAMS = [
    "STREAM_JEE_MAIN_ADVANCED",
    "STREAM_PRE_MEDICAL", 
    "STREAM_JEE_MAINS",
]

def getAllVariants():
    url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/variants"
   
    response = requests.get(url)
    variants = response.json()
    # pprint(res)
    with open("all_variants.json", 'w') as json_file:
        json.dump(variants, json_file, indent=4)
    return variants

def createFreemiumCopyOfVariant(variant):
    new_key = f"{variant['key']}_freemium"
    attachment = variant["attachment"]

    url = f"{FLAGR_API_URL}/flags/{FLAG_ID}/variants"

    body = {
        "key": new_key,
        "attachment": attachment
    }
    response = requests.post(url, json=body)
    print(f"createFreemiumCopyOfVariant: key: {variant['key']} =>", response.status_code, response.text)



def filterVariantsById(variants, variant_ids):
    res = []
    
    for variant in variants:
        if variant["id"] in variant_ids:
            res.append(variant)
    
    return res


    
if __name__ == "__main__":
    variants = getAllVariants()
    
    variant_ids_to_filter = [33,34]

    filtered_variants = filterVariantsById(variants = variants, variant_ids = variant_ids_to_filter)

    for variant in filtered_variants:
        createFreemiumCopyOfVariant(variant=variant)
