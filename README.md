
<h3 align="center">Gmail Voice Assistant</h3>

  <p align="center">
    Personal assistant that allows you to control your gmail through voice input
    <br />
</div>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Get Vocode API Key at [Vocode API](https://app.vocode.dev/)
2. Get an OpenAI API Key at [OpenAI API](https://platform.openai.com/account/api-keys)
3. Get Gmail API credentials.json, follow the guide here [Gmail API Guide](https://developers.google.com/gmail/api/quickstart/python)
4. Get Azure Speech Key [Azure API](https://azure.microsoft.com/en-us/products/api-management/?ef_id=_k_CjwKCAjwx_eiBhBGEiwA15gLNyx7zP9LxPrEZp2d4VYFjvdk0UXp2n9uZg7Xi686Kqsq9RIxjHV6ixoCzmcQAvD_BwE_k_&OCID=AIDcmm5edswduu_SEM__k_CjwKCAjwx_eiBhBGEiwA15gLNyx7zP9LxPrEZp2d4VYFjvdk0UXp2n9uZg7Xi686Kqsq9RIxjHV6ixoCzmcQAvD_BwE_k_&gad=1&gclid=CjwKCAjwx_eiBhBGEiwA15gLNyx7zP9LxPrEZp2d4VYFjvdk0UXp2n9uZg7Xi686Kqsq9RIxjHV6ixoCzmcQAvD_BwE)
5. Find your Azure Speech Region at [Azure regions](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech?tabs=streaming#prebuilt-neural-voices)
<br />
For Azure Speech region you should use the URL format. For example, if you’re using the “East US” region, the value should be “eastus”. See Azure Region list.
6. Download Whisper.cpp model at [Whisper API Model](https://github.com/ggerganov/whisper.cpp#quick-start)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/GhaithKhoja/gmail-voice-assistant
   ```
2. Install requirements using Pip
    ```sh
    pip install -r requirements.txt
    ```
3. Move your credentials.json to your project folder
4. Find your (absolute) paths for the whisper.cpp shared library file and the model you’ve just downloaded. If whisper.cpp is downloaded at /whisper.cpp, then the absolute path is /whisper.cpp/
5. Fill in your whisper path in `gmail_assistant.py`
6. Fill in your API keys in `gmail_assistant.py`

<!-- USAGE EXAMPLES -->
## Usage

1. Command the bot to join the voice channel using 
    ```sh
    python3 gmail_assistant.py
    ```
2. Say the words "read email"
3. Press any key to shutdown the conversation with the voice agent


<!-- ROADMAP -->
## Roadmap

- [ ] Add more response options such as "reply to email" or "send email"
- [ ] Use ChatGPT to craft emails and send them

<!-- CONTACT -->
## Contact

Ghaith Khoja - gkhoja@umich.edu

Project Link: https://github.com/GhaithKhoja/gmail-voice-assistant

