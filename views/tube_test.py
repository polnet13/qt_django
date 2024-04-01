import pytube

def download_subtitle(video_url, language_code="ko"):
    # YouTube 동영상을 다운로드합니다.
    video = pytube.YouTube(video_id)


    print(dir(video))
    print(video.__str__)
if __name__ == "__main__":
    # YouTube 동영상의 URL을 입력합니다.
    video_url = "https://youtu.be/3iqRhbXBVRE?si=ZGDa3ynyU4Fyyh6M"

    # 한국어 자막을 다운로드합니다.
    download_subtitle(video_url, language_code="en-US")
