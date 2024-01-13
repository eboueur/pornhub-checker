import requests
from bs4 import BeautifulSoup

url = "https://www.pornhub.com/video/search?"

mots_cles = ["je me doigte", "Solo Girl Masturbation", "Doigter", "Doigtage", "chatte", "joui","étudiante", "fille", "girl", "masturbation", "masturbe"]
mots_cles_restriction = ["je me doigte", "Solo Girl Masturbation", "Doigter", "Doigtage", "chatte", "joui","étudiante", "fille", "girl", "masturbation", "masturbe"]


videos_deja_vues = []

with open("output2.txt", "a") as output_file:
    for mot_cle in mots_cles:
        for mot_cle_restriction in mots_cles_restriction:
            recherche_url = url + "search=" + mot_cle + " " + mot_cle_restriction
            response = requests.get(recherche_url)
            soup = BeautifulSoup(response.content, "html.parser")
            videos = soup.find_all("div", class_="thumbnail-info-wrapper")
            title_element = soup.title

            with open("porn.txt", "a") as file:
                for video in videos:
                    video_url = video.find("a")["href"]
                    if "javascript:void(0)" not in video_url and "playlist" not in video_url:
                        if video_url not in videos_deja_vues:
                            if title_element:
                                title_text = title_element.text.lower()
                                if "bite" not in title_text or "ejac" not in title_text or "baiser" not in title_text:
                                    if "chatte" in title_text or "doigte" in title_text:
                                        videos_deja_vues.append(video_url)
                                        print("https://fr.pornhub.com" + video_url + "\n")
                                        file.write("https://fr.pornhub.com" + video_url + "\n")
