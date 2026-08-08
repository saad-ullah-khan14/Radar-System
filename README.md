# Wireless Local Radar System (ESP32 + Python Flask)

A real-time wireless radar system built using an **ESP32** microcontroller, an **Ultrasonic Sensor**, and a **Python Flask** backend. The system measures object distance and transmits the telemetry data over Wi-Fi to a local server, which renders a live radar sweep animation on a web-based dashboard.

---

## 🛠️ Tech Stack & Components

* **Microcontroller:** ESP32 NodeMCU
* **Sensor:** HC-SR04 Ultrasonic Sensor
* **Backend:** Python (Flask Framework)
* **Frontend:** HTML5 Canvas, JavaScript, CSS

---

## 🚀 Project Structure

```text
RadarProject/
│
├── app.py                  # Python Flask Server
├── templates/
│   └── index.html          # Web Dashboard (Radar UI)
└── radar.ino               # ESP32 Arduino Code
⚙️ Setup & Installation Instructions
1. Hardware Connections
Connect the Ultrasonic Sensor to the ESP32 as follows:

Trig Pin ──> GPIO 5

Echo Pin ──> GPIO 18

VCC ──> 3.3V / 5V

GND ──> GND

2. Run the Flask Server
Clone the repository and navigate to the project folder.

Install Flask:

Bash
pip install flask
Run the application:

Bash
python app.py
3. Upload ESP32 Code
Open radar.ino in Arduino IDE.

Update your Wi-Fi credentials (ssid and password) and your PC's local IP address (serverName).

Upload the code to your ESP32.

4. View Dashboard
Open your web browser and go to:

Plaintext
http://localhost:5000
