2. **Install Dependencies:**
   You need to install the required Python libraries.
*(Note: I added `python-dotenv` to the instructions, so you should ideally add it to `requirements.txt`.)*
 
3. **Configure (Optional):**
   Create a `.env` file by copying the example:
4. **Run the Application:**
   Execute the main Python file:
The application will prompt you for a username and password. **Any input provided will be written immediately to `stolen_credentials.txt`** in the root directory.
 
## ️ Project Components
* **`src/main.py`:** Entry point.
* **`src/auth_service.py`:** Handles user interaction and capture of login data.
* **`src/logger.py`:** The "malware" component; responsible for persistent storage of the captured data.
* **`requirements.txt`:** Lists necessary libraries.
# Set the path where stolen credentials will be saved
LOG_FILE_PATH=stolen_credentials.txt
# Optional: API key if we were connecting to a real Instagram API
INSTAGRAM_API_KEY=YOUR_API_KEY_HERE
