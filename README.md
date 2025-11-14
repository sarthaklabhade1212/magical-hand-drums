# 🎵 MAGICAL HAND DRUMS
### *A Gesture-Controlled Virtual Drum System using MediaPipe, OpenCV & Pygame*

This project uses **hand tracking + finger gesture recognition** to control a **virtual drum kit** in real-time.  
Just move your hands in front of the webcam — and enjoy playing drums without any physical instrument! 🥁✨

---

## 🚀 Features
- 🖐️ Real-time **hand & finger detection** using MediaPipe  
- 🎼 Gesture → Drum mapping (Kick, Snare, HiHat, Tom, Crash)  
- 💥 **Particle explosion effects** on every hit  
- 🌌 Animated starry background  
- 🎥 Circular webcam view  
- ⚡ Smooth & low-latency performance  
- 🎛️ Fully synthesized drum sounds  

---

## 🧠 How It Works
1. Webcam captures real-time frames  
2. MediaPipe detects **21 hand landmarks**  
3. System counts fingers → identifies gesture  
4. Each gesture triggers a **specific drum sound**  
5. Pygame shows animations, particles, and UI elements  

---

## 🏗️ System Architecture
```
Webcam → MediaPipe Hand Tracking → Gesture Logic → Drum Engine → Particle Effects → Display
```

---

## 🛠️ Tech Stack
| Component | Technology |
|----------|------------|
| Hand Tracking | MediaPipe |
| Image Processing | OpenCV |
| Audio Engine | Pygame |
| Animations | Pygame + Custom Particles |
| Language | Python |

---

## 📂 Project Structure
```
magical-hand-drums/
│── src/
│   ├── main.py
│   ├── hand_tracking.py
│   ├── gestures.py
│   ├── drum_sounds.py
│   ├── particles.py
│   ├── ui_elements.py
│
│── assets/
│   ├── sounds/
│   │   ├── kick.wav
│   │   ├── snare.wav
│   │   ├── hihat.wav
│   │   ├── tom.wav
│   │   └── crash.wav
│   └── icons/
│
│── README.md
│── requirements.txt
│── LICENSE
│── .gitignore
```

---

## 📦 Installation

### 1️⃣ Clone the repository
```
git clone https://github.com/<your-username>/magical-hand-drums.git
cd magical-hand-drums
```

### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the application
```
python src/main.py
```

---

## 🎮 Gestures → Drum Sounds
| Gesture | Fingers | Output |
|---------|---------|---------|
| 1 finger | Index | Kick |
| 2 fingers | Index + Middle | Snare |
| 3 fingers | Index + Middle + Ring | HiHat |
| 4 fingers | Four fingers | Tom |
| 5 fingers | Open palm | Crash |

---

## 🏆 Outcome
✔ Fully functional gesture-controlled virtual drum kit  
✔ Real-time gesture accuracy  
✔ Smooth UI, starry background & circular webcam  
✔ Fun & interactive music experience  

---

## 👨‍💻 Team — VEXON
- Snehal Patange (Leader)  
- Sarthak Labhade  
- Mitali Gawali  
- Jayesh Borade  
- Krushna Thete  

Guided By: **Prof. Raj Sir**  
Sanjivani University, Kopargaon

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Support
If you like this project, consider giving it a **Star ⭐ on GitHub**!
