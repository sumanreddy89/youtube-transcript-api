from fastapi import FastAPI, Request
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend tools like Bolt to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcript")
async def get_transcript(req: Request):
    body = await req.json()
    url = body.get("url", "")
    video_id = url.split("v=")[-1][:11]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([seg["text"] for seg in transcript])
        return {"transcript": full_text}
    except Exception as e:
        return {"error": str(e)}
