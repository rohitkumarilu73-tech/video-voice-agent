"""
Advanced example showing how to use VideoVoiceAgent for complex scenarios
"""

from agent import VideoVoiceAgent
import json

def create_english_video():
    """Create an English video"""
    agent = VideoVoiceAgent()
    
    script = {
        "title": "English_Tutorial",
        "scenes": [
            {
                "text": "Welcome to AI Video Generation!",
                "duration": 3,
                "background_color": (0, 100, 200)
            },
            {
                "text": "This agent creates videos from scripts automatically.",
                "duration": 4,
                "background_color": (200, 100, 0)
            },
            {
                "text": "You can customize colors, duration, and text.",
                "duration": 4,
                "background_color": (100, 200, 0)
            },
            {
                "text": "Thanks for watching!",
                "duration": 2,
                "background_color": (200, 0, 100)
            }
        ]
    }
    
    return agent.create_video_from_script(script)


def create_hindi_video():
    """Create a Hindi video"""
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Hindi_Tutorial",
        "scenes": [
            {
                "text": "नमस्ते! मैं एक AI agent हूँ।",
                "duration": 3,
                "background_color": (255, 153, 0)
            },
            {
                "text": "मैं स्क्रिप्ट से वीडियो बना सकता हूँ।",
                "duration": 4,
                "background_color": (51, 102, 255)
            },
            {
                "text": "मैं आवाज भी जोड़ सकता हूँ।",
                "duration": 4,
                "background_color": (102, 255, 102)
            },
            {
                "text": "धन्यवाद!",
                "duration": 2,
                "background_color": (255, 102, 178)
            }
        ]
    }
    
    return agent.create_video_from_script(script)


def create_mixed_language_video():
    """Create a video with mixed languages"""
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Mixed_Language_Video",
        "scenes": [
            {
                "text": "Hello! नमस्ते!",
                "duration": 3,
                "background_color": (100, 100, 255)
            },
            {
                "text": "This is bilingual content.",
                "duration": 3,
                "background_color": (255, 100, 100)
            },
            {
                "text": "यह content multilingual है।",
                "duration": 3,
                "background_color": (100, 255, 100)
            }
        ]
    }
    
    return agent.create_video_from_script(script)


def create_story_video():
    """Create a story-based video"""
    agent = VideoVoiceAgent()
    
    script = {
        "title": "Story_Adventure",
        "scenes": [
            {
                "text": "एक बार की बात है...",
                "duration": 3,
                "background_color": (100, 50, 100)
            },
            {
                "text": "एक छोटा सा गाँव था।",
                "duration": 3,
                "background_color": (150, 100, 50)
            },
            {
                "text": "वहाँ एक जादूगर रहता था।",
                "duration": 4,
                "background_color": (100, 150, 200)
            },
            {
                "text": "वह हर दिन अद्भुत चीजें करता था।",
                "duration": 4,
                "background_color": (200, 150, 100)
            },
            {
                "text": "और यही कहानी का अंत है।",
                "duration": 3,
                "background_color": (150, 100, 150)
            }
        ]
    }
    
    return agent.create_video_from_script(script)


def batch_create_videos():
    """Create multiple videos from JSON files"""
    scripts = ["sample_script.json"]
    
    agent = VideoVoiceAgent()
    
    for script_file in scripts:
        try:
            print(f"\n📹 Creating video from {script_file}...")
            agent.create_video_from_json(script_file)
        except Exception as e:
            print(f"❌ Error creating video from {script_file}: {e}")


if __name__ == "__main__":
    print("🎬 Video Voice Agent - Advanced Examples\n")
    
    # Uncomment the one you want to run:
    
    # 1. English Video
    print("Creating English video...")
    create_english_video()
    
    # 2. Hindi Video
    # print("Creating Hindi video...")
    # create_hindi_video()
    
    # 3. Mixed Language Video
    # print("Creating mixed language video...")
    # create_mixed_language_video()
    
    # 4. Story Video
    # print("Creating story video...")
    # create_story_video()
    
    # 5. Batch Create from JSON
    # print("Creating videos from JSON files...")
    # batch_create_videos()
    
    print("\n✅ Done!")