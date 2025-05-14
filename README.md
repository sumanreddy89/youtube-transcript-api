# YouTube Transcript API

A simple FastAPI microservice to extract transcripts from public YouTube videos using `youtube-transcript-api`. Ideal for fast AI summarization pipelines (e.g. with GPT via Bolt or Supabase).

## Features
- Pulls auto-generated YouTube captions in seconds
- CORS-enabled — ready for frontend or browser usage
- Deployable to Render, Replit, Railway, etc.

## 🚀 POST /transcript

**Request Body**
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
