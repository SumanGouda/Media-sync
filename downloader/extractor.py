import yt_dlp


def get_playlist_info(url):
    ydl_opts = {
        "quiet": False,
        "skip_download": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            # 🔥 If it's a playlist
            if info.get("_type") == "playlist":
                return info

            # 🔥 If it's a single video
            else:
                return info

    except Exception as e:
        print(f"Error extracting media info: {e}")
        return None
