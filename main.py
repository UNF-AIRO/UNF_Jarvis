"""
Assistant Set Up
"""
# Imports
from Assistant2 import Assistant_V2, Stream_Handler
from JarvisFunctions import *
from typing_extensions import override
from openai import OpenAI
from dotenv import load_dotenv
from os import environ, system
from json import loads
load_dotenv()

# Create an instance of the assistant
jARVIS: Assistant_V2 = Assistant_V2(
    client=OpenAI(
        api_key=environ['OPENAI_API_KEY']
    ),
    id=environ['ASSISTANT_ID']
)
jARVIS.Update_Assistant_Name('Jarvis')
jARVIS.Update_Assistant_Tools(Get_Function_Details())

# Create a thread to store messages
jARVIS.Create_Thread('MAIN_THREAD')

# Create a stream handler interact with the assistant
class Custom_Stream_Handler(Stream_Handler):
    def __init__(self, client, assistantName = 'Assistant'):
        super().__init__(client, assistantName)

    @override
    def Handle_Required_Actions(self, data) -> None:
        toolOutputs: list[dict] = []

        for tool in data.required_action.submit_tool_outputs.tool_calls:

            # Get the function arguments
            args: dict[str, any] = loads(tool.function.arguments)
            
            # Add a custom handler for each function call
            if tool.function.name == "Open_Webpage":
                toolOutputs.append({
                    "tool_call_id": tool.id,
                    "output": Open_Webpage(
                        url=args['url'],
                    )
                })

            elif tool.function.name == "Write_Code_Snippet":
                toolOutputs.append({
                    "tool_call_id": tool.id,
                    "output": Write_Code_Snippet(
                        codeSnippet=args['codeSnippet'],
                    )
                })

        # Submit the tool outputs
        self._Submit_Tool_Outputs(toolOutputs)

"""
TTS Set Up
"""
import Detection as dc
import TextToSpeech as s

# Select a microphone
microphoneIndex: int = dc.Select_Microphone()

"""
Main Loop
"""
system('cls')
while True:
    # Get user input
    userInput:str = dc.Get_Speech(
        micIndex=microphoneIndex
    )

    # send text to the assistant
    jARVIS.Create_Message(
        threadName='MAIN_THREAD',
        textContent=userInput
    )

    # Display user input
    print(f"User > {userInput}\n")

    # get response from the assistant
    jARVIS.Stream_Response(
        threadName='MAIN_THREAD',
        streamHandler=Custom_Stream_Handler(
            client=OpenAI(api_key=environ['OPENAI_API_KEY']),
            assistantName='Jarvis'
        )
    )

    # Speak the response
    s.Speak(
        text=jARVIS.Static_Response(
            threadName='MAIN_THREAD'
        )[-1],
        client=OpenAI(api_key=environ['OPENAI_API_KEY'])
    )
