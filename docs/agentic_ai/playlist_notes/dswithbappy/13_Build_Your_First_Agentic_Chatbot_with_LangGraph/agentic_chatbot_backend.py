from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()
print(os.getenv("OPENAI_API_KEY") is not None)

llm = ChatOpenAI(model_name="gpt-5-nano",
                 temperature=0.7)


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    # take user query from state
    messages = state["messages"]
    # send to llm
    response = llm.invoke(messages)
    # response store state
    return {'messages': [response]}


checkpoint = MemorySaver()


graph = StateGraph(ChatState)

# add nodes
graph.add_node("chat_node", chat_node)

# add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpoint)


# initialstate = {'messages': [HumanMessage(
#     content="What is quantum computing?")]}

# response = chatbot.invoke(initialstate)


# print(response['messages'][-1].content)
