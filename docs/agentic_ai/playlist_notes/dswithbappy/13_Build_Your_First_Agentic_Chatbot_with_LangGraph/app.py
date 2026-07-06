from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
import streamlit as st


st.title("Agentic Chatbot with LangGraph")

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

 # Loading conversation history from session state
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


def userquestion(user_input: str):
    thread_id = "1"
    config = {'configurable': {'thread_id': thread_id}}

    initialstate = {'messages': [HumanMessage(content=user_input)]}

    # full response
    response = chatbot.invoke(initialstate, config=config)
    return response['messages'][-1].content


# response = chatbot.invoke(
#     {'messages': [HumanMessage(content="What is capital of india?")]}, config=config)
# print(response['messages'][-1].content)
userinput = st.chat_input("Ask a question")


# Full response waiting

# if userinput:
#     st.session_state['message_history'].append(
#         {'role': 'user', 'content': userinput})

#     with st.chat_message("user"):
#         st.text(userinput)

#         response = userquestion(userinput)
#         st.session_state['message_history'].append(
#             {'role': 'assistant', 'content': response})

#     with st.chat_message("assistant"):
#         st.text(response)


# Streaming response
if userinput:
    CONFIG = {'configurable': {'thread_id': 'thread-1'}}
    st.session_state['message_history'].append(
        {'role': 'user', 'content': userinput})

    with st.chat_message("user"):
        st.text(userinput)

        response = userquestion(userinput)
        st.session_state['message_history'].append(
            {'role': 'assistant', 'content': response})

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=userinput)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    st.session_state['message_history'].append(
        {'role': 'assistant', 'content': ai_message})
