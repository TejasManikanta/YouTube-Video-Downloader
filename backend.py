from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import yt_dlp

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demonstration
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the path where you want to save the video (e.g., the Videos folder on your PC)
output_path = "C:/Users/Manikanta/Videos/"

@app.post("/download")
def download_video(link: str = Form(...)):
    # Set options for downloading
    ydl_opts = {
        "format": "best",
        "outtmpl": os.path.join(output_path, "video.mp4")  # Save in the specified folder
    }

    # Download the video using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

    return {"status": "Download started"}

