from downloader.extractor import get_playlist_info
from downloader.download_manager import download_playlist


def main():
    print("\n=== YouTube Playlist Downloader ===\n")

    # Step 1: Get Playlist URL
    url = input("Enter YouTube Playlist URL: ").strip()

    print("\nExtracting playlist information...\n")
    playlist_info = get_playlist_info(url)

    if not playlist_info:
        print("Failed to extract playlist data.")
        return

    playlist_title = playlist_info.get("title")
    videos = playlist_info.get("entries", [])

    print(f"Playlist Title: {playlist_title}")
    print(f"Total Videos: {len(videos)}\n")

    if not videos:
        print("No videos found in playlist.")
        return

    # Step 2: Ask Download Type
    print("Select Download Type:")
    print("1. Audio Only")
    print("2. Video")

    choice = input("Enter choice (1 or 2): ").strip()

    # ================= AUDIO MODE =================
    if choice == "1":
        print("\nSelect Audio Bitrate:")
        print("1. 128 kbps")
        print("2. 192 kbps")
        print("3. 320 kbps")

        bitrate_choice = input("Enter choice (1/2/3): ").strip()

        bitrate_map = {
            "1": "128",
            "2": "192",
            "3": "320"
        }

        if bitrate_choice not in bitrate_map:
            print("Invalid bitrate selection.")
            return

        selected_bitrate = bitrate_map[bitrate_choice]

        print(f"\nDownloading audio at {selected_bitrate} kbps...\n")
        download_playlist(
            url=url,
            mode="audio",
            format_option=selected_bitrate
        )

    # ================= VIDEO MODE =================
    elif choice == "2":

        print("\nAvailable Video Formats (based on first video):\n")

        first_video = videos[0]
        formats = first_video.get("formats", [])

        valid_formats = []

        for f in formats:
            if f.get("vcodec") != "none" and f.get("acodec") != "none":
                format_data = {
                    "format_id": f.get("format_id"),
                    "resolution": f.get("resolution"),
                    "ext": f.get("ext")
                }
                valid_formats.append(format_data)

        if not valid_formats:
            print("No valid combined formats found.")
            return

        for fmt in valid_formats:
            print(
                f"Format ID: {fmt['format_id']} | "
                f"Resolution: {fmt['resolution']} | "
                f"Extension: {fmt['ext']}"
            )

        selected_format = input("\nEnter format_id you want: ").strip()

        print(f"\nDownloading videos in format {selected_format}...\n")

        download_playlist(
            url=url,
            mode="video",
            format_option=selected_format
        )

    else:
        print("Invalid selection.")
        return

    print("\nDownload process finished.\n")


if __name__ == "__main__":
    main()
