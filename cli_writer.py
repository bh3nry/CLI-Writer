"""Writing Assistant designed for use with Apple Silicon."""

import sys
import uuid
import time
import ollama
import pandas as pd
import boto3

def write_question(decision: str) -> None:
    """
    Small decision flow function to control DB writes.
    """
    answer_options = { 'yes': 'y', 'no': 'n' }
    if decision != answer_options.get('yes'):
        sys.exit(1)
    print("Initiating DB write...")
    time.sleep(3)


def cli_input(text_input: str) -> str:
    """
    Parses raw user input from the command line.

    Args:
        text_input (str): raw user input.
    """
    if len(sys.argv) > 1:
        # All arguments given
        text_input = ' '.join(sys.argv[1:])
    elif not text_input.strip():
        text_input = input("Enter text to edit: ")
    if not text_input.strip():
        return None
    return text_input

def model_output(user_input: str) -> str:
    """
    Interprets text inputs from the user, and returns 
    a string representation of the models' response.

    Args: 
        user_input (str): user input.
    """
    response = ollama.chat(
        model="clean-grammar",
        messages=[{'role': 'user', 'content': user_input}],
        options={'temperature': 0.0}
    )
    return response['message']['content'].strip()

def write_to_csv(user_input: str, model_response: str) -> None:
    """
    Writes raw un-edited user inputs and model responses to a local
    CSV file with pandas.

    Args:
        user_input (str): raw user input.
        model_response (str): generated ai output.
    """
    data = { "raw_input": user_input, "refined_text": [model_response] }
    df = pd.DataFrame(data)
    df.to_csv('raw_inputs.csv', mode='a', index=False, header=True)
    print("Saved to CSV.")

def write_to_db(user_input: str, model_response: str) -> None:
    """
    Updated the database with raw user inputs, as well as outputted
    text respones from the model.

    Args:
        user_input (str): raw user input.
        model_response (str): generated ai output.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CLI-Writer')
    random_pk = str(uuid.uuid4())

    table.put_item(
        Item= {
            'writeId': random_pk,
            'raw_input': user_input,
            'ai_response': model_response,
            })
    print("Saved to DynamoDB.")

def main():
    """
    Input text that requires ammendments directly from 
    the command line. Review outputted text from the selected
    model pulled from Ollama/Hugging-Face.
    """

    USER_PROMPT=""
    text_to_edit = cli_input(USER_PROMPT)

    if not text_to_edit:
        print("Error: No input has been provided.")
        sys.exit(1)

    # Model Output
    new_response = model_output(text_to_edit)
    print(new_response)

    # Optional Write to CSV/AWS-db
    decision = input("Save to DynamoDB and CSV? [y/n] ")
    write_question(decision)

    write_to_csv(text_to_edit, new_response)
    write_to_db(text_to_edit, new_response)

if __name__ == "__main__":
    main()
