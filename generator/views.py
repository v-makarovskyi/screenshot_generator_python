from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from datetime import datetime
from selenium import webdriver

import base64
import os
import urllib.parse as urlparse

def get_screenshot(request):
    """Сделать снимок экрана и вернтуть файл png на основе url"""
    

