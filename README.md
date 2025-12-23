# Smart Grid Energy Meter & Theft Detector 

A real-time monitoring system designed to track household energy consumption and detect "Non-Technical Losses" (NTL) such as meter bypassing or illegal tapping using anomaly detection algorithms.

## Key Features
* **Real-Time Load Tracking:** Monitors power (W) and current (A) at a 5Hz sampling rate.
* **Automated Anomaly Detection:** Implements edge-based thresholding to identify sudden, non-linear load spikes.
* **Visual Alert System:** Dynamic Python dashboard that triggers a "CRITICAL" state (red-alert) upon detecting potential theft.

---

## Technical Stack
* **Hardware:** Arduino Uno, 10kΩ Potentiometer (Simulating Load Transducer).
* **Firmware:** C++ (Edge-based thresholding logic).
* **Software:** Python 3.13.
* **Libraries:** `Matplotlib` (Animation), `PySerial`.

---

## How It Works
1. **Edge Processing:** The Arduino calculates real-time power metrics and compares current draw against a safety threshold (12A simulation).
2. **Data Streaming:** Status flags and power data are streamed via Serial at 115,200 baud.
3. **Detection Dashboard:** A Python-based GUI monitors the stream. If the 'Theft Flag' is triggered, the UI performs a state-change (color shift and header alert) to notify the utility operator.

---

## Demonstration

![smart_energy_meter](https://github.com/user-attachments/assets/31f6f5ba-18b7-45a7-a9a2-e98beb4df2ac)


* **Green State:** Normal household consumption.
* **Red State:** Anomalous spike detected (Theft/Bypass simulation).
