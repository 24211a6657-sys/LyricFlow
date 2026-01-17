from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
import os
import uuid
import json
from datetime import datetime, timedelta
from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout
from PIL import Image, ImageDraw, ImageFont
import numpy as np

app = FastAPI(title="LyricFlow API")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directories
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "uploads")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "outputs")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Store job status
jobs = {}

class VideoRequest(BaseModel):
    audio_filename: str
    lyrics: List[str]
    style: str
    platform: str

class JobStatus(BaseModel):
    status: str
    progress: int
    video_url: Optional[str] = None
    error: Optional[str] = None

# Style presets
STYLES = {
    "aesthetic": {
        "bg_color": (255, 182, 193),
        "text_color": "white",
        "font_size": 60,
        "font_weight": "bold"
    },
    "elegant": {
        "bg_color": (25, 25, 25),
        "text_color": "gold",
        "font_size": 55,
        "font_weight": "normal"
    },
    "bold": {
        "bg_color": (255, 0, 0),
        "text_color": "white",
        "font_size": 70,
        "font_weight": "bold"
    },
    "dark": {
        "bg_color": (15, 15, 30),
        "text_color": "cyan",
        "font_size": 58,
        "font_weight": "bold"
    },
    "minimal": {
        "bg_color": (245, 245, 245),
        "text_color": "black",
        "font_size": 50,
        "font_weight": "normal"
    },
    "lyrical": {
        "bg_color": (138, 43, 226),
        "text_color": "white",
        "font_size": 62,
        "font_weight": "bold"
    }
}

PLATFORMS = {
    "reels": {"width": 1080, "height": 1920},
    "shorts": {"width": 1080, "height": 1920},
    "tiktok": {"width": 1080, "height": 1920},
    "square": {"width": 1080, "height": 1080}
}

@app.get("/")
async def root():
    return {"message": "LyricFlow API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    try:
        file_ext = os.path.splitext(file.filename)[1]
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        return {"filename": unique_filename, "original_name": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate_video(request: VideoRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued", "progress": 0}
    
    background_tasks.add_task(create_video, job_id, request)
    
    return {"job_id": job_id}

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

@app.get("/download/{filename}")
async def download_video(filename: str):
    file_path = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type="video/mp4", filename=filename)

def create_video(job_id: str, request: VideoRequest):
    try:
        jobs[job_id]["status"] = "processing"
        jobs[job_id]["progress"] = 10
        
        audio_path = os.path.join(UPLOAD_DIR, request.audio_filename)
        if not os.path.exists(audio_path):
            jobs[job_id]["status"] = "error"
            jobs[job_id]["error"] = "Audio file not found"
            return
        
        # Load audio
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        jobs[job_id]["progress"] = 20
        
        # Get style and platform settings
        style = STYLES.get(request.style.lower(), STYLES["aesthetic"])
        platform = PLATFORMS.get(request.platform.lower(), PLATFORMS["reels"])
        
        width, height = platform["width"], platform["height"]
        jobs[job_id]["progress"] = 30
        
        # Create background
        bg_clip = ColorClip(size=(width, height), color=style["bg_color"], duration=duration)
        jobs[job_id]["progress"] = 40
        
        # Create lyric clips
        lyrics = request.lyrics
        time_per_line = duration / len(lyrics) if lyrics else duration
        
        text_clips = []
        for i, line in enumerate(lyrics):
            start_time = i * time_per_line
            txt_clip = TextClip(
                line,
                fontsize=style["font_size"],
                color=style["text_color"],
                size=(width - 100, None),
                method='caption',
                align='center'
            ).set_position('center').set_start(start_time).set_duration(time_per_line)
            
            txt_clip = txt_clip.crossfadein(0.3).crossfadeout(0.3)
            text_clips.append(txt_clip)
            
            progress = 40 + int((i / len(lyrics)) * 40)
            jobs[job_id]["progress"] = progress
        
        jobs[job_id]["progress"] = 80
        
        # Composite video
        video = CompositeVideoClip([bg_clip] + text_clips)
        video = video.set_audio(audio)
        jobs[job_id]["progress"] = 85
        
        # Export video
        output_filename = f"{job_id}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        video.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio_codec='aac',
            threads=4,
            preset='medium'
        )
        
        video.close()
        audio.close()
        
        jobs[job_id]["status"] = "completed"
        jobs[job_id]["progress"] = 100
        jobs[job_id]["video_url"] = f"/download/{output_filename}"
        
    except Exception as e:
        jobs[job_id]["status"] = "error"
        jobs[job_id]["error"] = str(e)
        print(f"Error generating video: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
