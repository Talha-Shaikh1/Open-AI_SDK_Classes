from agents import Agent, RunContextWrapper, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig, handoff

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

Bussiness_Agent = Agent(
    name= "Bussiness Agent",
    instructions="You are a helpful Bussiness programming assistant.",
)

Python_Agent = Agent(
    name= "Python Agent",
    instructions="You are a helpful Python programming assistant.",
)

General_Agent = Agent(
    name= "General Agent",
    instructions="You are a helpful assistant.",
)

def on_handoff(ctx: RunContextWrapper[None]):
    print("Handoff to Bussiness Agent initiated.")
    
def on_python_handoff(ctx: RunContextWrapper[None]):
    print("Handoff to Python Agent initiated.")
    
def on_general_handoff(ctx: RunContextWrapper[None]):
    print("Handoff to General Agent initiated.")

python_handoff = handoff(
    agent=Python_Agent,
    on_handoff=on_python_handoff,
    tool_name_override="go_to_python_agent",
    tool_description_override="This is a Python Agent that helps with python programing questions."
)


handoff_object = handoff(
    agent= Bussiness_Agent,
    on_handoff=on_handoff,
    tool_name_override="Go_to_Bussiness_Agent",
    tool_description_override="This is a Bussiness Agent that can help with business-related queries."
)

general_handoff = handoff(
    agent= General_Agent,
    on_handoff=on_general_handoff,
    tool_name_override="Go_to_General_Agent",
    tool_description_override="This is a General Agent that can help with general queries."
)



Triage_Agent = Agent(
    name= "Triage Agent",
    instructions=(
        "You are a Triage Agent that decides which agent should handle the query.\n"
        "- If the query is related to Python or programming, hand it off to the Python Agent.\n"
        "- If the query is about business, hand it off to the Business Agent.\n"
        "- If the query doesn't match either, hand it off to the General Agent."
        ),
    handoffs=[handoff_object, python_handoff,general_handoff],
)

result = Runner.run_sync(
    Triage_Agent,input="mjhy roman urdu men kahani sunao achi si",
    run_config=config)

print("Result:", result.final_output)
print("Handoff Agent:", result.last_agent.name)