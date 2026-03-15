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

Create a file named `whatever_name_you_like.modelfile` with your system instructions and style samples, then register it with Ollama:

```bash
ollama create my-text-editor -f pg_editor.modelfile

```

#### 2. Script Installation

Ensure your Python script (`writer.py`) is executable:

```bash
chmod +x "/path../../../..//writer.py"

```

#### 3. Global Alias

Add the following to your `~/.zshrc` to enable the `fixit` command *(or whatever you'd like to name it)*:

```bash
alias fixit='python3 "/path../../../../writer.py"'

```

If you need to make changes to the script, just load up your `nano ~/.zshrc` dir, and save the new write,
then *Reload with `source ~/.zshrc`.*

---

### Usage

Pass your text directly to the command:

```bash
fixit "writing things down is importannt, and articuulatimg yourself helps you learn thingsz more better0;"

```

The tool will output the corrected version directly to your terminal.

---

### ⚙️ Requirements

* **OS:** macOS (Apple Silicon)
* **Backend:** [Ollama](https://ollama.ai/)
* **Model:** `qwen2.5:3b` or `qwen2.5:1.5b`
