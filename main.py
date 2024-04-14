from openai import OpenAI
import os
import subprocess
import json

# Load API key from a file and set it as an environment variable
with open('/etc/api-keys.json') as f:
    data = json.load(f)
    os.environ['OPENAI_API_KEY'] = data['OPENAI_API_KEY']
    
client = OpenAI()

if __name__ == "__main__":
    subprocess.run("figlet -f slant 'OpenAI Chat'", shell=True)
    print('Type "exit" to quit the program.')
    while True:
        usr_input = input('\n\nSay Something: ')
        if usr_input.lower() == "exit":
            print("Exiting...")
            break
        
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": usr_input}],
            stream=True,
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")

