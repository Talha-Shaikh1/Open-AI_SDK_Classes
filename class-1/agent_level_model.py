from agents import Agent, Runner, RunConfig
from module_config import external_model

assistant = Agent(
    name="HelloWorldAgent",
    instructions="An agent that prints a greeting message.",
    model=external_model,
)


result = Runner.run_sync(assistant, "Hello how are u?")

print(result.final_output)