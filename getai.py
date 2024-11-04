import argparse
import requests
from colorama import init, Fore, Style

# Constants for default values
DEFAULT_MODEL = "llama3"
SERVER_IP = "192.168.0.47"
PORT = 11435

# Initialize colorama
init(autoreset=True)

def send_request(model, query):
    url = f"http://{SERVER_IP}:{PORT}/api/generate"
    payload = {
        "model": model,
        "prompt": query,
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get('response', 'No response received from the server.')
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    parser = argparse.ArgumentParser(description="Communicate with the LLM model on the server.")
    parser.add_argument('-m', '--model', type=str, default=DEFAULT_MODEL, help='Select which model to use.')
    parser.add_argument('-f', '--full', action='store_true', help='Enter full terminal conversation mode.')
    parser.add_argument('query', nargs='?', type=str, help='The query to send to the model.')

    args = parser.parse_args()

    if args.full:
        print(Fore.GREEN + "Entering full conversation mode. Type 'exit' to quit.")
        model = args.model
        while True:
            query = input(Fore.BLUE + "You: " + Style.RESET_ALL)
            if query.lower() == 'exit':
                break
            response = send_request(model, query)
            print(Fore.YELLOW + "Model: " + Style.RESET_ALL + response)
    else:
        if args.query:
            response = send_request(args.model, args.query)
            print(Fore.YELLOW + response + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: A query is required in non-full mode." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
