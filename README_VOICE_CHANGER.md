````markdown name=README_VOICE_CHANGER.md
# 🎙️ Video Voice Agent - Voice Changer Guide

## नई Features! 🆕

अब आप **अलग-अलग voice styles** में videos बना सकते हो!

### 🎬 Available Voice Styles

#### 1️⃣ **Modi Ji Style** 🇮🇳
- गहरी, सिरीयस आवाज़
- Slower speech (authority)
- Perfect for speeches & announcements
```python
voice_changer.generate_modi_voice("नमस्ते देशवासियों!", "output.mp3")
```

#### 2️⃣ **Trump Style** 🗽
- तेज़, energetic आवाज़
- Fast speech
- Powerful delivery
```python
voice_changer.generate_trump_voice("This is tremendous!", "output.mp3")
```

#### 3️⃣ **Kid Style** 👶
- High pitch
- Playful tone
- Fast & fun
```python
voice_changer.generate_kid_voice("हाय दोस्तों!", "output.mp3")
```

#### 4️⃣ **Robot Style** 🤖
- Mechanical effect
- Robotic pitch modulation
- Futuristic sound
```python
voice_changer.generate_robot_voice("Beep boop!", "output.mp3")
```

#### 5️⃣ **Custom Style** ⚙️
- अपने parameters से control करो
- Pitch, Speed, Voice type
```python
voice_changer.generate_custom_voice(
    text="नमस्ते!",
    output_file="output.mp3",
    pitch=1.2,        # 0.5-2.0 (1.0 = normal)
    speed=150,        # 50-200 (150 = normal)
    voice_type='male' # 'male' या 'female'
)
```

---

## 🚀 Quick Start

### Step 1: Install scipy (for audio processing)
```bash
pip install scipy
```

### Step 2: Run Demo
```bash
python voice_changer_demo.py
```

यह सभी 5 voice styles के साथ videos बनाएगा! 🎥

### Step 3: Check Output
```
videos/
  ├── Modi_Ji_Speech_*.mp4
  ├── Trump_Speech_*.mp4
  ├── Kid_Story_*.mp4
  ├── Robot_Message_*.mp4
  └── Custom_Voice_Demo_*.mp4

voices/
  ├── modi_voice_*.mp3
  ├── trump_voice_*.mp3
  ├── kid_voice_*.mp3
  ├── robot_voice_*.mp3
  └── custom_voice_*.mp3
```

---

## 💻 Code Examples

### Example 1: Modi Video बनाएं
```python
from voice_changer import VoiceChanger
from agent import VideoVoiceAgent

voice_changer = VoiceChanger()
agent = VideoVoiceAgent()

script = {
    "title": "My_Modi_Video",
    "scenes": [
        {
            "text": "नमस्ते! आज मैं एक महत्वपूर्ण संदेश देना चाहता हूँ।",
            "duration": 4,
            "background_color": (255, 140, 0)  # Saffron
        },
        {
            "text": "हमारा भारत प्रगति के पथ पर है।",
            "duration": 3,
            "background_color": (255, 165, 0)
        }
    ]
}

# Generate Modi voice for each scene
for idx, scene in enumerate(script['scenes']):
    voice_file = f"voices/modi_{idx}.mp3"
    voice_changer.generate_modi_voice(scene['text'], voice_file)

# Create video
agent.create_video_from_script(script)
```

### Example 2: Trump & Modi Mix
```python
script = {
    "title": "Funny_Mix",
    "scenes": [
        {
            "text": "Hello! This is tremendous!",
            "duration": 3,
            "background_color": (200, 0, 0)
        },
        {
            "text": "जय हिंद!",
            "duration": 2,
            "background_color": (255, 140, 0)
        }
    ]
}

# Mixed voices
voice_changer.generate_trump_voice(script['scenes'][0]['text'], "voices/scene1.mp3")
voice_changer.generate_modi_voice(script['scenes'][1]['text'], "voices/scene2.mp3")

agent.create_video_from_script(script)
```

### Example 3: Custom Parameters
```python
# High pitch, fast speed (energetic)
voice_changer.generate_custom_voice(
    "वाह! बहुत अच्छा है!",
    "voices/excited.mp3",
    pitch=1.3,
    speed=180,
    voice_type='female'
)

# Deep voice, slow speed (serious)
voice_changer.generate_custom_voice(
    "यह गंभीर विषय है।",
    "voices/serious.mp3",
    pitch=0.7,
    speed=100,
    voice_type='male'
)
```

---

## 🎨 Voice Parameters

### Pitch
- **0.5-0.8** → Deeper voice (like Modi)
- **1.0** → Normal voice
- **1.2-1.5** → Higher voice (like Kid/Trump)

### Speed
- **50-100** → Very Slow (like documentary)
- **120-150** → Normal (like regular speech)
- **160-200** → Fast (like Trump/excited)

### Voice Type
- **'male'** → Male voice
- **'female'** → Female voice

---

## 📊 VoiceChanger Class Methods

```python
from voice_changer import VoiceChanger

vc = VoiceChanger(voice_dir="voices")

# Generate different voices
vc.generate_modi_voice(text, output_file)
vc.generate_trump_voice(text, output_file)
vc.generate_kid_voice(text, output_file)
vc.generate_robot_voice(text, output_file)
vc.generate_custom_voice(text, output_file, pitch=1.0, speed=150, voice_type='male')

# List available system voices
vc.list_available_voices()
```

---

## 🔧 Troubleshooting

### Issue: "scipy not found"
```bash
pip install scipy
```

### Issue: Voice quality is bad
- Try different pitch values
- Adjust speed parameter
- Test with `list_available_voices()`

### Issue: Audio processing fails
- Make sure output directory exists
- Check disk space
- Try with shorter text first

---

## 🚀 Advanced Usage

### Batch Create Multiple Voices
```python
texts = [
    "नमस्ते!",
    "Hello!",
    "Beep boop!"
]

voice_changer = VoiceChanger()

for i, text in enumerate(texts):
    voice_changer.generate_modi_voice(text, f"voices/batch_{i}_modi.mp3")
    voice_changer.generate_trump_voice(text, f"voices/batch_{i}_trump.mp3")
    voice_changer.generate_kid_voice(text, f"voices/batch_{i}_kid.mp3")
```

### Create Multilingual Video
```python
script = {
    "title": "Multi_Language",
    "scenes": [
        {
            "text": "Hello world!",  # English
            "duration": 3,
            "background_color": (100, 100, 255)
        },
        {
            "text": "नमस्ते दुनिया!",  # Hindi
            "duration": 3,
            "background_color": (255, 100, 100)
        },
        {
            "text": "Hola mundo!",  # Spanish
            "duration": 3,
            "background_color": (100, 255, 100)
        }
    ]
}
```

---

## 📝 Next Steps

- [x] Basic voice generation
- [x] Modi/Trump/Kid/Robot voices
- [x] Custom parameters
- [ ] Background music
- [ ] Subtitles
- [ ] Advanced audio effects
- [ ] Real voice cloning (Eleven Labs API)

---

## 📞 Support

अगर कोई problem हो तो:
1. `voice_changer_demo.py` run करके देखो
2. `list_available_voices()` से voices check करो
3. अपने system पर TTS test करो

---

**Happy Video Creating!** 🎬✨
````
