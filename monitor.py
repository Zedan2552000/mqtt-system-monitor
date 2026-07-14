import psutil
import paho.mqtt.client as mqtt
import time
import json
import os

# MQTT Configuration (can be overridden by environment variables)
BROKER = os.getenv("MQTT_BROKER", "192.168.1.100")
PORT = int(os.getenv("MQTT_PORT", 1883))
USER = os.getenv("MQTT_USER", "")
PASSWORD = os.getenv("MQTT_PASSWORD", "")
TOPIC = os.getenv("MQTT_TOPIC", "homeassistant/sensor/pc_monitor/state")
INTERVAL = int(os.getenv("UPDATE_INTERVAL", 5))

def get_system_stats():
    """Gather CPU, RAM, and Disk statistics."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    return {
        "cpu_usage": cpu_usage,
        "ram_usage": ram.percent,
        "ram_free_gb": round(ram.available / (1024 ** 3), 2),
        "disk_usage": disk.percent,
        "disk_free_gb": round(disk.free / (1024 ** 3), 2)
    }

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

def main():
    print("Starting MQTT System Monitor...")
    
    client = mqtt.Client(client_id="pc_system_monitor")
    if USER and PASSWORD:
        client.username_pw_set(USER, PASSWORD)
        
    client.on_connect = on_connect
    
    try:
        client.connect(BROKER, PORT, 60)
        client.loop_start()
    except Exception as e:
        print(f"Connection failed: {e}")
        return

    try:
        while True:
            stats = get_system_stats()
            payload = json.dumps(stats)
            client.publish(TOPIC, payload, retain=False)
            print(f"Published: {payload}")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Stopping Monitor...")
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
