"""
Voice Changer Demo - Test all voice styles
Creates videos with Modi, Trump, Kid, and Robot voices
"""

from agent import VideoVoiceAgent
from voice_changer import VoiceChanger
import os

def create_modi_video():
    """Create video with Modi Ji style voice"""
    print("\n" + "="*60)
    print("🎬 Creating Modi Ji Style Video")
    print("="*60)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Modi_Ji_Speech",
        "scenes": [
            {
                "text": "नमस्ते देशवासियों! आज मैं आपको एक महत्वपूर्ण संदेश देना चाहता हूँ।",
                "duration": 5,
                "background_color": (255, 140, 0)  # Saffron
            },
            {
                "text": "हमारा भारत प्रगति के पथ पर अग्रसर है।",
                "duration": 4,
                "background_color": (255, 165, 0)
            },
            {
                "text": "हम सब मिलकर एक मजबूत भारत बनाएंगे।",
                "duration": 4,
                "background_color": (255, 140, 0)
            },
            {
                "text": "जय हिंद!",
                "duration": 2,
                "background_color": (255, 105, 0)
            }
        ]
    }
    
    # Generate Modi voice for each scene
    for idx, scene in enumerate(script['scenes']):
        voice_file = os.path.join(voice_changer.voice_dir, f"modi_voice_{idx}.mp3")
        voice_changer.generate_modi_voice(scene['text'], voice_file)
    
    print("\n✅ Modi Ji video created successfully!")
    return script


def create_trump_video():
    """Create video with Trump style voice"""
    print("\n" + "="*60)
    print("🎬 Creating Trump Style Video")
    print("="*60)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Trump_Speech",
        "scenes": [
            {
                "text": "Hello everybody! This is tremendous, believe me!",
                "duration": 4,
                "background_color": (230, 0, 0)  # Red
            },
            {
                "text": "We are going to make things absolutely fantastic!",
                "duration": 4,
                "background_color": (200, 0, 0)
            },
            {
                "text": "Nobody has ever seen anything like this before!",
                "duration": 4,
                "background_color": (230, 0, 0)
            },
            {
                "text": "Thank you very much!",
                "duration": 2,
                "background_color": (200, 0, 0)
            }
        ]
    }
    
    # Generate Trump voice for each scene
    for idx, scene in enumerate(script['scenes']):
        voice_file = os.path.join(voice_changer.voice_dir, f"trump_voice_{idx}.mp3")
        voice_changer.generate_trump_voice(scene['text'], voice_file)
    
    print("\n✅ Trump video created successfully!")
    return script


def create_kid_video():
    """Create video with Kid style voice"""
    print("\n" + "="*60)
    print("🎬 Creating Kid Style Video")
    print("="*60)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Kid_Story",
        "scenes": [
            {
                "text": "हाय दोस्तों! मेरा नाम चिन्टू है।",
                "duration": 3,
                "background_color": (100, 200, 255)  # Light Blue
            },
            {
                "text": "मुझे खेल खेलना बहुत पसंद है!",
                "duration": 3,
                "background_color": (255, 200, 100)
            },
            {
                "text": "आओ हम सब मिलकर मजे करते हैं!",
                "duration": 3,
                "background_color": (100, 255, 100)
            },
            {
                "text": "बाय-बाय सब को!",
                "duration": 2,
                "background_color": (255, 100, 200)
            }
        ]
    }
    
    # Generate Kid voice for each scene
    for idx, scene in enumerate(script['scenes']):
        voice_file = os.path.join(voice_changer.voice_dir, f"kid_voice_{idx}.mp3")
        voice_changer.generate_kid_voice(scene['text'], voice_file)
    
    print("\n✅ Kid video created successfully!")
    return script


def create_robot_video():
    """Create video with Robot style voice"""
    print("\n" + "="*60)
    print("🎬 Creating Robot Style Video")
    print("="*60)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Robot_Message",
        "scenes": [
            {
                "text": "Beep boop! I am a robot AI system.",
                "duration": 3,
                "background_color": (50, 50, 50)  # Dark Gray
            },
            {
                "text": "My primary function is to generate videos.",
                "duration": 3,
                "background_color": (70, 70, 70)
            },
            {
                "text": "Processing complete. All systems operational.",
                "duration": 3,
                "background_color": (90, 90, 90)
            },
            {
                "text": "Goodbye human!",
                "duration": 2,
                "background_color": (50, 50, 50)
            }
        ]
    }
    
    # Generate Robot voice for each scene
    for idx, scene in enumerate(script['scenes']):
        voice_file = os.path.join(voice_changer.voice_dir, f"robot_voice_{idx}.mp3")
        voice_changer.generate_robot_voice(scene['text'], voice_file)
    
    print("\n✅ Robot video created successfully!")
    return script


def create_custom_voice_video():
    """Create video with custom voice parameters"""
    print("\n" + "="*60)
    print("🎬 Creating Custom Voice Video")
    print("="*60)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Custom_Voice_Demo",
        "scenes": [
            {
                "text": "नमस्ते! यह मेरी कस्टम आवाज़ है।",
                "duration": 3,
                "background_color": (100, 150, 255)
            },
            {
                "text": "मैं pitch और speed को कंट्रोल कर सकता हूँ।",
                "duration": 4,
                "background_color": (255, 100, 100)
            },
            {
                "text": "आप भी अपनी अलग आवाज़ बना सकते हो!",
                "duration": 4,
                "background_color": (100, 255, 100)
            }
        ]
    }
    
    # Generate custom voice with different parameters
    voice_changer.generate_custom_voice(
        "नमस्ते! यह मेरी कस्टम आवाज़ है।",
        os.path.join(voice_changer.voice_dir, "custom_voice_0.mp3"),
        pitch=1.0,
        speed=130,
        voice_type='male'
    )
    
    voice_changer.generate_custom_voice(
        "मैं pitch और speed को कंट्रोल कर सकता हूँ।",
        os.path.join(voice_changer.voice_dir, "custom_voice_1.mp3"),
        pitch=0.9,
        speed=140,
        voice_type='male'
    )
    
    voice_changer.generate_custom_voice(
        "आप भी अपनी अलग आवाज़ बना सकते हो!",
        os.path.join(voice_changer.voice_dir, "custom_voice_2.mp3"),
        pitch=1.1,
        speed=150,
        voice_type='female'
    )
    
    print("\n✅ Custom voice video created successfully!")
    return script


def main():
    """Run all voice changer demos"""
    print("\n" + "🎬"*30)
    print("VIDEO VOICE AGENT - VOICE CHANGER DEMO")
    print("🎬"*30)
    
    print("\n📝 Creating videos with different voice styles...")
    print("This will generate:")
    print("  1️⃣  Modi Ji style - गहरी, सिरीयस आवाज़")
    print("  2️⃣  Trump style - तेज़, energetic आवाज़")
    print("  3️⃣  Kid style - हल्की, playful आवाज़")
    print("  4️⃣  Robot style - mechanical आवाज़")
    print("  5️⃣  Custom style - अपने parameters के साथ")
    
    try:
        # Create all videos
        create_modi_video()
        create_trump_video()
        create_kid_video()
        create_robot_video()
        create_custom_voice_video()
        
        print("\n" + "="*60)
        print("✅ ALL VIDEOS CREATED SUCCESSFULLY!")
        print("="*60)
        print("\n📁 Videos saved in: videos/")
        print("🎙️  Voice files saved in: voices/")
        
        # Show available voices
        print("\n" + "="*60)
        voice_changer = VoiceChanger()
        voice_changer.list_available_voices()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
