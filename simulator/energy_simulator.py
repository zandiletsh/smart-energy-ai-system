import random
import time
import requests

API_URL = "http://127.0.0.1:5000/energy"

while True:

    voltage = round(random.uniform(210, 230), 2)
    current = round(random.uniform(1.5, 5.0), 2)
    power = round(voltage * current, 2)

    energy_data = {
        "voltage": voltage,
        "current": current,
        "power": power
    }

    print(f"Sending -> Voltage: {voltage}V, Current: {current}A, Power: {power}W")

    try:
        response = requests.post(API_URL, json=energy_data)
        print("API Response:", response.json())
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(5)