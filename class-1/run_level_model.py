from agents import Agent, Runner , RunConfig
from module_config import external_model

config = RunConfig(
    model=external_model,
    tracing_disabled=True
)

assistant = Agent(
    name="HelloWorldAgent",
    instructions="An agent that prints a greeting message."
)

result = Runner.run_sync(assistant, "Hello how are u?", run_config=config)
print(result.final_output)