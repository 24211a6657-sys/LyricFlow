# 🚀 LyricFlow Deployment Guide

## Quick Deploy (15 minutes)

### Backend on Render

1. **Go to** [render.com](https://render.com)
2. **Sign in** with GitHub
3. **Click** "New" → "Web Service"
4. **Select** this repository (`LyricFlow`)
5. **Configure:**
   - Name: `lyricflow-api`
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Add Environment Variables:**
   ```
   ENVIRONMENT=production
   UPLOAD_DIR=/tmp/uploads
   OUTPUT_DIR=/tmp/outputs
   ALLOW_ORIGINS=*
   ```
7. **Click** "Create Web Service"
8. **Wait** 3-5 minutes for deployment
9. **Copy** your backend URL (e.g., `https://lyricflow-api.onrender.com`)

### Frontend on Vercel

1. **Go to** [vercel.com](https://vercel.com)
2. **Sign in** with GitHub
3. **Click** "Add New" → "Project"
4. **Select** this repository (`LyricFlow`)
5. **Configure:**
   - Framework: Next.js
   - Root Directory: `frontend` (if using separate folder)
6. **Add Environment Variable:**
   ```
   NEXT_PUBLIC_API_URL=https://lyricflow-api.onrender.com
   ```
   (paste your Render backend URL from step 9 above)
7. **Click** "Deploy"
8. **Wait** 2-3 minutes
9. **Your app is live!** 🎉

## Test Your Deployment

1. Visit your Vercel URL
2. Upload an audio file
3. Add lyrics
4. Choose style & platform
5. Generate video!

## Current Status

✅ Backend code ready (`backend/main.py`)
✅ Backend dependencies (`backend/requirements.txt`)
⏳ Frontend (create Next.js app separately or use simple HTML/JS)

## Alternative: Simple HTML Frontend

For fastest testing, you can create a simple `index.html` with JavaScript that calls your Render backend API.

## Cost

- Render Free Tier: 750 hours/month
- Vercel Free Tier: 100GB bandwidth
- **Total: $0/month** for MVP

## Need Help?

Repo: https://github.com/24211a6657-sys/LyricFlow
