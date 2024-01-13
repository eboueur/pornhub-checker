import requests
from bs4 import BeautifulSoup

url = "https://fr.pornhub.com/video/search?"
mots_cles = ["Etudiante solo masturbation", "Student solo masturbation"]



visited_links = []

def rechercher_videos():
    for mot_cle in mots_cles:
        recherche_url = f"{url}search={mot_cle}&page=1"
        response = requests.get(recherche_url)
        soup = BeautifulSoup(response.content, "html.parser")
        videos = soup.find_all("div", class_="thumbnail-info-wrapper")
        for video in videos:
            video_url = video.find("a")["href"]
            if "javascript:void(0)" not in video_url and "playlist" not in video_url:
                video_title = video.find("span", class_="title").text.strip().lower()
                if "sperme" not in video_title and "bite" not in video_title and "branler" not in video_title and "sexe" not in video_title and "orgie" not in video_title and "familyxxx" not in video_title and "baise" not in video_title and "big shot" not in video_title:
                    if video_url not in visited_links:
                        with open("output.txt", "r") as file:
                            if video_url not in file.read():
                                print(video_title)
                                with open("output.txt", "a") as file:
                                    file.write("https://fr.pornhub.com" + video_url + "\n")
                                    print("https://fr.pornhub.com" + video_url + "\n")
                                visited_links.append(video_url)
    

# Appeler la fonction rechercher_videos
rechercher_videos()
