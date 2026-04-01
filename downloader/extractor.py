import yt_dlp

def get_playlist_info(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": "in_playlist",  # ✅ Only fetch lightweight metadata for playlist entries
        "ignoreerrors": True,           # ✅ Skip unavailable/private videos silently
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info

    except Exception as e:
        print(f"Error extracting media info: {e}")
        return None


def get_first_video_formats(video_url):
    """Fetch full format info ONLY for the first video, used to show quality options."""
    ydl_opts = {
        "quiet": True,
        "skip_download": True, 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return info.get("formats", [])

    except Exception as e:
        print(f"Error fetching formats: {e}")
        return []