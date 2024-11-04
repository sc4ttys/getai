## What is this? 
I wanted a way to quickly interact with my locally hosted LLMs from my command line. 
This lets me either send quick single queries, or open a conversation mode. 


## Operation modes
1. Single Query Mode

	This is the default mode. 

	The usage is 'getai "your query"', e.g. '"getai why is the sky blue?"' 

	Optional argument is -m or --model, to specify which model to use. 

2. Conversation mode 

	Full screen back-and-forth conversation mode. 

	Activated with 'getai -f' or --full. 

	Provides chat-like interface but queries will not be linked together. 


## Set up 
Fork this.

Change the variables on lines 6-8:

	DEFAULT_MODEL = <your preferred default model> 

	SERVER_IP = <your ollama server ip>

	PORT = <your port>


Make sure to have argparse, requests and colorama installed. 

Optionally add it to your path so you can call it from anywhere. 
