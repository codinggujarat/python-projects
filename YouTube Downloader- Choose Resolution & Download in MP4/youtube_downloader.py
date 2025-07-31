# Import the yt_dlp module for downloading YouTube videos
import yt_dlp

# Function to download a video from YouTube at the specified resolution
def download_video(url, resolution):
    # Define options for yt_dlp
    ydl_opts = {
        # Select best video with max height <= resolution and best audio
        'format': f'bestvideo[height<={resolution}]+bestaudio/best',
        # Merge video and audio into MP4 format
        'merge_output_format': 'mp4',
        # Output filename format: Title [Resolution].ext
        'outtmpl': '%(title)s [%(resolution)s].%(ext)s',
        # Show output during download (set False to show messages)
        'quiet': False,
        # Disable playlist downloads
        'noplaylist': True
    }

    # Use the yt_dlp object with defined options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"\n⬇️ Downloading {resolution}p video...")
            # Start the download process
            ydl.download([url])
            print("✅ Download completed successfully!")
        except Exception as e:
            # Print any errors encountered
            print(f"❌ Error: {e}")

# Main function to run the script
def main():
    # Ask user to input the YouTube video URL
    url = input("🔗 Enter YouTube video URL: ").strip()

    # Display resolution choices
    print("\n🎯 Choose resolution:")
    print("1. 2160 (4K)")
    print("2. 1440 (2K)")
    print("3. 1080 (Full HD)")
    print("4. 720 (HD)")

    # Get user input for resolution choice
    choice = input("Enter choice (1-4): ").strip()

    # Map the choice to actual resolution values
    resolution_map = {
        '1': '2160',
        '2': '1440',
        '3': '1080',
        '4': '720'
    }

    # Default to 1080p if invalid choice
    resolution = resolution_map.get(choice, '1080')

    # Call function to download the video
    download_video(url, resolution)

# Entry point of the script
if __name__ == "__main__":
    main()
