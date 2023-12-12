import concurrent.futures
from langchain.llms import Ollama


mistral = Ollama(base_url='http://localhost:11434', model='mistral')


def handle_response(message) -> str:
    p_message = message.lower()
    words = p_message.split()
    if words[0] == "!mistral":
        prompt = " ".join(words[1:])
        with concurrent.futures.ProcessPoolExecutor() as executor:
            future = executor.submit(mistral, prompt)
            result = future.result()
            return result
    else:
        return 'If you want to talk to the AI write a message that starts with "!mistral" followed by a blank space'
