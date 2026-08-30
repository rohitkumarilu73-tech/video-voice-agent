import pyttsx3
from moviepy.editor import ColorClip, TextClip, concatenate_videoclips, AudioFileClip
import os
from datetime import datetime

class VideoVoiceAgent:
    """AI Agent to create videos from scripts with voice"""
    
    def __init__(self, output_dir="videos", fps=24):
        """
        Initialize the VideoVoiceAgent
        
        Args:
            output_dir: Directory to save generated videos
            fps: Frames per second for video
        """
        self.output_dir = output_dir
        self.fps = fps
        self.voice_dir = "voices"
        
        # Create directories if they don't exist
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(self.voice_dir, exist_ok=True)
        
        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 150)  # Speed
        self.tts_engine.setProperty('volume', 1.0)  # Volume
    
    def generate_voice(self, text, voice_file):
        """
        Generate voice from text using pyttsx3
        
        Args:
            text: Text to convert to speech
            voice_file: Path to save the audio file
        """
        print(f"🎙️  Generating voice for: {text[:50]}...")
        self.tts_engine.save_to_file(text, voice_file)
        self.tts_engine.runAndWait()
        print(f"✅ Voice saved: {voice_file}")
    
    def create_video_from_script(self, script):
        """
        Create a video from a script with voice
        
        Args:
            script: Dictionary containing:
                - title: Video title
                - scenes: List of scenes with text, duration, and background_color
        
        Returns:
            Path to the generated video file
        """
        clips = []
        
        print(f"\n🎬 Creating video: {script['title']}")
        print(f"📝 Total scenes: {len(script['scenes'])}\n")
        
        for idx, scene in enumerate(script['scenes']):
            print(f"Processing scene {idx + 1}/{len(script['scenes'])}...")
            
            text = scene['text']
            duration = scene['duration']
            bg_color = scene.get('background_color', (200, 200, 200))
            
            # Generate voice for this scene
            voice_file = os.path.join(self.voice_dir, f"voice_{idx}.mp3")
            self.generate_voice(text, voice_file)
            
            # Create video clip with background color
            video_clip = ColorClip(
                size=(800, 600),
                color=bg_color
            ).set_duration(duration)
            
            # Add text overlay
            txt_clip = TextClip(
                text,
                fontsize=40,
                color='white',
                font='Arial',
                size=(700, None),
                method='caption'
            ).set_duration(duration)
            
            txt_clip = txt_clip.set_position('center')
            
            # Composite video and text
            video_with_text = video_clip.composite(txt_clip)
            
            # Add audio
            audio_clip = AudioFileClip(voice_file)
            video_with_text = video_with_text.set_audio(audio_clip)
            
            clips.append(video_with_text)
        
        # Concatenate all clips
        print("\n🎞️  Combining all scenes...")
        final_video = concatenate_videoclips(clips)
        
        # Save the final video
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(self.output_dir, f"{script['title']}_{timestamp}.mp4")
        
        print(f"💾 Saving video to: {output_file}")
        final_video.write_videofile(
            output_file,
            fps=self.fps,
            verbose=False,
            logger=None
        )
        
        print(f"✅ Video created successfully: {output_file}")
        return output_file
    
    def create_video_from_json(self, json_file):
        """
        Create a video from a JSON script file
        
        Args:
            json_file: Path to JSON file containing the script
        
        Returns:
            Path to the generated video file
        """
        with open(json_file, 'r', encoding='utf-8') as f:
            script = json.load(f)
        
        return self.create_video_from_script(script)