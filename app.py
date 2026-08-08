from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ESP32 se aane wala latest data store karne ke liye variable
latest_data = {"angle": 0, "distance": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global latest_data
    data = request.get_json()
    if data:
        latest_data['angle'] = data.get('angle', 0)
        latest_data['distance'] = data.get('distance', 0)
    return jsonify({"status": "success"}), 200

@app.route('/data')
def get_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    