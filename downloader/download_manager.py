import yt_dlp
import os

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()

        print(f"\rDownloading... {percent} | Speed: {speed} | ETA: {eta}", end="")

    elif d['status'] == 'finished':
        print("\nDownload completed. Processing...\n")


def download_playlist(url: str, mode: str, format_option: str):
    """
    Downloads playlist based on mode:
    - mode = 'audio'  → format_option = bitrate (128/192/320)
    - mode = 'video'  → format_option = format_id
    """

    # Create downloads folder if not exists
    os.makedirs("downloads", exist_ok=True)

    # Base options
    ydl_opts = {
        "outtmpl": "downloads/%(playlist_title)s/%(title)s.%(ext)s",
        "progress_hooks": [progress_hook],
        "noplaylist": False,
        "quiet": True,
    }

    # ================= AUDIO MODE =================
    if mode == "audio":

        ydl_opts.update({
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": format_option,
            }],
        })

    # ================= VIDEO MODE =================
    elif mode == "video":

        ydl_opts.update({
            "format": format_option,
            # No unnecessary post-processing
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as e:
        print(f"\nError during download: {e}")
