# LAN File Share

A mobile-optimized web and Android application for sharing files over your local network.

## Features

✨ **Web Interface**
- Upload and download files
- Real-time file listing
- Mobile-responsive design
- Dark/Light theme toggle
- Customizable UI colors

📱 **Mobile App (Kivy)**
- Native Android integration
- Runs Flask server in background
- PWA support
- Auto-detect local IP address
- QR code for easy sharing

🔒 **Security**
- Session-based authentication
- Local network only
- Simple password protection

## Quick Start

### Web Application
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Access at: http://localhost:5000
# Login with: admin / password
```

### Android Application
```bash
# Install dependencies
pip install -r requirements.txt
pip install kivy

# Run with Kivy
python main.py
```

## Building APK

### Option 1: GitHub Actions (Automatic)
1. Fork this repository
2. Go to Settings → Secrets and add `GITHUB_TOKEN`
3. Push to trigger automatic build
4. Download APK from Actions artifacts

### Option 2: Local Build with Buildozer
```bash
# Install buildozer
pip install buildozer cython

# Build APK
buildozer android debug

# APK will be in bin/ directory
```

### Option 3: Upload to GitHub

```bash
# Follow the instructions below to push to GitHub
```

## GitHub Setup Instructions

### 1. Create a GitHub Repository

Go to [github.com/new](https://github.com/new) and create a new repository named `lan-file-share` (or your preferred name).

**Do NOT initialize with README, .gitignore, or license** - we'll push existing files.

### 2. Add Remote and Push

Replace `YOUR_USERNAME` with your GitHub username:

```bash
# From the project directory
cd C:\Users\SiliCon\Pictures\somewhat

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/lan-file-share.git

# Rename branch to main
git branch -m master main

# Push to GitHub
git push -u origin main
```

### 3. Set Up GitHub Actions

The workflow in `.github/workflows/build.yml` will automatically:
- Build the APK on every push
- Store APK as artifact
- Create releases with APK attached

### 4. Download APK from GitHub

After push:
1. Go to your repository
2. Click "Actions" tab
3. Click the latest workflow run
4. Download "apk-debug" artifact
5. Extract and install on Android device

## Authentication

Default credentials:
- Username: `admin`
- Password: `password`

Change in `app.py`:
```python
if (username == "admin" and password == "password"):
```

## File Structure

```
.
├── app.py              # Flask backend
├── main.py             # Kivy app entry point
├── requirements.txt    # Python dependencies
├── buildozer.spec      # APK build config
├── templates/          # HTML templates
│   ├── login.html
│   ├── index.html
│   └── base.html
├── static/             # CSS, JS, assets
│   ├── style.css
│   ├── sw.js          # Service Worker
│   ├── manifest.json  # PWA manifest
│   └── qr_code.png
└── uploads/           # File storage

```

## Technologies

- **Backend**: Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Mobile**: Kivy, Python-for-Android
- **Build**: Buildozer, GitHub Actions
- **Web App Features**: PWA, Service Worker

## Permissions

Android permissions requested:
- `INTERNET` - Network access
- `ACCESS_NETWORK_STATE` - Check network connection
- `ACCESS_WIFI_STATE` - Detect WiFi

## Configuration

### Port
Default: 5000 (change in `app.py` and `buildozer.spec`)

### QR Code
Automatically generated at startup. Shows your local IP address.

### Color Customization
Users can customize colors via the web UI. Colors persist in browser localStorage.

## Troubleshooting

### APK won't install
- Ensure device has Android 5.0+ (API 21+)
- Enable "Unknown Sources" in security settings
- Check storage space (50MB minimum)

### Connection refused
- Check both devices are on same WiFi network
- Verify firewall isn't blocking port 5000
- Check QR code IP address

### Files won't upload
- Check `uploads/` folder permissions
- Ensure sufficient disk space
- Check browser file upload limits

## Development

### Requirements
- Python 3.8+
- Kivy 2.0+
- Flask 2.0+
- Buildozer (for APK builds)

### Adding Features

1. **Backend** (Flask):
   - Edit `app.py`
   - Modify routes and logic

2. **Frontend** (Web):
   - Edit templates in `templates/`
   - Modify styles in `static/style.css`
   - Add scripts to template files

3. **Mobile** (Kivy):
   - Edit `main.py`
   - Add Kivy widgets as needed

## License

MIT License - Feel free to use for personal and commercial projects.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review existing GitHub issues
3. Create a new issue with details

## Future Enhancements

- [ ] User management system
- [ ] File preview directly in browser
- [ ] Download multiple files as ZIP
- [ ] WebRTC for P2P transfer
- [ ] End-to-end encryption
- [ ] File versioning
- [ ] Drag-and-drop upload

---

**Made with ❤️ for easy local file sharing**
