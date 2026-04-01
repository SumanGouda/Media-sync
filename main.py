from downloader.extractor import get_playlist_info, get_first_video_formats
from downloader.download_manager import download_playlist


def print_separator():
    print("-" * 45)


def get_valid_input(prompt, valid_choices):
    """Keep asking until the user enters a valid choice."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid input. Please enter one of: {', '.join(valid_choices)}")


def select_audio_bitrate():
    """Prompt user to select audio bitrate and return the selected value."""
    print("\nSelect Audio Bitrate:")
    print("  1. 128 kbps")
    print("  2. 192 kbps")
    print("  3. 320 kbps")

    bitrate_map = {
        "1": "128",
        "2": "192",
        "3": "320",
    }

    choice = get_valid_input("Enter choice (1/2/3): ", bitrate_map.keys())
    return bitrate_map[choice]


def select_video_format(first_video_url):
    """
    Fetch formats for the first video and prompt the user to pick one.
    Returns the selected format_id, or None if no valid formats found.
    """
    print("\nFetching available video formats from the first video...")
    formats = get_first_video_formats(first_video_url)

    # Filter to only formats that have a video stream
    valid_formats = [
        f for f in formats
        if f.get("vcodec") not in (None, "none")
        and f.get("resolution") not in (None, "unknown")
    ]

    if not valid_formats:
        print("No valid video formats found for this media.")
        return None

    # Deduplicate by resolution to keep the list clean
    seen_resolutions = set()
    unique_formats = []
    for f in valid_formats:
        res = f.get("resolution")
        if res not in seen_resolutions:
            seen_resolutions.add(res)
            unique_formats.append(f)

    print_separator()
    print(f"{'#':<4} {'Format ID':<14} {'Resolution':<14} {'Ext'}")
    print_separator()

    for i, fmt in enumerate(unique_formats, start=1):
        print(
            f"{i:<4} {fmt.get('format_id', 'N/A'):<14} "
            f"{fmt.get('resolution', 'N/A'):<14} "
            f"{fmt.get('ext', 'N/A')}"
        )

    print_separator()

    valid_indices = [str(i) for i in range(1, len(unique_formats) + 1)]
    choice = get_valid_input(
        f"Select format number (1-{len(unique_formats)}): ", valid_indices
    )

    selected = unique_formats[int(choice) - 1]
    return selected.get("format_id")


def main():
    print("\n" + "=" * 45)
    print("         YouTube / Media Downloader")
    print("=" * 45 + "\n")

    # ── Step 1: Get URL ──────────────────────────────
    url = input("Enter Media URL (playlist or single video):\n> ").strip()
    if not url:
        print("No URL entered. Exiting.")
        return

    # ── Step 2: Extract lightweight metadata ─────────
    print("\nExtracting media information (this should be fast)...")
    media_info = get_playlist_info(url)

    if not media_info:
        print("Failed to extract media information. Check the URL and try again.")
        return

    # ── Step 3: Determine playlist vs single video ───
    if media_info.get("_type") == "playlist":
        videos = [v for v in media_info.get("entries", []) if v]  # filter out None entries
        media_title = media_info.get("title", "Unknown Playlist")
        print(f"\nPlaylist detected : {media_title}")
    else:
        videos = [media_info]
        media_title = media_info.get("title", "Unknown Video")
        print(f"\nSingle video detected : {media_title}")

    print(f"Total videos      : {len(videos)}")

    if not videos:
        print("No downloadable videos found. Exiting.")
        return

    # ── Step 4: Choose download type ─────────────────
    print_separator()
    print("Select Download Type:")
    print("  1. Audio Only (MP3)")
    print("  2. Video")
    print_separator()

    download_type = get_valid_input("Enter choice (1 or 2): ", ["1", "2"])

    # ── Step 5: Audio mode ───────────────────────────
    if download_type == "1":
        selected_bitrate = select_audio_bitrate()

        print_separator()
        print(f"Starting audio download at {selected_bitrate} kbps...")
        print(f"Saving to : downloads/{media_title}/")
        print_separator()

        download_playlist(
            url=url,
            mode="audio",
            format_option=selected_bitrate,
        )

    # ── Step 6: Video mode ───────────────────────────
    elif download_type == "2":
        # Get the URL of the first video to fetch format options
        first_video = videos[0]
        first_video_url = (
            first_video.get("url")
            or first_video.get("webpage_url")
            or first_video.get("original_url")
        )

        if not first_video_url:
            print("Could not determine the URL of the first video. Exiting.")
            return

        selected_format_id = select_video_format(first_video_url)

        if not selected_format_id:
            print("No format selected. Exiting.")
            return

        print_separator()
        print(f"Starting video download (format: {selected_format_id})...")
        print(f"Saving to : downloads/{media_title}/")
        print_separator()

        download_playlist(
            url=url,
            mode="video",
            format_option=selected_format_id,
        )

    # ── Done ─────────────────────────────────────────
    print("\n" + "=" * 45)
    print("  All downloads finished successfully!")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()
