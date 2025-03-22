from flask import Flask, jsonify
import cloudscraper
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to ActiveSG Gym Capacity API"})

@app.route('/api/gym-capacity', methods=['GET'])
def get_gym_capacity():
    gym_capacity = {}
    scraper = cloudscraper.create_scraper()
    url = "https://activesg.gov.sg/api/trpc/pass.getFacilityCapacities?input=%7B%22json%22%3Anull%2C%22meta%22%3A%7B%22values%22%3A%5B%22undefined%22%5D%7D%7D"
    response = scraper.get(url)

    if response.status_code == 200:
        result = json.loads(response.text)
        gymFacilities = result["result"]["data"]["json"]["gymFacilities"]
        
        for gym in gymFacilities:
            gym_capacity[gym["name"]] = gym["capacityInfo"]
        return jsonify(gym_capacity)
    else:
        return jsonify({"error": f"Failed with status code {response.status_code}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)