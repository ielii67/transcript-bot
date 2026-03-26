# Discord Audio Transcription Bot

A Discord bot that automatically transcribes uploaded audio files using [AssemblyAI](https://www.assemblyai.com/).  
It supports common formats like `.mp3`, `.wav`, `.ogg`, `.flac`, and `.m4a`.
> Note: Discord does not allow accessing voice messages as files so this bot does not transcribe voice messages, only uploaded audio files!

## Features
- :microphone2: Transcribes audio files uploaded directly into Discord channels.
- :paperclip: Handles forwarded messages with audio attachments.
- :warning: Detects Discord voice messages and politely informs users that these cannot be transcribed (Discord does not expose voice message audio to bots).
- :key: Uses environment variables for secure API key and token management.

## Installation
1. Clone this repository:
   ```git clone https://github.com/ielii67/transcript-bot.git```
   ```cd transcript-bot```
2. Create and activate a virtual environment:
```python -m venv .venv```
3. Install dependencies:
```pip install -r requirements.txt```
4. Create a .env file in the project root:
```Create a .env file in the project root:```
    ```ASSEMBLYAI_API_KEY = YOUR KEY```
    ```DISCORD_TOKEN = YOUR TOKEN```

## How to Run the Bot
   ```python main.py```

## Important Notes and Limitations
- Bots cannot access Discord voice messages. Only uploaded audio files can be transcribed.
- Long audio files may take time to process. You can optimize the transcription time with the following changes:
> ```transcript_text = await asyncio.to_thread(transcribe, audio)```
> ```await message.channel.send(f"{message.author.mention} - {transcript_text}")```
- The bot must have the Message Content Intent enabled in the Discord Developer Portal.

## License
This repository is free to clone, share, and use for learning purposes. Anyone is welcome to study the code, optimize it, add new features, or adapt it for their own projects.
> If you build on this project, a note of credit is appreciated but not required.