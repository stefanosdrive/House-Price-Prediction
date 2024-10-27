from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_name')
def get_locations_name():
    response = jsonify({
        'locations': util.get_location_name()
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    total_rooms = int(request.form["total_rooms"])
    total_m2 = float(request.form["total_m2"])
    level = int(request.form["level"])
    total_baths = int(request.form["total_baths"])
    total_balconies = int(request.form["total_balconies"])
    location = request.form["location"]
    
    response = jsonify({
        'estimated_price': util.get_price(location, total_m2, total_rooms, total_baths, total_balconies, level)
        })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python FLask Server...")
    util.load_saved_artifacts()
    app.run()