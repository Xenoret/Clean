#!/usr/bin/python3
#-*- coding: UTF-8 -*-

#by Xenoret


import os

os.system('cls || clear')

print('''
========================
{FAST CLEAR YOUR SYSTEM}
=======================''')

os.system('sudo apt update && sudo apt upgrade')#Update and upgrade system
os.system('sudo apt-get clean && sudo apt-get autoremove')#Эти команды очистят локальный репозиторий от скачанных файлов пакетов.
os.system('sudo apt -f install')#Установка пакетов зависимостей которые были не до конца установлены

print('''\n
======================================
{Your operating system is clean, bye!}
======================================''')
