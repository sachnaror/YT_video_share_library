from urllib.parse import urlparse, parse_qs

def get_video_code(video_url: str) -> dict:
    """
    Get video code from a video URL:
    - Validate if it's a YouTube link
    - Extract the video ID
    - Return embed link and metadata
    """
    parsed = urlparse(video_url)

    video_id = None

    # Standard YouTube URL: https://www.youtube.com/watch?v=VIDEO_ID
    if "youtube.com" in parsed.netloc:
        qs = parse_qs(parsed.query)
        video_id = qs.get("v", [None])[0]

    # Short YouTube URL: https://youtu.be/VIDEO_ID
    elif "youtu.be" in parsed.netloc:
        video_id = parsed.path.lstrip("/")

    if video_id:
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        return {
            "url": video_url,
            "status": "ok",
            "video_id": video_id,
            "embed_url": embed_url,
            "message": "Valid YouTube video"
        }

    return {
        "url": video_url,
        "status": "error",
        "message": "Unsupported or invalid video format"
    }
