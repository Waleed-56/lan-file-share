# Import necessary modules from Flask for web app functionality
from flask import Flask, render_template, request, send_from_directory, redirect, url_for 
# Import os for file system operations
import os
from datetime import datetime, timezone
import qrcode
from flask import session
import socket


# Initialize the Flask application with the current module name
app = Flask(__name__)
# Set the secret key for session management, using an environment variable or a default value
app.secret_key = os.environ.get('SECRET_KEY', 'devsecret')

# Get the base directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Join the base directory with 'uploads' to create the upload folder path
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
# Create the uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Create static directory if it doesn't exist
STATIC_FOLDER = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_FOLDER, exist_ok=True)

# Decorator to define the route for "/login" accepting GET and POST methods
@app.route("/login", methods=["GET", "POST"])
def login():
    # Handle login logic
    if request.method == "POST":
        username = request.form.get("username") or "admin"
        password = request.form.get("password")

        # Debug logging for mobile login issues
        print(f"Login attempt from {request.remote_addr}: username={username!r}, password={password!r}")

        # Allow either username+password or just password on mobile
        if (username == "admin" and password == "password") or (password == "password"):
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            # Keep user on login page with message
            return render_template("login.html", error="Invalid credentials. Use admin/password")
    return render_template("login.html")

# Function to get the local IP address of the machine
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a remote address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:  # If there's an error (e.g., no network), default to localhost
        ip = "127.0.0.1"
    finally:  # Close the socket after getting the IP address
        s.close()
    return ip

# Function to generate QR code on app startup
def generate_qr_code():
    try:
        # Get the local IP address of the machine
        local_ip = get_ip_address()
        # Create a QR code with the local IP address and port
        qr_data = f"http://{local_ip}:5000"
        qr = qrcode.make(qr_data)
        # Save the QR code image to static folder
        qr_path = os.path.join(STATIC_FOLDER, "qr_code.png")
        qr.save(qr_path)
        print(f"QR code generated: {qr_data}")
    except Exception as e:
        print(f"Error generating QR code: {e}")

# Generate QR code when app starts
generate_qr_code()

# Decorator to define the route for the root URL "/"
@app.route("/")
def index():
    # Verify user login
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    # List to hold data about uploaded files
    files_data = []
    # Iterate through files in the upload folder
    for filename in os.listdir(UPLOAD_FOLDER):
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        # Check if the path is a file (not a directory)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)  # size in bytes
            upload_time = os.path.getmtime(filepath)  # upload time in seconds since epoch
            # Format the time to human-readable format
            formatted_time = datetime.fromtimestamp(upload_time).strftime('%b %d, %I:%M %p')
            # Append the file data to the list with name, size in KB, and upload time
            files_data.append({
                "name": filename,
                "size": round(size / 1024, 2),  # KB
                "time": formatted_time
            })

    # Get local IP address for display and QR-code reference
    ip = get_ip_address()
    return render_template("index.html", files=files_data, ip=ip)

# Decorator to define the route for "/upload" accepting POST methods
@app.route("/upload", methods=["POST"])
# Function to handle file uploads
def upload():
    # Get the uploaded file from the request
    file = request.files.get('file')

    # Check if no file was selected or filename is empty
    if file is None or file.filename == '':
        # Return error message with 400 status
        return "No file selected", 400

    # Create the full filepath for saving the file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    # Save the file to the uploads folder
    file.save(filepath)

    # Redirect back to the index page to show updated file list
    return redirect(url_for('index'))

# Decorator to define the route for downloading files with filename parameter
@app.route('/download/<filename>')
# Function to handle file downloads
def download(filename):
    # Print the filename being downloaded (for debugging)
    print("Downloading:", filename)
    # Send the file from the uploads folder as an attachment
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# Decorator to define the route for deleting files with filename parameter, accepting POST methods
@app.route("/delete/<filename>", methods=["POST"])
def delete(filename):
    # Create the full filepath for the file to be deleted
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    # Check if the file exists before attempting to delete it
    if os.path.isfile(filepath):
        os.remove(filepath)
    # Redirect back to the index page
    return redirect(url_for('index'))

# Comment for running the app
#Run the app
# Check if this script is run directly (not imported)
if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(host="0.0.0.0", port=5000)