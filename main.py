# main.py
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms  # 'sms.py' dosyasındaki 'SendSms' sınıfını import ettik
from concurrent.futures import ThreadPoolExecutor, wait

# Kodun geri kalanı burada