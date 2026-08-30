import os
import json
from agent import VideoVoiceAgent

def main():
    """Main entry point for the video-voice agent"""
    
    # Initialize the agent
    agent = VideoVoiceAgent()
    
    # Example script
    sample_script = {
        "title": "My First Video",
        "scenes": [
            {
                "text": "Hello! This is my first AI generated video.",
                "duration": 3,
                "background_color": (100, 150, 255)
            },
            {
                "text": "The agent can create videos from scripts automatically.",
                "duration": 3,
                "background_color": (255, 100, 100)
            },
            {
                "text": "Thank you for watching!",
                "duration": 2,
                "background_color": (100, 255, 100)
            }
        ]
    }
    
    # Create video from script
    print("🎬 Starting video generation...")
    output_file = agent.create_video_from_script(sample_script)
    print(f"✅ Video created: {output_file}")

if __name__ == "__main__":
    main()