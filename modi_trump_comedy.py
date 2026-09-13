"""
Modi vs Trump Comedy Cartoon - Funny Dialogue Script
बहुत मजेदार conversation!
"""

from agent import VideoVoiceAgent
from voice_changer import VoiceChanger
import os

def create_modi_trump_comedy():
    """Create Modi vs Trump Comedy Cartoon"""
    
    print("\n" + "="*70)
    print("🎬 MODI vs TRUMP - COMEDY CARTOON")
    print("="*70)
    
    voice_changer = VoiceChanger()
    agent = VideoVoiceAgent()
    
    # Comedy Script
    comedy_script = {
        "title": "Modi_Trump_Comedy",
        "scenes": [
            # Scene 1: Introduction
            {
                "character": "Modi",
                "text": "नमस्ते दोस्तों! मैं नरेंद्र मोदी हूँ, भारत का प्रधानमंत्री।",
                "duration": 4,
                "background_color": (255, 140, 0),  # Saffron
                "voice_type": "modi"
            },
            # Scene 2: Trump enters
            {
                "character": "Trump",
                "text": "Hello! I am Donald Trump, and I'm fabulous!",
                "duration": 3,
                "background_color": (200, 0, 0),  # Red
                "voice_type": "trump"
            },
            # Scene 3: Modi's joke
            {
                "character": "Modi",
                "text": "ट्रंप भैया, तुम्हारे बाल इतने अच्छे हैं! क्या ये असली हैं?",
                "duration": 4,
                "background_color": (255, 140, 0),
                "voice_type": "modi"
            },
            # Scene 4: Trump's reply
            {
                "character": "Trump",
                "text": "Of course they're real! And they're tremendous, the best hair ever!",
                "duration": 4,
                "background_color": (200, 0, 0),
                "voice_type": "trump"
            },
            # Scene 5: Modi's comeback
            {
                "character": "Modi",
                "text": "वाह! तुम बहुत शानदार हो! पर भारत में हम और भी अच्छे हैं!",
                "duration": 4,
                "background_color": (255, 165, 0),
                "voice_type": "modi"
            },
            # Scene 6: Trump boasts
            {
                "character": "Trump",
                "text": "Better? Impossible! Nobody is better than me, believe me!",
                "duration": 4,
                "background_color": (230, 0, 0),
                "voice_type": "trump"
            },
            # Scene 7: Modi's funny line
            {
                "character": "Modi",
                "text": "ठीक है, ठीक है! तुम भी अच्छे हो। चलो, पहलवान बनकर कुश्ती करते हैं!",
                "duration": 5,
                "background_color": (255, 140, 0),
                "voice_type": "modi"
            },
            # Scene 8: Trump's reaction
            {
                "character": "Trump",
                "text": "Wrestling? I would win! I have the strongest hands in the world!",
                "duration": 4,
                "background_color": (200, 0, 0),
                "voice_type": "trump"
            },
            # Scene 9: Kids appear
            {
                "character": "Kids",
                "text": "वाह! मोदी जी और ट्रंप भैया बहुत मजेदार हैं!",
                "duration": 3,
                "background_color": (100, 200, 255),  # Light Blue
                "voice_type": "kid"
            },
            # Scene 10: Both laugh
            {
                "character": "Modi & Trump",
                "text": "हा हा हा! हा हा हा!",
                "duration": 3,
                "background_color": (255, 200, 100),
                "voice_type": "modi"
            },
            # Scene 11: Final joke
            {
                "character": "Modi",
                "text": "ट्रंप! तुम मेरे सबसे अच्छे दोस्त हो, भले ही तुम थोड़े पागल हो!",
                "duration": 4,
                "background_color": (255, 140, 0),
                "voice_type": "modi"
            },
            # Scene 12: Trump's response
            {
                "character": "Trump",
                "text": "Crazy? I prefer 'unique and spectacular'! But yes, you're my friend too!",
                "duration": 4,
                "background_color": (200, 0, 0),
                "voice_type": "trump"
            },
            # Scene 13: Ending
            {
                "character": "Both",
                "text": "हमेशा खुश रहो सब! बाय-बाय!",
                "duration": 3,
                "background_color": (100, 255, 100),  # Green
                "voice_type": "kid"
            }
        ]
    }
    
    print("\n🎙️ Generating voice files...")
    
    # Generate voice files for each scene
    for idx, scene in enumerate(comedy_script['scenes']):
        character = scene['character']
        text = scene['text']
        voice_type = scene['voice_type']
        voice_file = os.path.join(voice_changer.voice_dir, f"comedy_{idx}_{character}.mp3")
        
        print(f"\n Scene {idx + 1}: {character}")
        print(f" Text: {text[:50]}...")
        
        if voice_type == "modi":
            voice_changer.generate_modi_voice(text, voice_file)
        elif voice_type == "trump":
            voice_changer.generate_trump_voice(text, voice_file)
        elif voice_type == "kid":
            voice_changer.generate_kid_voice(text, voice_file)
        else:
            voice_changer.generate_modi_voice(text, voice_file)
    
    print("\n" + "="*70)
    print("✅ All voice files generated!")
    print("="*70)
    
    # Print script summary
    print("\n📝 COMEDY SCRIPT SUMMARY:")
    print("-" * 70)
    for idx, scene in enumerate(comedy_script['scenes']):
        print(f"\nScene {idx + 1}: {scene['character']}")
        print(f"Text: {scene['text']}")
        print(f"Duration: {scene['duration']}s")
    
    return comedy_script


def main():
    """Run Modi-Trump Comedy"""
    print("\n" + "🎬"*35)
    print("MODI vs TRUMP - COMEDY CARTOON CREATOR")
    print("🎬"*35)
    
    try:
        comedy_script = create_modi_trump_comedy()
        
        print("\n" + "="*70)
        print("✅ COMEDY CARTOON SCRIPT READY!")
        print("="*70)
        print("\n📁 Voice files location: voices/")
        print("📝 Script: Modi vs Trump Comedy")
        print("🎬 Ready to create video animation!")
        print("\n🎉 अब तुम इस script को animation software में use कर सकते हो!")
        print("   (जैसे: Adobe Animate, Blender, या कोई और tool)")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
