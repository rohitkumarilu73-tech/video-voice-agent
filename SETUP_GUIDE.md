# 🚀 Setup Guide - Video Voice Agent

## आपका Agent तैयार है! अब शुरुआत करें 🎬

### Step 1: Repository Clone करें
```bash
git clone https://github.com/rohitkumarilu73-tech/video-voice-agent.git
cd video-voice-agent
```

### Step 2: Python Virtual Environment बनाएं
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Dependencies Install करें
```bash
pip install -r requirements.txt
```

### Step 4: पहला Video Generate करें
```bash
python main.py
```

✅ आपका video `videos/` folder में save होगा!

---

## 📝 अपना खुद का Script कैसे बनाएं?

### Method 1: Python में Direct
```python
from agent import VideoVoiceAgent

agent = VideoVoiceAgent()

script = {
    "title": "मेरा वीडियो",
    "scenes": [
        {
            "text": "नमस्ते दुनिया!",
            "duration": 3,
            "background_color": (255, 0, 0)  # Red
        },
        {
            "text": "यह एक AI video है।",
            "duration": 3,
            "background_color": (0, 255, 0)  # Green
        }
    ]
}

agent.create_video_from_script(script)
```

### Method 2: JSON File से
```bash
python -c "from agent import VideoVoiceAgent; VideoVoiceAgent().create_video_from_json('sample_script.json')"
```

---

## 🎨 Background Colors (RGB Format)

```python
(255, 0, 0)      # Red
(0, 255, 0)      # Green
(0, 0, 255)      # Blue
(255, 255, 0)    # Yellow
(255, 0, 255)    # Magenta
(0, 255, 255)    # Cyan
(255, 165, 0)    # Orange
(128, 0, 128)    # Purple
```

---

## 🔧 Advanced Examples

### Hindi Video बनाएं
```bash
python advanced_example.py
# और फिर create_hindi_video() को uncomment करें
```

### Multiple Languages
```python
script = {
    "title": "Multilingual",
    "scenes": [
        {
            "text": "Hello हैलो مرحبا",
            "duration": 4,
            "background_color": (100, 100, 255)
        }
    ]
}
```

---

## 📊 Output Files कहां मिलेंगी?

- **Videos**: `videos/` folder में
- **Voice Files**: `voices/` folder में
- **Format**: MP4 video with MP3 audio

---

## ⚙️ Configuration Customize करें

### agent.py में changes करें:

```python
# 1. Speed बदलें (50-200)
agent.tts_engine.setProperty('rate', 100)  # Slower

# 2. Quality बदलें
agent = VideoVoiceAgent(fps=30)  # Higher FPS = Better quality

# 3. Resolution बदलें (agent.py में)
video_clip = ColorClip(size=(1280, 720), ...)  # 720p
```

---

## 🐛 Common Issues

### Issue: "moviepy not found"
```bash
pip install moviepy --upgrade
```

### Issue: "pyttsx3 voice नहीं सुनाई देता"
- **Windows**: SAPI5 है confirm करें
- **Mac**: `say` command install करें
- **Linux**: `sudo apt-get install espeak`

### Issue: Video quality bad है
FPS बढ़ाएं:
```python
agent = VideoVoiceAgent(fps=30)
```

---

## 🚀 अगला Step?

- [ ] अपना custom script बनाएं
- [ ] Multiple videos generate करें
- [ ] Background music add करें
- [ ] Subtitles add करें

---

**Happy Creating!** 🎬✨
