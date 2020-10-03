import os
import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from converter.models import Converter
from converter.forms import ConvertForm
from .tasks import get_mp3
from django.conf import settings
from django.http import HttpResponse, response


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
