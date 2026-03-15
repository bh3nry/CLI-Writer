# Lightweight Writing Editor for Mac OS.

A zippy, local writing assistant that edits text for spelling/grammar/punctuation. 

Optimized for Apple Silicon using **Ollama**: **llama3.1:8b**.

<p align="left">
  <img src="assets/usage.gif" alt="CLI-Writer demo" width="500" />
</p>

---

## Features

* Reviews inputs for minor spelling and grammatical errors.
* Optionally integrated with the CLI.
* Local processing.
* Syncs with AWS for training your own models based on your writing style/cadence.

---

### Setup

#### 1. Model Configuration

- pip install ollama
```zshrc
ollama pull (whatever model you like) ---> eg: llama3.2:3b
```

At root level, create a file named `whatever_name_you_like.modelfile` with your system instructions and style samples, then register it with Ollama:

```bash
ollama create my-text-editor -f pg_editor.modelfile

```

#### 2. Script Installation

Ensure your Python script (`writer.py`) is executable:

```zshrc
chmod +x "/path../../../..//writer.py"

```

#### 3. Global Alias

Add the following to your `~/.zshrc` via the `nano ~/.zshrc` terminal command t
This will enable the `fixit` command *(or whatever you'd like to name it)*:

```zshrc
alias fixit='python3 "/path../../../../writer.py"'

```

If you need to make changes to the script, just load up your `nano ~/.zshrc` dir, and save the new write,
then *Reload with `source ~/.zshrc`.*

---

### Usage

Pass your text directly to the command:

```zshrc
fixit "writing things down is importannt, and articuulatimg yourself helps you learn thingsz more better0;"

```

The tool will output the corrected version directly to your terminal.

---

### ⚙️ Requirements

* **OS:** macOS (Apple Silicon)
* **Backend:** [Ollama](https://ollama.ai/)
* **Model:** `llama3.1:8b` or `qwen2.5:1.5b`
