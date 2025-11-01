import subprocess
import sys
import os

def run_fastapi_server():
    try:
        # Define the command to run the FastAPI server
        command = [
            sys.executable,  # Use current Python interpreter
            "-m", "uvicorn",  # Run uvicorn as a module
            "main:app",       # FastAPI app path (filename:app_variable)
            "--reload",       # Enable hot reload
            "--host", "0.0.0.0",  # Listen on all network interfaces
            "--port", "8000"      # Port number
        ]

        # Run the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Stream output in real-time
        for line in process.stdout:
            print(line.decode().strip())

    except KeyboardInterrupt:
        print("\n Server stopped by user.")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    # Ensure uvicorn is installed
    try:
        __import__("uvicorn")
    except ImportError:
        print("⚙️ Installing uvicorn...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn"])

    run_fastapi_server()
