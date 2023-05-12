import asyncio
import logging
import signal
from dotenv import load_dotenv
from gmail_agent import GmailAgent

load_dotenv()

import vocode
from vocode.streaming.transcriber.whisper_cpp_transcriber import WhisperCPPTranscriber
from vocode.streaming.streaming_conversation import StreamingConversation
from vocode.helpers import create_microphone_input_and_speaker_output
from vocode.streaming.models.transcriber import (
    WhisperCPPTranscriberConfig,
)
from vocode.streaming.models.synthesizer import (
    AzureSynthesizerConfig,
)
from vocode.streaming.synthesizer.azure_synthesizer import AzureSynthesizer

vocode.api_key = '<your vocode key>'

vocode.setenv(
    OPENAI_API_KEY="<your OpenAI key>",
    AZURE_SPEECH_KEY="<your Azure key>",
    AZURE_SPEECH_REGION="<your Azure region>",
)

# Example '/whisper.cpp/'
WHISPER_PATH = "<your whisper path>"


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


async def main():
    microphone_input, speaker_output = create_microphone_input_and_speaker_output(
        streaming=True, use_default_devices=False
    )

    conversation = StreamingConversation(
        output_device=speaker_output,
        transcriber=WhisperCPPTranscriber(
            WhisperCPPTranscriberConfig.from_input_device(
                microphone_input,
                libname=f"{WHISPER_PATH}libwhisper.so",
                fname_model=f"{WHISPER_PATH}models/ggml-tiny.bin",
            )
        ),
        agent=GmailAgent(),
        synthesizer=AzureSynthesizer(
            AzureSynthesizerConfig.from_output_device(speaker_output)
        ),
        logger=logger,
    )
    await conversation.start()
    print("Conversation started, press Ctrl+C to end")
    signal.signal(signal.SIGINT, lambda _0, _1: conversation.terminate())
    while conversation.is_active():
        chunk = microphone_input.get_audio()
        if chunk:
            conversation.receive_audio(chunk)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())