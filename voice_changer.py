"""
Voice Changer Module - Create different voice styles
Supports: Modi style, Trump style, and custom voice effects
"""

import pyttsx3
import numpy as np
from scipy import signal
from scipy.io import wavfile
import os
from datetime import datetime

class VoiceChanger:
    """Create different voice styles and effects"""
    
    def __init__(self, voice_dir="voices"):
        """Initialize VoiceChanger"""
        self.voice_dir = voice_dir
        os.makedirs(voice_dir, exist_ok=True)
        self.tts_engine = pyttsx3.init()
    
    def generate_modi_voice(self, text, output_file):
        """
        Generate Modi Ji style voice
        - Deep, serious tone
        - Slower speed (authority)
        - Medium-low pitch
        """
        print(f"🎙️  Generating Modi Ji style voice: {text[:50]}...")
        
        # Set Modi's voice characteristics
        self.tts_engine.setProperty('rate', 120)      # Slower speed
        self.tts_engine.setProperty('volume', 1.0)    # Full volume
        
        # Get available voices and try to use male voice
        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[0].id)  # Male voice
        
        # Save to temp file first
        temp_file = output_file.replace('.mp3', '_temp.mp3')
        self.tts_engine.save_to_file(text, temp_file)
        self.tts_engine.runAndWait()
        
        # Apply audio processing for deeper voice
        self._process_audio_deep_voice(temp_file, output_file)
        
        print(f"✅ Modi Ji voice saved: {output_file}")
        return output_file
    
    def generate_trump_voice(self, text, output_file):
        """
        Generate Trump style voice
        - Fast, energetic speech
        - Higher pitch
        - Powerful delivery
        """
        print(f"🎙️  Generating Trump style voice: {text[:50]}...")
        
        # Set Trump's voice characteristics
        self.tts_engine.setProperty('rate', 180)      # Faster speed (energetic)
        self.tts_engine.setProperty('volume', 1.0)
        
        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[0].id)
        
        temp_file = output_file.replace('.mp3', '_temp.mp3')
        self.tts_engine.save_to_file(text, temp_file)
        self.tts_engine.runAndWait()
        
        # Apply audio processing for higher energy
        self._process_audio_high_pitch(temp_file, output_file)
        
        print(f"✅ Trump style voice saved: {output_file}")
        return output_file
    
    def generate_kid_voice(self, text, output_file):
        """
        Generate Kid style voice
        - High pitch
        - Fast speed
        - Playful tone
        """
        print(f"🎙️  Generating Kid style voice: {text[:50]}...")
        
        self.tts_engine.setProperty('rate', 160)      # Fast
        self.tts_engine.setProperty('volume', 0.9)
        
        voices = self.tts_engine.getProperty('voices')
        if len(voices) > 1:
            # Try female voice if available
            self.tts_engine.setProperty('voice', voices[1].id)
        
        temp_file = output_file.replace('.mp3', '_temp.mp3')
        self.tts_engine.save_to_file(text, temp_file)
        self.tts_engine.runAndWait()
        
        self._process_audio_high_pitch(temp_file, output_file)
        
        print(f"✅ Kid voice saved: {output_file}")
        return output_file
    
    def generate_robot_voice(self, text, output_file):
        """
        Generate Robot style voice
        - Mechanical effect
        - Robotic pitch modulation
        """
        print(f"🎙️  Generating Robot style voice: {text[:50]}...")
        
        self.tts_engine.setProperty('rate', 140)
        self.tts_engine.setProperty('volume', 1.0)
        
        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[0].id)
        
        temp_file = output_file.replace('.mp3', '_temp.mp3')
        self.tts_engine.save_to_file(text, temp_file)
        self.tts_engine.runAndWait()
        
        self._process_audio_robot(temp_file, output_file)
        
        print(f"✅ Robot voice saved: {output_file}")
        return output_file
    
    def generate_custom_voice(self, text, output_file, pitch=1.0, speed=150, voice_type='male'):
        """
        Generate custom voice with parameters
        
        Args:
            text: Text to convert
            output_file: Output file path
            pitch: Pitch multiplier (0.5-2.0, 1.0 = normal)
            speed: Speech speed (50-200)
            voice_type: 'male' or 'female'
        """
        print(f"🎙️  Generating custom voice: {text[:50]}...")
        
        self.tts_engine.setProperty('rate', speed)
        self.tts_engine.setProperty('volume', 1.0)
        
        voices = self.tts_engine.getProperty('voices')
        if voices:
            voice_idx = 1 if voice_type == 'female' and len(voices) > 1 else 0
            self.tts_engine.setProperty('voice', voices[voice_idx].id)
        
        temp_file = output_file.replace('.mp3', '_temp.mp3')
        self.tts_engine.save_to_file(text, temp_file)
        self.tts_engine.runAndWait()
        
        if pitch != 1.0:
            self._apply_pitch_shift(temp_file, output_file, pitch)
        else:
            os.rename(temp_file, output_file)
        
        print(f"✅ Custom voice saved: {output_file}")
        return output_file
    
    def _process_audio_deep_voice(self, input_file, output_file):
        """Process audio to make voice deeper (Modi style)"""
        try:
            # Read audio
            sample_rate, audio_data = wavfile.read(input_file)
            
            # Lower the pitch (make deeper)
            audio_data = self._pitch_shift(audio_data, 0.8)
            
            # Save processed audio
            wavfile.write(output_file, sample_rate, audio_data.astype(np.int16))
            os.remove(input_file)
        except Exception as e:
            print(f"⚠️  Audio processing failed, using original: {e}")
            os.rename(input_file, output_file)
    
    def _process_audio_high_pitch(self, input_file, output_file):
        """Process audio to make voice higher pitch (Trump/Kid style)"""
        try:
            sample_rate, audio_data = wavfile.read(input_file)
            
            # Raise the pitch (make higher)
            audio_data = self._pitch_shift(audio_data, 1.2)
            
            wavfile.write(output_file, sample_rate, audio_data.astype(np.int16))
            os.remove(input_file)
        except Exception as e:
            print(f"⚠️  Audio processing failed, using original: {e}")
            os.rename(input_file, output_file)
    
    def _process_audio_robot(self, input_file, output_file):
        """Process audio to make voice robotic"""
        try:
            sample_rate, audio_data = wavfile.read(input_file)
            
            # Apply effects
            audio_data = self._pitch_shift(audio_data, 1.1)
            audio_data = self._add_bit_crush(audio_data, bits=8)
            
            wavfile.write(output_file, sample_rate, audio_data.astype(np.int16))
            os.remove(input_file)
        except Exception as e:
            print(f"⚠️  Audio processing failed, using original: {e}")
            os.rename(input_file, output_file)
    
    def _pitch_shift(self, audio_data, factor):
        """Shift pitch of audio"""
        # Simple pitch shift using resampling
        indices = np.arange(0, len(audio_data), factor)
        indices = indices[indices < len(audio_data)].astype(int)
        return audio_data[indices]
    
    def _add_bit_crush(self, audio_data, bits=8):
        """Add bit crushing effect (robotic sound)"""
        max_val = 2 ** (bits - 1)
        crushed = (audio_data / 32768.0 * max_val).astype(int)
        return crushed * (32768 // max_val)
    
    def _apply_pitch_shift(self, input_file, output_file, factor):
        """Apply pitch shift to audio file"""
        try:
            sample_rate, audio_data = wavfile.read(input_file)
            shifted = self._pitch_shift(audio_data, factor)
            wavfile.write(output_file, sample_rate, shifted.astype(np.int16))
            os.remove(input_file)
        except Exception as e:
            print(f"⚠️  Pitch shift failed: {e}")
            os.rename(input_file, output_file)
    
    def list_available_voices(self):
        """List all available system voices"""
        voices = self.tts_engine.getProperty('voices')
        print("\n📻 Available Voices:")
        for idx, voice in enumerate(voices):
            print(f"{idx}: {voice.name} - {voice.languages}")
        return voices


# Helper function for easy import
def get_voice_changer():
    """Get a VoiceChanger instance"""
    return VoiceChanger()
