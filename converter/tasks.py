import requests
import youtube_dl
import re
from django.core.mail import send_mail
from main.celery import app
from django.conf import settings
from .models import Converter


@app.task
def get_mp3(url, email, link):

    DOWNLOAD_OPTIONS_MP3 = {

        'format': 'bestaudio/best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(DOWNLOAD_OPTIONS_MP3) as dl:
        result = dl.extract_info(link)
        filename = result['title'].replace(' ', '%20').replace(' - ', '%20').replace(' | ', '%20')

    download_link = 'http://' + url + '/media/' + filename.replace(' ', '%20').replace(' - ', '%20').replace(' | ', '%20') + '.mp3'
    send_mail('Ссылка на скачивание файла', download_link, settings.EMAIL_HOST_USER, [email], fail_silently=False,)
