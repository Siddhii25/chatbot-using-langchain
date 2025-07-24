# Ollama-based LangChain Chatbot

A conversational AI application leveraging **Streamlit**, **LangChain**, and **Ollama (LLaMA3.2)** to deliver contextual conversations with persistent session memory through LangChain's `ConversationBufferMemory`.

## Key Features

- **Interactive Web Interface**: Intuitive chat experience powered by Streamlit
- **Dynamic System Configuration**: Customizable AI behavior and response parameters
- **Session Memory Management**: Maintains conversation context throughout the session
- **Conversation Reset Capability**: Clear chat history and start fresh conversations
- **Local Model Integration**: Seamless integration with locally hosted Ollama models

---

## Repository

**GitHub**: [Siddhii25/chatbot-using-langchain](https://github.com/Siddhii25/chatbot-using-langchain.git)

---

## Technology Stack

- **Python 3.9+** – Core programming language
- **Streamlit** – Web application framework
- **LangChain** – Large Language Model orchestration and memory management
- **langchain-ollama** – Ollama integration layer for LangChain
- **Ollama** – Local large language model inference engine

---

## Installation Guide

### Prerequisites Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Siddhii25/chatbot-using-langchain.git
   cd chatbot-using-langchain
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   # venv\Scripts\activate        # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Ollama Configuration

1. **Download and Install Ollama**
   
   Visit [https://ollama.com/download](https://ollama.com/download) to download the appropriate version for your operating system.

2. **Initialize Language Model**
   ```bash
   ollama run llama3:instruct
   ```
   
   > **Note**: Ensure the model name in your application configuration matches the installed model (e.g., `llama3.2`, `llama3:instruct`).

---

## Application Deployment

Launch the application using Streamlit:

```bash
streamlit run app.py
```

> Replace `app.py` with your main application file if using a different filename.

---

## User Guide

### Configuration Panel (Sidebar)

- **Temperature Control**: Adjusts the creativity and randomness of AI responses (0.0 = deterministic, 1.0 = highly creative)
- **System Prompt Configuration**: Define the AI's behavior profile (e.g., professional assistant, educational tutor, technical expert)
- **Conversation Reset**: Clear current session memory and initialize a new conversation thread

### Chat Interface

- **Message Input**: Submit queries and engage in natural conversation
- **Contextual Responses**: The system maintains conversation history and provides contextually relevant responses
- **Real-time Processing**: Immediate response generation with visual feedback

---

## Architecture Overview

The application implements a modular architecture combining:

- **Frontend Layer**: Streamlit-based user interface
- **Orchestration Layer**: LangChain for workflow management and memory handling
- **Model Layer**: Ollama for local LLM inference
- **Memory Management**: Persistent conversation context within sessions

---

## Configuration Options

The application supports various configuration parameters:

- **Model Selection**: Choose from available Ollama models
- **Response Parameters**: Customize temperature, max tokens, and other generation settings
- **System Behavior**: Define AI personality and response style through system prompts
- **Memory Settings**: Configure conversation buffer size and retention policies

---

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python**: Version 3.9 or higher
- **Memory**: Minimum 8GB RAM (16GB recommended for optimal performance)
- **Storage**: At least 4GB free space for model files
- **Network**: Internet connection for initial model download

---

## Troubleshooting

### Common Issues

- **Model Not Found**: Verify the model name matches the installed Ollama model
- **Connection Error**: Ensure Ollama service is running on the default port
- **Memory Issues**: Consider adjusting conversation buffer size for resource-constrained environments

### Support

For technical support and feature requests, please visit the project repository or submit an issue through GitHub.

---

*This application demonstrates the integration of modern AI technologies to create a robust, locally-hosted conversational AI solution suitable for various professional and educational applications.*    
<img width="1913" height="648" alt="Image" src="https://github.com/user-attachments/assets/93c59b01-9c9b-4cff-b5c2-ad117a97344d" />
