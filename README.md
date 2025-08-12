                                                                                           🌟 Gemini Chatbot Automation Script
<img width="2096" height="1182" alt="image" src="https://github.com/user-attachments/assets/580cbf32-688f-4a3e-bdc3-6cebf437353d" />

This Python script automates interactions with the Google Gemini web interface using Selenium.
It can send prompts to Gemini and retrieve responses, simulating a text-based chatbot experience.

This method offers significant advantages, especially when compared to free-tier Gemini API keys:

⚡ Blazing Fast Responses: Experience near real-time interactions! While free API keys can often take a fraction of a minute to generate responses, this script delivers responses in mere seconds by directly leveraging the optimized web interface.

🚫 No Rate Limits: Unlike API keys that come with strict rate limits, this web-scraping approach bypasses such restrictions, allowing for more frequent and extensive use in your projects.

🔗 Backend Integration Ready: This script is ideal for integrating Gemini's capabilities into your backend projects, providing a powerful and free solution for automated text generation, content creation, or intelligent conversational agents.

🛠 Crucial Initial Prompt for Seamless Experience
The script includes an initial prompt:

```
behave like a strict text base chatbot , strictly don't use anything which is not text base for you like canvas , code editor etc don't even try to open canvas produce responces in plain text only even if they are code or json or anything
```
This prompt is essential as it instructs Gemini to respond purely in text.
Without it, Gemini might attempt to use UI elements like "canvas" or "code editor," which can trigger a sign-out pop-up and lead to the loss of your entire conversation thread.

You can still modify the prompt by keeping this base text and adding more instructions to make the bot behave in a certain way — it currently behaves like a chatbot.

⚠ Note: This script relies on web scraping techniques and may cease to function if the Gemini web interface undergoes significant changes. It is provided "as-is" and its continued functionality is not guaranteed.

✨ Features
- Automates sending messages to Gemini.
- Captures and displays Gemini's responses.
- Handles potential login pop-ups.
- Runs in headless mode (no browser UI visible).

📦 Prerequisites
Before running the script, ensure you have Python installed.

⚙️ Installation
1. Clone the repository or download the script files (`geminiBot.py`, `geminiColab.py`).

2. Install the required Python packages:

```bash
pip install selenium webdriver-manager
```

💻 How to Run
### Local Execution (`geminiBot.py`)
1. Run the script from your terminal:

```bash
python geminiBot.py
```
The script will open a headless Chrome browser, navigate to Gemini, send an initial prompt, and then enter a loop where you can type messages and receive responses.

2. Type `exit` and press Enter to quit the chatbot.

### Google Colab Execution (`geminiColab.py`)
This script (`geminiColab.py`) is adapted for use in Google Colab environments. Here's how to use it:

1. Upload `geminiColab.py` to your Colab notebook environment.

2. Install Dependencies in a Colab cell:

```python
!pip install selenium webdriver-manager
```

3. Run the script from a Colab cell:

```python
%run geminiColab.py
```
💡 For interactive use within a cell, you can copy the contents of `geminiColab.py` directly into a cell and execute it.

⚠ Note: The Colab file is under construction and may not work correctly.

🛠 Troubleshooting
- `selenium_logs.txt` – Contains logs from Selenium for debugging issues.
- `page_source.html` & `screenshot.png` – Generated if a response isn't captured, showing the page’s HTML source and a screenshot for troubleshooting.
- Element Not Found/Clickable – The Gemini UI may change, causing CSS selectors/XPaths to break. Update them in `geminiBot.py` or `geminiColab.py` (e.g., `div.ql-editor`, `button[aria-label="Send"]`).

<img src="https://images.unsplash.com/photo-1518770660439-4636190af524?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Footer Banner" width="100%"> 

