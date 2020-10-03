import os
import requests
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, response
from django.shortcuts import render, redirect

from converter.forms import ConvertForm
from converter.models import Converter
from .tasks import get_mp3


def get_link(request):
    if request.method == "POST":
        form = ConvertForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data.get("link")
            email = form.cleaned_data.get("email")
            url = request.get_host()
            get_mp3.delay(url, email, link)
            messages.success(
                request, "Ссылка на скачивание отправлена на почту!"
            )
    else:
        form = ConvertForm()
    return render(request, "index.html", locals())
