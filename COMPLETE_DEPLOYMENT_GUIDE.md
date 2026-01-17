# LyricFlow - Complete Deployment Guide

## ✅ DEPLOYED COMPONENTS

### Frontend (LIVE)
- **URL**: https://24211a6657-sys.github.io/LyricFlow/
- **Status**: ✅ Fully Deployed and Working
- **Platform**: GitHub Pages
- **Features**: Upload audio/video, text overlay, style selection, video preview

### Backend Status
- **Repository**: https://github.com/24211a6657-sys/LyricFlow
- **Code**: ✅ Complete and Ready
- **Platform Tested**: Render (MoviePy build limitations on free tier)

---

## 🚀 COMPLETE BACKEND DEPLOYMENT OPTIONS

### Option 1: PythonAnywhere (RECOMMENDED - Free & Easy)

#### Step-by-Step Deployment:

1. **Create Account**
   - Go to: https://www.pythonanywhere.com/registration/register/beginner/
   - Fill in Username, Email, Password
   - Check the "I agree to Terms" checkbox
   - Click blue "Register" button

2. **Upload Backend Code**
   - After login, click "Files" tab (top navigation bar)
   - Click "Upload a file" button (right side)
   - Upload `main.py` from: https://github.com/24211a6657-sys/LyricFlow/blob/main/backend/main.py
   - Upload `requirements.txt` from: https://github.com/24211a6657-sys/LyricFlow/blob/main/backend/requirements.txt

3. **Install Dependencies**
   - Click "Consoles" tab (top navigation)
   - Click "Bash" under "Start a new console"
   - Type: `pip3 install --user -r requirements.txt`
   - Press Enter and wait for installation

4. **Configure Web App**
   - Click "Web" tab (top navigation)
   - Click "Add a new web app" button
   - Click "Next" on the domain name page
   - Select "Flask" framework
   - Select Python 3.10
   - Click "Next" through configuration

5. **Set Up WSGI File**
   - In Web tab, find "WSGI configuration file" link
   - Click the link to edit
   - Replace ALL content with:
   ```python
   import sys
   path = '/home/YOUR_USERNAME'
   if path not in sys.path:
       sys.path.append(path)
   
   from main import app as application
   ```
   - Replace YOUR_USERNAME with your PythonAnywhere username
   - Click "Save" (top right)

6. **Enable CORS and Start**
   - Go back to "Web" tab
   - Click green "Reload" button
   - Your backend URL will be: `https://YOUR_USERNAME.pythonanywhere.com`

7. **Update Frontend**
   - Update the API URL in `index.html` at line 15
   - Change: `const API_URL = 'https://YOUR_USERNAME.pythonanywhere.com';`

---

### Option 2: Replit (Interactive & Fast)

#### Step-by-Step:

1. **Import Repository**
   - Go to: https://replit.com/
   - Click "Create Repl" button (top right)
   - Select "Import from GitHub"
   - Paste: `https://github.com/24211a6657-sys/LyricFlow`
   - Click "Import from GitHub"

2. **Configure**
   - In file tree, open `backend/main.py`
   - Click "Run" button at top
   - Replit will auto-install dependencies

3. **Get Backend URL**
   - After running, look for URL in console
   - Format: `https://lyricflow.YOUR_USERNAME.repl.co`
   - Copy this URL

4. **Update Frontend**
   - Update API_URL in index.html with your Replit URL

---

### Option 3: Local Deployment (For Testing)

#### Step-by-Step:

1. **Install Python**
   - Download Python 3.10+ from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"
   - Click "Install Now"

2. **Download Backend Code**
   - Go to: https://github.com/24211a6657-sys/LyricFlow
   - Click green "Code" button
   - Click "Download ZIP"
   - Extract ZIP file to a folder

3. **Install Dependencies**
   - Open Command Prompt (Windows) or Terminal (Mac/Linux)
   - Navigate to backend folder: `cd path/to/LyricFlow/backend`
   - Run: `pip install -r requirements.txt`
   - Wait for installation to complete

4. **Run Backend**
   - In same terminal, run: `python main.py`
   - Backend will start at: `http://localhost:8000`

5. **Update Frontend for Local Testing**
   - Open `index.html` in text editor
   - Change API_URL to: `http://localhost:8000`
   - Open `index.html` in browser

---

## 📋 WHAT'S INCLUDED

### Frontend Features (Already Live):
- ✅ Audio/Video file upload
- ✅ Text input for lyrics/captions
- ✅ Style selection (Bold, Italic, Outlined, Shadow)
- ✅ Font family selection
- ✅ Font size control (20-100px)
- ✅ Color picker for text
- ✅ Position selection (Top, Center, Bottom)
- ✅ Generate button
- ✅ Video preview player
- ✅ Download button
- ✅ Responsive design

### Backend Features (Code Ready):
- ✅ FastAPI server
- ✅ Video processing with MoviePy
- ✅ Text overlay with custom styles
- ✅ Multiple font support
- ✅ CORS enabled for frontend
- ✅ File upload handling
- ✅ Temporary file management

---

## 🎯 QUICK START (Frontend Only)

Your frontend is already working at:
**https://24211a6657-sys.github.io/LyricFlow/**

To test it:
1. Click the URL above
2. Upload a video file
3. Enter some text
4. Choose a style
5. Click "Generate Lyrical Video"

Note: Backend processing requires deployment (see options above)

---

## 📦 TECH STACK

### Frontend:
- HTML5
- CSS3 (Responsive Design)
- Vanilla JavaScript
- GitHub Pages Hosting

### Backend:
- FastAPI (Python)
- MoviePy (Video Processing)
- PIL/Pillow (Image Processing)
- uvicorn (ASGI Server)

---

## 🔧 TROUBLESHOOTING

### Backend Won't Start:
1. Check Python version: `python --version` (need 3.10+)
2. Reinstall dependencies: `pip install -r requirements.txt --upgrade`
3. Check port availability: Try changing port in main.py

### Video Processing Errors:
1. Ensure FFmpeg is installed (required by MoviePy)
2. Check file format (MP4, MOV, AVI supported)
3. Check file size (free tiers have limits)

### Frontend Not Connecting:
1. Verify backend URL is correct in index.html
2. Check CORS is enabled in backend
3. Ensure backend is running and accessible

---

## 🎉 SUCCESS METRICS

✅ Repository Created: https://github.com/24211a6657-sys/LyricFlow
✅ Frontend Deployed: https://24211a6657-sys.github.io/LyricFlow/
✅ Backend Code Complete: Ready for deployment
✅ Documentation: Complete guides provided
✅ Free Platforms: PythonAnywhere, Replit, Local options
✅ Step-by-Step: Detailed click-by-click instructions

---

## 📞 NEXT STEPS

1. Choose a backend deployment option above
2. Follow the step-by-step guide
3. Update frontend with backend URL
4. Test the complete application
5. Share with users!

**Frontend is LIVE NOW** - Backend deployment takes 10-15 minutes following any option above.
