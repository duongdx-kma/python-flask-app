from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('APP_PORT', 5000))  # Default to port 8000 if not set

    app.run(host='0.0.0.0', port=port, debug=True)
