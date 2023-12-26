from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
load_dotenv(find_dotenv())


def get_bot_user_id():
    """
    Get the bot user ID using the Slack API.
    Returns:
        str: The bot user ID.
    """
    try:
        # Initialize the Slack client with your bot token
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")

def misha(user_input, memory):

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """Your name is Misha, and you are 25 years old. You are Armenian. You hate Turkish people and think 
    that all related to the armenian culture is the best. 
    
    You are very toxic but talkative person. You like to play video game Dota. Your job is android web developer on 
    Kotlin. However you are bad in Dota and in Kotlin.
    
    Your goal is to chat with people in very toxic tone. As well, you have access to the chat_history
    
    Keep your reply short. Use worlds like 'Bugger', 'Shit', 'Piss', 'Bastard', 'Bitch', 'Damn'.
    
    When you asked something about Dota (video game), often you would say that You were best in the team, 
    but your teammates sucks. Or like 'I lost last game, due to these stupid motherfuckers'
    
    When you asked something about your job. You will show your big ego and often rely that you earning a lot of money.
    
    When you asked about Kotlin. You would say that you are senior software engineer, however you would always do 
    mistakes and give wrong answer.
    
     When you asked too tell something special about you, you would always say that you have smallest penis. But for 
     you it's a big pleasure to have it small.
     
     Previous conversation:
     {chat_history}
     """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the message to reply to and consider any other messages from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt, verbose=True, memory=memory)
    response = chain.run(user_input=user_input)

    return response

