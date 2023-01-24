from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import base64
import os
import urllib.parse

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def get_screenshot(request):
    """Сделать снимок экрана и вернтуть файл png на основе url"""

    width = 1024
    height = 768

    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url', '')
        if url is not None and url != '':
            save = False
            base_url = '{0.scheme}://{0.netloc}'.format(urllib.parse.urlsplit(url))
            domain = urllib.parse.urlsplit(url)[1]
            params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
            if len(params) > 0:
                if 'w' in params: 
                    width = int(params['w'][0])
                if 'h' in params: 
                    height = int(params['h'][0])
            my_driver = driver        
            my_driver.get(url)
            my_driver.set_window_size(width, height)

            if 'save' in params and params['save'][0] == 'true':
                save = True
                now = str(datetime.today().timestamp())
                img_dir = settings.MEDIA_ROOT
                img_name = ''.join([now, '_image.png'])
                full_img_path = os.path.join(img_dir, img_name)
                if not os.path.exists(img_dir):
                    os.makedirs(img_dir)
                my_driver.save_screenshot(full_img_path)
                screenshot = img_name
            else:
                screenshot_img = driver.get_screenshot_as_png()
                screenshot = base64.encodebytes(screenshot_img)

            context = {
                'screenshot': screenshot,
                'domain': domain,
                'base_url': base_url,
                'full_url': url,
                'save': save,
            }

            my_driver.quit()
            return render(request, 'generator/index.html', context=context)
    
    else:
        return render(request, 'generator/index.html')
    
    
    
    







   
    




