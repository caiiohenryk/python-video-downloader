import yt_dlp as yt

def download_video(url):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',  # Define o nome do arquivo de saída (ou edite, se preferir)
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'cookiefile': 'cookies.txt'  # Caminho para o arquivo de cookies, se necessário
    }

    with yt.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Digite o URL do vídeo: ")
    download_video(video_url)
