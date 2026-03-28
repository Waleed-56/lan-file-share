#!/usr/bin/env python3
"""
Simple APK builder for LAN File Share using python-for-android
"""
import subprocess
import sys
import os

# Get the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("Building APK for LAN File Share")
print("=" * 60)

# Build APK using p4a directly as module
cmd = [
    sys.executable,
    "-m", "pythonforandroid.toolchain",
    "apk",
    "--private", project_dir,
    "--package", "org.lanfileshare",
    "--name", "LAN File Share",
    "--version", "1.0.0",
    "--bootstrap", "sdl2",
    "--requirements", "python3,kivy,flask,werkzeug,requests,qrcode,pillow",
    "--permission", "INTERNET",
    "--permission", "ACCESS_NETWORK_STATE",
    "--permission", "ACCESS_WIFI_STATE",
    "--orientation", "portrait",
    "--arch", "armeabi-v7a"
]

print("\nRunning command:")
print(" ".join(cmd))
print("\nThis may take several minutes...\n")

try:
    result = subprocess.run(cmd, check=True)
    print("\n" + "=" * 60)
    print("✅ APK build completed successfully!")
    print("=" * 60)
    print("\nAPK file should be in the 'dist' folder")
    sys.exit(0)
except subprocess.CalledProcessError as e:
    print("\n" + "=" * 60)
    print("❌ APK build failed!")
    print("=" * 60)
    print(f"Error code: {e.returncode}")
    sys.exit(1)
except FileNotFoundError:
    print("\n❌ Error: python-for-android not found!")
    print("Make sure python-for-android is properly installed in your environment")
    sys.exit(1)
