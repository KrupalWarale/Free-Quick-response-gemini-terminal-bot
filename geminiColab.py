from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, NoSuchElementException, StaleElementReferenceException
import time
import sys
import os

# For Colab: Suppress logs - This part might not be necessary or can be handled differently in Colab
# log_file = open("selenium_logs.txt", "w", encoding="utf-8")
# sys.stderr = log_file
# try:
#     devnull = open(os.devnull, 'w')
#     os.dup2(devnull.fileno(), 2)
# except:
#     pass

# Initialize Chrome driver with headless options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Use new headless mode for Chrome
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")  # Required for many Linux-based deployments, especially in Colab
options.add_argument("--disable-dev-shm-usage")  # Avoids issues in Docker/Colab
options.add_argument("--window-size=1920,1080") # Added for consistent rendering in headless mode
# Optional: Reuse Chrome profile for persistent login (configure path for deployment)
# options.add_argument("--user-data-dir=/path/to/chrome/profile")

# Colab-specific driver setup
try:
    driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)
except:
    # Fallback for systems where chromedriver might be in a different path or needs manager
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Navigate to Gemini website
driver.get("https://gemini.google.com/app")
WebDriverWait(driver, 7).until(lambda d: d.execute_script("return document.readyState") == "complete")

# Initialize response count
prev_response_count = len(driver.find_elements(By.CSS_SELECTOR, 'div.markdown.markdown-main-panel, message-content.model-response-text'))

# Locate the input field
try:
    input_field = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ql-editor.textarea.new-input-ui[contenteditable="true"][data-placeholder="Ask Gemini"]'))
    )
except TimeoutException:
    input_field = None

def handle_login_popup():
    try:
        close_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Close") or contains(@class, "close") or @data-testid="close-button" or contains(text(), "Close")]'))
        )
        driver.execute_script("arguments[0].click();", close_button)
        return True
    except TimeoutException:
        return False

def get_gemini_response(driver, user_message, prev_response_count):
    try:
        WebDriverWait(driver, 15).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, 'div.markdown.markdown-main-panel, message-content.model-response-text')) > prev_response_count
        )
        response_elements = driver.find_elements(By.CSS_SELECTOR, 'div.markdown.markdown-main-panel, message-content.model-response-text')
        current_response_count = len(response_elements)
        prev_text = ""
        current_text = ""
        timeout = 15
        start_time = time.time()
        max_unchanged_iterations = 2
        unchanged_count = 0

        while time.time() - start_time < timeout:
            try:
                current_text = driver.execute_script("return arguments[0].innerText;", response_elements[-1]).strip()
            except Exception:
                current_text = ""

            if current_text == prev_text and current_text != "":
                unchanged_count += 1
            else:
                unchanged_count = 0
            prev_text = current_text

            if unchanged_count >= max_unchanged_iterations:
                break

            try:
                animating = driver.find_elements(By.CSS_SELECTOR, 'div.markdown.markdown-main-panel[style*="animation"], message-content[style*="animation"]')
                if not animating:
                    break
            except:
                pass

            time.sleep(0.5)

        final_response = current_text if (current_text and user_message not in current_text and "double-check" not in current_text) else ""
        if not final_response:
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.save_screenshot("screenshot.png")
            return "No response captured.", current_response_count

        return final_response, current_response_count
    except TimeoutException:
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        driver.save_screenshot("screenshot.png")
        return "Timeout waiting for response.", prev_response_count

# Send initial prompt
initial_prompt = "behave like a strict text base chatbot , strictly don't use anything which is not text base for you like canvas , code editor etc don't even try to open canvas produce responces in plain text only even if they are code or json or anything"
try:
    if input_field:
        current_text = driver.execute_script("return arguments[0].innerText;", input_field).strip()
        if current_text:
            driver.execute_script("arguments[0].innerText = '';", input_field)
        driver.execute_script("arguments[0].focus();", input_field)
        input_field.click()
        input_field.send_keys(initial_prompt)
        try:
            send_button = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Send") or contains(@class, "send") or contains(text(), "Send") or @data-testid="send-button"]'))
            )
            send_button.click()
        except TimeoutException:
            input_field.send_keys(Keys.ENTER)
        _, prev_response_count = get_gemini_response(driver, initial_prompt, prev_response_count)
except Exception:
    handle_login_popup()
    input_field = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ql-editor.textarea.new-input-ui[contenteditable="true"][data-placeholder="Ask Gemini"]'))
    )
    driver.execute_script("arguments[0].innerText = '';", input_field)
    driver.execute_script("arguments[0].focus();", input_field)
    input_field.click()
    input_field.send_keys(initial_prompt)
    try:
        send_button = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Send") or contains(@class, "send") or contains(text(), "Send") or @data-testid="send-button"]'))
        )
        send_button.click()
    except TimeoutException:
        input_field.send_keys(Keys.ENTER)
    _, prev_response_count = get_gemini_response(driver, initial_prompt, prev_response_count)

# Chatbot loop
try:
    while True:
        print("You: ", end="", flush=True)
        user_message = input().strip()
        if user_message.lower() == 'exit':
            break
          

        try:
            if input_field is None:
                raise NoSuchElementException("Input field not initialized.")
            current_text = driver.execute_script("return arguments[0].innerText;", input_field).strip()
            if current_text:
                driver.execute_script("arguments[0].innerText = '';", input_field)
            driver.execute_script("arguments[0].focus();", input_field)
            input_field.click()
            input_field.send_keys(user_message)
        except (StaleElementReferenceException, NoSuchElementException):
            handle_login_popup()
            input_field = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ql-editor.textarea.new-input-ui[contenteditable="true"][data-placeholder="Ask Gemini"]'))
            )
            driver.execute_script("arguments[0].innerText = '';", input_field)
            driver.execute_script("arguments[0].focus();", input_field)
            input_field.click()
            input_field.send_keys(user_message)
        except ElementClickInterceptedException:
            handle_login_popup()
            driver.execute_script("arguments[0].click();", input_field)
            driver.execute_script("arguments[0].innerText = arguments[1];", input_field, user_message)

        try:
            send_button = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@aria-label, "Send") or contains(@class, "send") or contains(text(), "Send") or @data-testid="send-button"]'))
            )
            send_button.click()
        except TimeoutException:
            input_field.send_keys(Keys.ENTER)

        response, prev_response_count = get_gemini_response(driver, user_message, prev_response_count)
        print(f"Gemini: {response}")

except KeyboardInterrupt:
    pass
finally:
    # For Colab: Log file closing might not be necessary if sys.stderr is not redirected
    # try:
    #     devnull.close()
    # except:
    #     pass
    # sys.stderr = sys.__stderr__
    # log_file.close()
    driver.quit() 