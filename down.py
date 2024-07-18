import os
import yt_dlp

def download_video(url, output_path=None):
    # Déterminer le chemin par défaut comme le dossier Téléchargements dans le dossier personnel
    default_output_path = os.path.expanduser('~/Téléchargements')
    
    # Utiliser le chemin par défaut s'il n'est pas spécifié
    output_path = output_path or default_output_path
    
    # Options pour yt-dlp
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Modèle de nom de fichier pour les vidéos téléchargées
        'format': 'bestvideo[ext=mp4]+bestaudio/best' # Télécharger la meilleure qualité vidéo disponible
    }

    # Téléchargement du fichier
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    # Demander l'URL du fichier à l'utilisateur
    url = input("Entrez l'URL du fichier que vous souhaitez télécharger : ")
    
    # Télécharger le fichier le chemin par défaut comme Téléchargements dans le dossier personnel
    download_video(url)
    
    # Confirmation de téléchargement
    print("Téléchargement terminé !")
