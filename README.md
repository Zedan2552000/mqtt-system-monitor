# 💻 MQTT System Monitor

A lightweight Python script that monitors your PC's real-time performance (CPU, RAM, and Disk usage) and publishes the data to an MQTT broker. 

Perfect for displaying your PC's health on a **Home Assistant** dashboard!

## ✨ Features
- **Cross-Platform:** Works on Windows, macOS, and Linux (powered by `psutil`).
- **Low Resource:** Runs silently in the background with minimal overhead.
- **JSON Payload:** Publishes data in a structured JSON format, making it extremely easy for Home Assistant to parse using MQTT Sensors.

## 🚀 Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Zedan2552000/mqtt-system-monitor.git
   cd mqtt-system-monitor
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Set your MQTT credentials as environment variables (or edit the script directly):
   - `MQTT_BROKER` (default: 192.168.1.100)
   - `MQTT_PORT` (default: 1883)
   - `MQTT_USER`
   - `MQTT_PASSWORD`
   - `MQTT_TOPIC` (default: homeassistant/sensor/pc_monitor/state)

4. Run the script:
   \`\`\`bash
   python monitor.py
   \`\`\`

## 🏠 Home Assistant Configuration
Add the following to your `configuration.yaml` in Home Assistant:

\`\`\`yaml
mqtt:
  sensor:
    - name: "PC CPU Usage"
      state_topic: "homeassistant/sensor/pc_monitor/state"
      value_template: "{{ value_json.cpu_usage }}"
      unit_of_measurement: "%"
    - name: "PC RAM Usage"
      state_topic: "homeassistant/sensor/pc_monitor/state"
      value_template: "{{ value_json.ram_usage }}"
      unit_of_measurement: "%"
\`\`\`

## 📄 License
MIT License
