# Discord Mistral


A simple discord bot made in an afternoon to learn about python and AI.
This bot uses Ollama to run the inference of an LLM (in my case I´m using Mistral 7B, but you could choose any model that runs in Ollama) and redirect the output to discord.


## Getting Started
### Prerequisites

  + Use a linux distro compatible with Ollama.
  + Install [Ollama](https://ollama.ai/download/linux)
  + Pull Mistral from Ollama´s repository

        ollama pull mistral
  + Install the [Langchain](https://python.langchain.com/docs/get_started/introduction) python extension

        pip install langchain

## Installation

  Clone the repository:

    git clone https://github.com/pablodrake/Discord-Mistral.git
    
  Run the bot:

    python3 main.py

## Usage

Invite the bot to your discord server using your invite link and start asking Mistral!
