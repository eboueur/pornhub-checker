import requests
from bs4 import BeautifulSoup
import re

with open("porn.txt", "a") as file:
    file.write("-------------------------" + "\n")

url = "https://www.pornhub.com/video/search?"

mots_cles = ["Solo Girl Masturbation", "Doigter", "Doigtage", "orgasm", "cumming", "chatte", "joui"]
mots_cles_restriction = ["étudiante", "lycéenne", "fille", "girl", "masturbation", "masturbe"]

blacklist_mots = ["Step Sister", "stepsister", "chevauchait", "pote", "baise", "suce", "levrette intense", "sucent", "éjaculer", "éjacule", "sucent", "Je baise", "baisée", "Bite", "poilu", "bite", "éjaculée", "son ami", "sperme", "couverte", "Gangbang", "hentai", "CUM"]

videos_deja_vues = []

mots_cles_importants = ["chatte"]

with open("output2.txt", "a") as output_file:
    for mot_cle in mots_cles:
        for mot_cle_restriction in mots_cles_restriction:
            recherche_url = url + "search=" + mot_cle + " " + mot_cle_restriction
            response = requests.get(recherche_url)
            soup = BeautifulSoup(response.content, "html.parser")
            videos = soup.find_all("div", class_="thumbnail-info-wrapper")
            
            with open("porn.txt", "a") as file:
                for video in videos:
                    video_url = video.find("a")["href"]
                    if "javascript:void(0)" not in video_url and "playlist" not in video_url:
                        mots_video = video.find("span", class_="title").text.lower() + video.find("span", class_="title").text.upper()
                        if any(mot in mots_video for mot in blacklist_mots):
                            continue
                        if video_url not in videos_deja_vues:
                            videos_deja_vues.append(video_url)
                            print("https://fr.pornhub.com" + video_url + "\n")
                            file.write("https://fr.pornhub.com" + video_url + "\n")
                            if any(mot in mots_video for mot in mots_cles_importants):
                                output_file.write("https://fr.pornhub.com" + video_url + " - " + mots_video + "\n")
