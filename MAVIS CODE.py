from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
import ast
from langchain_core.prompts import PromptTemplate
load_dotenv()

# Initialize model
model= ChatGoogleGenerativeAI(model= "gemini-2.5-pro")

# Parser SettingUP
parser= StrOutputParser()

# LIVE SEARCH TOOL
from langchain_community.tools import DuckDuckGoSearchRun

search= DuckDuckGoSearchRun()

def Search_Func(query: str) -> str:
    """
    This tool uses DuckDuckGo Search Engine to find the answer of any general query.
    This tool take one input argument (query) that is of string datatype, search that query on DuckDuckGo and return the result in string format.
    """
    response= search.invoke(query)
    return response

Search_Tool= Tool(
    name= "Searching Tool",
    func= Search_Func,
    description=(
        "This tool is used to search any query on the internet"
        "Example: Suppose Query is 'Today weather of Newyork', so this query will be go to the DuckDuckGo Search Engine, it compute the result and Return that result back."
    )
)

# GMAIL SEND TOOL
from langchain_google_community.gmail.send_message import GmailSendMessage
Gmail_Send= GmailSendMessage()

def Gmail_Send_Func(to_sub_message: list) -> str:
    """
    This function will send the mail using GmailSendMessage tool.
    This function will take one list as input, and list contains 3 variable first is to, second is subject and third is message.
    Example: ['abc@gmail.com', 'Thankyou', 'This is the body.']
    """

    To_Sub_Message= ast.literal_eval(to_sub_message)
    email_input = {
        "to": To_Sub_Message[0],
        "subject": To_Sub_Message[1],
        "message": To_Sub_Message[2]
    }
    result = Gmail_Send.run(email_input)
    return result

Gmail_Send_Tool = Tool(
    name="Gmail_Send_Tool",
    func=Gmail_Send_Func,
    description=(
        "Send an email using Gmail. Provide 'to', 'subject', and 'message' in a list. "
        "Example: Send an email to 'john@example.com' with subject 'Meeting' and message 'Let's meet tomorrow.'"
    )
)

# GMAIL SEARCH I.E. SUMMARIZE TOOLS
from langchain_google_community.gmail.search import GmailSearch

Gmail_Search = GmailSearch()

def Gmail_Search_Func(query: list) -> str:
    """
    This tool fetches the top x number of mails(mention in query) and based on the user query it perform any task on those mail.
    This tool take one list in input, the list contains two elements first is query and second is Total Number of Mails required for search.
    Example: ['Summarize these mails in simple words.', 7]
    """
    Query= ast.literal_eval(query)
    query_input = {
        "query": "",       # Empty string = get everything
        "max_results": Query[1]  # Limit to top 10 emails
    }
    user_query= Query[0]
    # Run the search
    all_mails = Gmail_Search.run(query_input)
   
    prompt = PromptTemplate(
        template=""" 
                    You are a Helpful Assistant!
                    I will give you a list of emails and a user query, and you have to understand the User Query properly and whatever the user query related to this emails answer them accordingly.
                    The emails contain some meta-data like ID and threadID — please ignore these.
                    This is the User Query: {user_query} and 
                    These are the emails: {all_mails}
                    
                """,
        input_variables=["all_mails", "user_query"]
    )

    chain = prompt | model | parser
    finalResult= chain.invoke({'all_mails':all_mails,'user_query':user_query})
    return finalResult


Gmail_Search_Tool= Tool(
    name= "Gmail_Search_Tool",
    func= Gmail_Search_Func,
    description= (
        "Use this tool to perform any task to the mails like Summary of mails, Find Important Mails etc."
        "The fucntion take one arguments i.e. list, first element of the list is query and second element is top n mails on which we have to perform task"
        "For Example: ['Tell me the summary of mails',10] "
    )
)


# SMS/ WHATSAPP TOOL using TWILIO
from langchain_community.utilities.twilio import TwilioAPIWrapper

twilio_Message = TwilioAPIWrapper(
        account_sid="your_account_side_comes",
        auth_token="your_auth_token_number_comes",
        from_number="+your_phone_number"
)

def twilio_Message_Func(message_number: list) -> str:
    """
    This function will send whatsapp message to the particular phone number.
    This function will take one list as inputs which contains two elements: first element is message and second element is phone number.
    """
    Message_Number= ast.literal_eval(message_number)
    send= twilio_Message.run(Message_Number[0],Message_Number[1])
    print("The message Send successfully: ")
    return send

twilio_Message_Tool= Tool(
    name= "twilio_Message_Tool",
    func= twilio_Message_Func,
    description= (
        "Use this tool to send any whatsapp message."
        "The fucntion take one arguments i.e. list, first element of the list is message and second element is phone number."
        "For Example: 'This is the message',+910987654321 "
    )
)

slashPrompt= " use proper slashes before any single quote or double quotes in between the message"



prompt = hub.pull("hwchase17/react")
agent= create_react_agent(
    llm= model,
    tools= [Search_Tool,Gmail_Send_Tool, twilio_Message_Tool, Gmail_Search_Tool],
    prompt= prompt
)

agentExecutor= AgentExecutor(
    agent= agent,
    tools= [Search_Tool,Gmail_Send_Tool, twilio_Message_Tool, Gmail_Search_Tool],
    verbose= True,
    handle_parsing_errors=True
)

# STREAM LIT CODE UI
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Smart AI Assistant", layout="centered")

# Title
st.title("🤖 MAVIS BOT")

# Define multi-line placeholder with bullet points
placeholder_text = (
    "🔹 What I can do for you:\n"
    "• Send Emails\n"
    "• Retrieve and Summarize Emails\n"
    "• Generate Smart Email Replies\n"
    "• Perform Live Web Searches\n"
    "• Send WhatsApp Messages\n"
    "• Send SMS/Text Messages\n\n"
    "💬 Just type your request below in simple language..."
)

# Large input box with placeholder
user_input = st.text_area("Your Request", placeholder=placeholder_text, height=200)

# Button to trigger action
if st.button("🚀 Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a prompt to proceed.")
    else:
        with st.spinner("Processing your request..."):
            try:
                # Replace with your actual AI agent logic
                queryResult= agentExecutor.invoke({
                                                    "input": f"{user_input} and {slashPrompt}"
                                                })
                st.write(queryResult["output"])
            except Exception as e:
                st.error("❌ Something went wrong.")
                st.exception(e)
