"""Writing Assistant designed for use with Apple Silicon."""

import sys
import ollama

def main():
    """
    Uses the 'pg-editor' Ollama model (based on qwen2.5:3b) to process and fix text.
    For specific usage, the script assumes use of modelfiles.

    Command-line Usage:
        python cli_writer.py "text to fix"
        
    Interactive Usage:
        python cli_writer.py
        Then enter text when prompted.

    Raises:
        Exception: If there's an error communicating with the Ollama model.
        
    Returns:
        None: Prints the processed text to stdout or error message to stderr.

    Notes: 
        The model uses a temperature setting of 0.3 for more deterministic output.
    """

    # Check if user provided text as arguments
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
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
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
