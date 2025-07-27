from agents import  AsyncOpenAI, OpenAIChatCompletionsModel


external_client = AsyncOpenAI(
    api_key='AIzaSyDUM3mvFpKM5pR6tAKxClTFG-rBSzmhNTA',
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

external_model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=external_client,
)