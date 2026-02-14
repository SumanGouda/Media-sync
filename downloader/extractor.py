import yt_dlp


def get_playlist_info(url: str) -> dict | None:
    """
    Extract playlist metadata without downloading.
    Returns playlist info dictionary or None if failed.
    """

    ydl_opts = {
        "quiet": True,
        "extract_flat": False,  # Get full metadata
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if "entries" not in info:
                print("No playlist entries found.")
                return None

            return info

    except Exception as e:
        print(f"Error extracting playlist info: {e}")
        return None
