<div align="center">
  <h1>🌟 Gemini Chatbot Automation Script</h1>
</div>
<br>


<div align="center">
<img src="https://github.com/user-attachments/assets/d5b58937-1513-4936-959c-aa88366e2360" alt="Gemini Chatbot Demo" width="600" />
</div>


<br>
<br>


## 🎯 The Problem statment
<br
Accessing powerful AI models like Gemini often involves reliance on API keys, especially for integration into custom applications. However, free-tier API keys frequently come with significant limitations, including restrictive rate limits, slower response times, and potential costs for higher usage. This creates a barrier for developers and hobbyists looking to leverage advanced AI capabilities in their projects without incurring expenses or compromising on performance.
  
<br>
This Python script automates interactions with the Google Gemini web interface using Selenium. It can send prompts and retrieve responses, simulating a text-based chatbot experience.
<br>
<br>
🚀 Why Use This Script?
This method offers significant advantages over free-tier Gemini API keys:

⚡ Blazing Fast Responses: Experience near real-time interactions! While free API keys can often take a fraction of a minute to generate responses, this script delivers responses in mere seconds by directly leveraging the optimized web interface.

🚫 No Rate Limits: Unlike API keys with strict rate limits, this web-scraping approach bypasses such restrictions, allowing for more frequent and extensive use in your projects.

🔗 Backend Integration Ready: This script is ideal for integrating Gemini's capabilities into your backend projects, providing a powerful and free solution for automated text generation, content creation, or intelligent conversational agents.
<br>

🛠️ Crucial Initial Prompt
The script includes a critical initial prompt to ensure a seamless text-based experience:
<br>

```
behave like a strict text base chatbot , strictly don't use anything which is not text base for you like canvas , code editor etc don't even try to open canvas produce responces in plain text only even if they are code or json or anything
```
This prompt is essential because it instructs Gemini to respond purely in text. Without it, Gemini might attempt to use UI elements like "canvas" or "code editor," which can trigger a sign-out pop-up and lead to the loss of your conversation.

You can modify this prompt by keeping the base text and adding more specific instructions to guide the bot's behavior.

⚠ Note: This script relies on web scraping techniques and may cease to function if the Gemini web interface undergoes significant changes. Its continued functionality is not guaranteed.
<br>
✨ Features
- Automates sending messages to Gemini.
- Captures and displays Gemini's responses.
- Handles potential login pop-ups.
- Runs in headless mode (no browser UI visible).
<br>
📦 Prerequisites
Before running the script, ensure you have Python installed.
<br>
⚙️ Installation
1. Clone the repository or download the script files (geminiBot.py, geminiColab.py).

2. Install the required Python packages:

```bash
pip install selenium webdriver-manager
```
<br>
💻 How to Run
### Local Execution (`geminiBot.py`)
1. Run the script from your terminal:

```bash
python geminiBot.py
```
The script will open a headless Chrome browser, navigate to Gemini, send the initial prompt, and then enter a loop where you can type messages and receive responses.

2. Type `exit` and press Enter to quit the chatbot.
<br>
### Google Colab Execution (`geminiColab.py`)
This script is adapted for use in Google Colab.

1. Upload `geminiColab.py` to your Colab notebook environment.

2. Install dependencies in a Colab cell:

```python
!pip install selenium webdriver-manager
```

3. Run the script from a Colab cell:

```python
%run geminiColab.py
```
💡 For interactive use, you can copy the contents of `geminiColab.py` directly into a Colab cell and execute it.

⚠ Note: The Colab file is under construction and may not work correctly.
<br>

<div align="center">
<img src="https://github.com/user-attachments/assets/580cbf32-688f-4a3e-bdc3-6cebf437353d" alt="Example of Gemini chatbot in action" width="800" />
</div>
<br>
<br>

🛠️ Troubleshooting
- `selenium_logs.txt`: Contains logs from Selenium for debugging.
- `page_source.html` & `screenshot.png`: Generated if a response isn't captured, showing the page’s HTML source and a screenshot for troubleshooting.
- Element Not Found/Clickable: The Gemini UI may change, causing CSS selectors/XPaths to break. Update them in `geminiBot.py` or `geminiColab.py` (e.g., `div.ql-editor`, `button[aria-label="Send"]`). 








