import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Page setup
st.set_page_config(page_title="🧠 Memory Chatbot")
st.title("💬 Ollama Based Langchain Chatbot")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Settings")
    temperature = st.slider("Temperature", 0.0, 2.0, 1.0, 0.1)
    system_prompt = st.text_area(
        "System Prompt (Context)",
        value=st.session_state.get("system_prompt", "You are a helpful assistant."),
        height=100
    )
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.session_state.system_prompt = system_prompt
        st.session_state.memory = None
        st.rerun()

# Initialize messages and memory if not present
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.system_prompt = system_prompt

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Display chat history
for message in st.session_state.messages:
    role = "user" if isinstance(message, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(message.content)

# Input box
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Add user message to UI and memory
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(HumanMessage(content=prompt))
    st.session_state.memory.chat_memory.add_user_message(prompt)

    # Load LLM and conversation chain with memory
    llm = ChatOllama(model="llama3.2", temperature=temperature)
    chain = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )

    # Generate response
    response = chain.predict(input=prompt)

    # Display and store response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(AIMessage(content=response))
    st.session_state.memory.chat_memory.add_ai_message(response)
