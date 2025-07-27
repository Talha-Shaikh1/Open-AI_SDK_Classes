from agents import set_default_openai_api, set_tracing_disabled, set_default_openai_client, Agent, Runner
from module_config import external_client

set_tracing_disabled(True)
set_default_openai_api('chat_completions')
set_default_openai_client(external_client)

agent = Agent(
    name="HelloWorldAgent",
    instructions="An agent that prints a greeting message.",
    model='gemini-2.0-flash'
)

result = Runner.run_sync(agent, "Hello how are u?")
print(result.final_output)