from agents import Agent, Handoff, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, handoff

external_client = AsyncOpenAI(
    api_key='AIzaSyDUM3mvFpKM5pR6tAKxClTFG-rBSzmhNTA',
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
) 

external_model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=external_client,
)

config = RunConfig(
    model=external_model,
    tracing_disabled=True,
)

Python_Agent = Agent(
    name= "Python Agent",
    instructions="You are a helpful Python programming assistant.",
)

Nextjs_Agent = Agent(
    name= "Next.js Agent",
    instructions="You are a helpful Next.js programming assistant.",
)

Triage_Agent = Agent(
    name= "Triage Agent",
    model=external_model,
    instructions="You are a helpful assistant that navigates between different agents based on the user's query.",
    handoffs=[Python_Agent, handoff(Nextjs_Agent)], # we can also use handoff() function to customize handoffs
)



result = Runner.run_sync(Triage_Agent, "what is the routing in nextjs and how to use it?", run_config=config)

print("Final Output" ,result.final_output)

print("Last Agent Used:", result.last_agent.name)


print("'Python Agent default description by SDK'...", Handoff.default_tool_description(Python_Agent))
print("'Nextjs Agent default description by SDK'...", Handoff.default_tool_description(Nextjs_Agent))
