import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
import uuid

# Page setup
st.set_page_config(page_title="🧠 Memory Chatbot")
st.title("💬 Chatbot with Memory + Sessions")

# Initialize session storage
if "all_sessions" not in st.session_state:
    st.session_state.all_sessions = {}
if "current_session_id" not in st.session_state:
    session_id = str(uuid.uuid4())[:8]
    st.session_state.current_session_id = session_id
    st.session_state.all_sessions[session_id] = {
        "messages": [],
        "system_prompt": "You are a helpful assistant.",
        "memory": ConversationBufferMemory(return_messages=True)
    }

# Sidebar for session control
with st.sidebar:
    st.header("⚙️ Settings")

    # System Prompt
    new_prompt = st.text_area(
        "System Prompt (Context)",
        value=st.session_state.all_sessions[st.session_state.current_session_id]["system_prompt"],
        height=100
    )
    st.session_state.all_sessions[st.session_state.current_session_id]["system_prompt"] = new_prompt

    # Temperature
    temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1)

    # Session Selection
    session_ids = list(st.session_state.all_sessions.keys())
    selected_session = st.selectbox("Chat Session ID", session_ids, index=session_ids.index(st.session_state.current_session_id))
    if selected_session != st.session_state.current_session_id:
        st.session_state.current_session_id = selected_session
        st.rerun()

    # New Session
    if st.button("➕ New Session"):
        new_id = str(uuid.uuid4())[:8]
        st.session_state.all_sessions[new_id] = {
            "messages": [],
            "system_prompt": "You are a helpful assistant.",
            "memory": ConversationBufferMemory(return_messages=True)
        }
        st.session_state.current_session_id = new_id
        st.rerun()

    # Reset Session
    if st.button("🔄 Reset Current Session"):
        sid = st.session_state.current_session_id
        st.session_state.all_sessions[sid]["messages"] = []
        st.session_state.all_sessions[sid]["memory"] = ConversationBufferMemory(return_messages=True)
        st.rerun()

# Load current session
session = st.session_state.all_sessions[st.session_state.current_session_id]

# Display history
for msg in session["messages"]:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# Input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    session["messages"].append(HumanMessage(content=prompt))
    session["memory"].chat_memory.add_user_message(prompt)

    # Add system message if first time
    if not any(isinstance(m, SystemMessage) for m in session["memory"].chat_memory.messages):
        session["memory"].chat_memory.messages.insert(0, SystemMessage(content=session["system_prompt"]))

    # Build LLM + Chain
    llm = ChatOllama(model="llama3.2", temperature=temperature)
    chain = ConversationChain(llm=llm, memory=session["memory"], verbose=False)

    # Get Response
    response = chain.predict(input=prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    session["messages"].append(AIMessage(content=response))
    session["memory"].chat_memory.add_ai_message(response)
