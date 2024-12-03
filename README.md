# 🧠🎙️ AI Voice Assistant  

The **AI Voice Assistant** is a cutting-edge, real-time voice-enabled assistant built using advanced AI technologies in speech recognition, natural language understanding, and text-to-speech synthesis. It ensures seamless, human-like interaction with concise and meaningful responses, making it ideal for modern communication needs.  

## ✨ Features  

- 🎤 **Voice Activity Detection (VAD):** Leverages Silero’s robust VAD to detect when users speak, ensuring smooth conversations.  
- 🗣️ **Speech-to-Text (STT):** Powered by Deepgram for fast and highly accurate transcription.  
- 🤖 **Natural Language Processing (NLP):** Uses OpenAI’s `GPT-3.5-turbo` for intelligent, context-aware conversations.  
- 🔊 **Text-to-Speech (TTS):** Utilizes ElevenLabs for lifelike voice responses in real-time.  
- 🏠 **Multi-Zone Temperature Control (Extension):** Manage room temperatures seamlessly via AI-powered assistant functions.  

## 🛠️ Technologies Used  

- **LiveKit**: Enables real-time communication and AI integration.  
- **Silero**: Provides reliable Voice Activity Detection.  
- **Deepgram**: Ensures accurate speech-to-text functionality.  
- **OpenAI GPT**: Powers the assistant’s natural language understanding.  
- **ElevenLabs**: Delivers realistic text-to-speech synthesis.  
- **Python**: Backend development using `asyncio` for efficient operations.  

## 🚀 Installation and Setup  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/yourusername/AI-voice-assistant.git  
   cd AI-voice-assistant
2. **Install dependencies**:
   ```bash  
   pip install -r requirements.txt
3. **Set up environment variables**:
   - Create a .env file in the project root directory.
   - Add the following keys (replace with your actual API keys):
   ```bash  
   LIVEKIT_URL=wss://your_livekit_url  
   LIVEKIT_API_SECRET=your_livekit_api_secret  
   LIVEKIT_API_KEY=your_livekit_api_key  
   OPENAI_API_KEY=your_openai_api_key  
   DEEPGRAM_API_KEY=your_deepgram_api_key  
   ELEVEN_API_KEY=your_eleven_api_key
4. **Run the application**:
   ```bash  
   python main.py

## 🎯 Usage:

- Upon starting, the assistant connects to a LiveKit room and begins listening for user input.  
- Users interact via voice, receiving real-time audio responses.  
- Supports modular functionalities, such as temperature control, which can be extended or customized.

## 🔮 Future Enhancements:
- 🌍 **Multi-Language Support**: Handle multiple languages for broader accessibility.
- 🏡 **Smart Home Integration**: Control a variety of IoT devices beyond temperature.
- 🎨 **Customization**: Allow users to personalize the assistant’s voice and response style.

## 🤝 Contributing:
Contributions are welcome! Fork the repository and submit a pull request with your changes. For major updates, open an issue to discuss your idea first.

## 🙌 Acknowledgments:

Special thanks to:

- **LiveKit** for their real-time communication platform.
- **Silero** for their VAD model.
- **Deepgram** for their STT services.
- **OpenAI** for the GPT model.
- **ElevenLabs** for TTS technology.

