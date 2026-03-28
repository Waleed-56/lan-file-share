from kivy.app import App
from kivy.uix.label import Label
import threading
from app import app as flask_app

# Function to run the Flask server in a separate thread
def run_server():
    flask_app.run(host="0.0.0.0", port=5000)

# Main Kivy application class
class MainApp(App):
    def build(self):
        # Start the Flask server in a separate thread
        threading.Thread(target=run_server, daemon=True).start()
        # Return a simple label for the Kivy app (you can customize this)
        return Label(text="LAN File Share is running...")

#  Check if this script is run directly (not imported)
if __name__ == "__main__":
    MainApp().run()