from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/energy', methods=['POST'])
def receive_energy_data():
    data = request.json

    voltage = data.get("voltage")
    current = data.get("current")
    power = data.get("power")

    print(f"Received Energy Data -> Voltage: {voltage}V, Current: {current}A, Power: {power}W")

    return jsonify({"status": "success", "message": "Energy data received"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)