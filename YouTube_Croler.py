import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import youtube_dl
import os.path


class Music:
    def YouTube_Downloader(self, output_path, MusicDownload_List):
        path = "C:\\Users\\xhens\\Desktop\\chromedriver.exe"
        count = 1

        Url = "https://www.youtube.com/results?search_query="
        driver = webdriver.Chrome(path)
        for query in range(len(MusicDownload_List)):
            Download_Path = os.path.join(output_path, '{}.%(title)s.%(ext)s'.format(count))

            driver.get(Url + MusicDownload_List[query])
            # title = driver.find_elements_by_id('video-title')
            title = driver.find_element_by_id('video-title')
            attr = title.get_attribute("href")
            if attr is not None:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': Download_Path,
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([attr])
                    count += 1

        driver.close()


if __name__ == '__main__':
    Mp3_Download_Path = 'Download'
    MusicCrol_Down = Music()
    MusicDownload = ["", ""] # Insert desired image name
    MusicCrol_Down.YouTube_Downloader(Mp3_Download_Path, MusicDownload)
