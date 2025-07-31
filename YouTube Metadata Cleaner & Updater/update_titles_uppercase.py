import re
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def get_my_videos(youtube):
    videos = []
    request = youtube.channels().list(part="contentDetails", mine=True)
    response = request.execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    next_page_token = None
    while True:
        playlist_response = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in playlist_response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            title = item["snippet"]["title"]
            videos.append({"id": video_id, "title": title})

        next_page_token = playlist_response.get("nextPageToken")
        if not next_page_token:
            break

    return videos

def update_video_if_needed(youtube, video_id, title):
    video_details = youtube.videos().list(part="snippet", id=video_id).execute()

    if not video_details["items"]:
        print(f"Video not found: {video_id}")
        return

    snippet = video_details["items"][0]["snippet"]
    original_description = snippet.get("description", "")

    # Remove amanayak.github.io links
    cleaned_description = re.sub(r'https://amanayak\.github\.io/\S*', '', original_description).strip()

    # Add new line after GitHub link if it's present and not already followed by the site link
    github_line = "🔗 Source code: https://github.com/codinggujarat"
    site_link = "https://codingcg.vercel.app/"

    if github_line in cleaned_description and site_link not in cleaned_description:
        cleaned_description = cleaned_description.replace(
            github_line, f"{github_line}\n{site_link}"
        )

    updated = False
    new_title = title.upper()

    if title != new_title:
        print(f"Updating Title: {title} → {new_title}")
        updated = True

    if original_description != cleaned_description:
        print(f"Updating Description in: {title}")
        updated = True

    if not updated:
        print(f"No changes for: {title}")
        return

    updated_snippet = {
        "title": new_title,
        "description": cleaned_description,
        "categoryId": snippet.get("categoryId", "22"),
        "tags": snippet.get("tags", []),
        "defaultLanguage": snippet.get("defaultLanguage", None)
    }

    updated_snippet = {k: v for k, v in updated_snippet.items() if v}

    youtube.videos().update(
        part="snippet",
        body={
            "id": video_id,
            "snippet": updated_snippet
        }
    ).execute()

def main():
    youtube = get_authenticated_service()
    videos = get_my_videos(youtube)

    for video in videos:
        update_video_if_needed(youtube, video["id"], video["title"])

if __name__ == "__main__":
    main()
