import random
import time

def simulate_energy_data():
    while True:
        voltage = 220 + random.uniform(-5, 5)  # simulate 215V to 225V
        current = random.uniform(0.5, 5.0)     # simulate 0.5A to 5A
        power = voltage * current               # power in watts
        print(f"Voltage: {voltage:.1f} V, Current: {current:.2f} A, Power: {power:.1f} W")
        time.sleep(2)

if __name__ == "__main__":
    simulate_energy_data()