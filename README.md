# tiny-local-ai-demo
A tiny demo for laptop-hosted AI.

### 1. Create a Hugging Face Account

You will need an account to download the model file.
*   Go to [huggingface.co](https://huggingface.co/) and sign up for a free account.

### 2. Download the Language Model

We are using a quantized, 4GB version of Code Llama 7B. You only need to do this once.

*   **Model Link:** [TheBloke/CodeLlama-7B-Instruct-GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF)
*   **File to Download:** `codellama-7b-instruct.Q4_K_M.gguf`

You can download it in one of three ways. Pick the one you are most comfortable with:

*   **(Option A: Browser)** Go to the "Files and versions" tab on the model link above, find the correct filename, and click the download icon to the right.
*   **(Option B: `curl`)** Open your terminal and run this command:
    ```bash
    curl -L "https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_M.gguf?download=true" -o "codellama-7b-instruct.Q4_K_M.gguf"
    ```
*   **(Option C: `wget`)** Open your terminal and run this command:
    ```bash
    wget -O codellama-7b-instruct.Q4_K_M.gguf "https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF/resolve/main/codellama-7b-instruct.Q4_K_M.gguf?download=true"
    ```

**IMPORTANT:** After downloading, ensure the model file (`codellama-7b-instruct.Q4_K_M.gguf`) is in the same directory as the `main.py` script.

### 3. Set Up Python Environment

It is highly recommended to use a virtual environment.

```bash
python3 -m venv llama

# macOS / Linux:
source llama/bin/activate
# Windows:
source llama/Scripts/activate

# 3. Install the required library
pip install llama-cpp-python flask
```

### 4. Usage: Generate a "Hello, World!" Script

Run the script from your terminal, providing the prompt and an output filename.

```bash
python3 main.py "create a simple python script that prints hello world" -o hello.py
```

This will generate a file named hello.py. You can inspect it with cat hello.py and run it with python hello.py.

### 5. Example: Generate a Flask Web Server

```bash
python3 main.py "Create a simple web server using Flask that has one route '/' which returns a JSON object {'status': 'ok'}. The server should run on port 8080." -o app.py
```

```bash
python3 app.py
```

Open a new terminal to test the server:
```bash
curl http://127.0.0.1:8080
```

### 6. Explore and have fun!
Try benchmarking different models for your machine, or exploring different models for different tasks on hugging face.

