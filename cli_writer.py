"""Writing Assistant designed for use with Apple Silicon."""

import sys
import uuid
import ollama
import pandas as pd
import boto3

def main():
    """
    Uses the pg-editor Ollama model (based on llama3.2:3b) 
    to process and fix text. For specific usage, the script 
    assumes use of `Modelfiles`.

    Command-line Usage:
        - python cli_writer.py "text to fix"

    Interactive Usage:
        - python cli_writer.py
        - Then enter text when prompted.

    Raises:
        Exception: 
        - Error communicating with the Ollama model.
        
    Returns:
        None: Prints the processed text to `stdout` or error message to `stderr`.

    Notes: 
        The model uses a temperature setting of 0.2 for more deterministic output.
    """

    # Check if user provided text as arguments
    if len(sys.argv) > 1:

        # All arguments given
        user_input = ''.join(sys.argv[1:])
    else:
        user_input = input("Text to fix: ")
    if not user_input.strip():
        return

    try:
        response = ollama.chat(
            model="pg-editor",
            messages=[{'role': 'user', 'content': user_input}],
            options={'temperature': 0.3}
        )
        print(response['message']['content'].strip())

        # Extract to local CSV file.
        data = { 'Input': [response['message']['content']], 'Raw_Input': user_input }
        df = pd.DataFrame(data)
        df.to_csv('raw_inputs.csv', mode='a', index=False, header=True)

        print("Data saved to user_inputs.csv")
        print(response['message']['content'])

        # Update Dynamo DB table
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('CLI-Writer')
        random_pk = str(uuid.uuid4())

        table.put_item(
            Item= {
                'writeId': random_pk,
                'raw_input': user_input,
                'ai_response': response['message']['content'],
                })

    except IndexError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
