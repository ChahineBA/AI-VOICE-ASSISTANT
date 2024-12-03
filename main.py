from dotenv import load_dotenv
import asyncio
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero, deepgram, elevenlabs
from api import AssistantFnc

# Load environment variables from a .env file
load_dotenv()

# Define the asynchronous entry point function for the application
async def entrypoint(ctx: JobContext):
    # Create an initial chat context for the voice assistant with system instructions
    initial_ctx = llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, avoiding usage of unpronouncable punctuation."
        ),
    )
    
    # Connect to the context, subscribing only to audio streams
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    
    # Initialize the functional context for the assistant (custom functionality)
    fnc_ctx = AssistantFnc()
    
    # Instantiate the VoiceAssistant with necessary components:
    # - Voice Activity Detection (VAD) using Silero
    # - Speech-to-Text (STT) using Deepgram
    # - Large Language Model (LLM) using OpenAI's GPT-3.5 Turbo
    # - Text-to-Speech (TTS) using ElevenLabs
    # - Chat context and functional context
    assistant = VoiceAssistant(
        vad=silero.VAD.load(),
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-3.5-turbo"),
        tts=elevenlabs.TTS(),
        chat_ctx=initial_ctx,
        fnc_ctx=fnc_ctx
    )
    
    # Start the voice assistant in the connected room
    assistant.start(ctx.room)
    
    # Introduce a small delay to ensure smooth operation
    await asyncio.sleep(1)
    
    # Make the assistant greet the user with an introductory message
    await assistant.say("Hey, How can I help you today!", allow_interruptions=True)

# Entry point for the application
if __name__ == "__main__":
    # Run the application with the entrypoint function and worker options
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
