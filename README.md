
# 🌃 Smart Street Lighting System using Raspberry Pi Pico

This project is a part of a larger implementation titled **Smart Street Lighting with AI-based Accident Detection**. It uses a Raspberry Pi Pico to automatically control street light brightness based on **ambient light intensity** and **motion detection**, improving energy efficiency and automation.

## 🔧 Features

- 🔦 Adjusts street light brightness based on surroundings:
  - Automatically turns **OFF** during the day.
  - Lights up to **dim** brightness at night when no motion is detected.
  - Switches to **full brightness** when motion is detected.
- 🧠 Energy-efficient: Uses PWM to control brightness.
- 🧩 Easily extendable to add:
  - Fault detection
  - SOS/Accident alert system
  - GPS module for location tracking

## 🛠️ Components Used

- **Raspberry Pi Pico**
- **LDR (Light Dependent Resistor)**
- **PIR Motion Sensor**
- **6 LEDs**
- **Resistors** for LDR and LEDs
- **Breadboard & Jumper Wires**

## 🧪 Working Principle

| Condition              | LED Brightness  |
|------------------------|-----------------|
| Bright light (Daytime) | OFF             |
| Dark + No Motion       | Dim             |
| Dark + Motion Detected | Full Brightness |

## 🧾 Code Overview

- Reads **LDR sensor** using ADC to detect light levels.
- Reads **PIR sensor** to detect movement.
- Uses **PWM** to control brightness of 6 LEDs.
- Decision logic based on light and motion status.



