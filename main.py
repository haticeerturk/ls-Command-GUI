# !/usr/bin/env python
# -*- coding: cp1254 -*-
# -*- coding: utf-8 -*-

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui

uygulama = QApplication([])
windows = QWidget()

metin = QLabel('')

scrollA = QtGui.QScrollArea()
scrollA.setWidgetResizable(True)
scrollAreaWidgetContents = QtGui.QWidget(scrollA)
scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 247))
scrollA.setWidget(scrollAreaWidgetContents)
scrollA.setWidget(metin)
def ls_a():
    f = os.popen("ls -a")
    result = "<h3 style='color:#DC143C'> Aciklama : Sakli dosyalarda gosterilir.</h3><br/>"
    for i in f.readlines():
        result += i
	result += "<br/>"
    metin.setText(result)

def ls_A():
    f = os.popen("ls -A")
    result = "<h3 style='color:#DC143C'> Aciklama : . ve .. dizinleri listelenmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_author():
    f = os.popen("ls --author -l")
    result = "<h3 style='color:#DC143C'> Aciklama : Her dosyanin olusturanida yazilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_b():
    f = os.popen("ls -b")
    result = "<h3 style='color:#DC143C'> Aciklama : Grafik olmayan karakterler icin C tarzi kacisi yazilir. Ornegin bosluk karakterinde '\ ' kullanilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_block_size():
    f = os.popen("ls --block-size=M")
    result = "<h3 style='color:#DC143C'> Aciklama : Yazdirmadan once boyutlari tarafindan olceklenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_B():
    f = os.popen("ls -B")
    result = "<h3 style='color:#DC143C'> Aciklama : Sonu ~ ile gosterilmis girdiler gosterilmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_c_lt():
    f = os.popen("ls -c -lt")
    result = "<h3 style='color:#DC143C'> Aciklama : Dosya durum bilgilerinin son degisiklikzamani siralanir ve gosterilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_c_l():
    f=os.popen("ls -c -l")
    result = "<h3 style='color:#DC143C'> Aciklama : Dosya durum bilgilerinin son degisiklik zamani gosterilir ve isme gore siralanir, aksi takdirde en son degistirilmis dosya durum bilgilerinin son degisiklik zamanina gore siralanir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_d():
    f = os.popen("ls -d")
    result = "<h3 style='color:#DC143C'> Aciklama : Dizin icindeki girdiler listelenmez ve sembolik baglantilar incelenmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_D():
    f = os.popen("ls -D")
    result = "<h3 style='color:#DC143C'> Aciklama : Emacs' dired modu icin tasarlanmis cikti listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_F():
    f = os.popen("ls -F")
    result = "<h3 style='color:#DC143C'> Aciklama : Girislere */=>@| gostergelerinden biri eklenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_file_type():
    f = os.popen("ls --file-type")
    result = " <h3 style='color:#DC143C'> Aciklama : Ayni sekilde '*' haric eklenmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_g():
    f = os.popen("ls -g")
    result = "<h3 style='color:#DC143C'> Aciklama : -l gibidir fakat sahipler listelenmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_G():
    f = os.popen("ls -G")
    result = "<h3 style='color:#DC143C'> Aciklama : Uzun bir listede grup adlari yazilmaz.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_h_l():
    f = os.popen("ls -h -l")
    result = "<h3 style='color:#DC143C'> Aciklama : Insanin okuyabilecegi formatta yazilir. (Or., 1K 234M 2G)</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_si():
    f = os.popen("ls --si")
    result = "<h3 style='color:#DC143C'> Aciklama : Ayni sekilde fakat 1024 degil 1000 yetkisini kullanilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_H():
    f = os.popen("ls -H")
    result = "<h3 style='color:#DC143C'> Aciklama : Komut satirinda listelenen sembolik baglantilari izleyin.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_i():
    f = os.popen("ls -i")
    result = "<h3 style='color:#DC143C'> Aciklama : Her dosyanin dizin numarasi yazdirilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_k():
    f = os.popen("ls -k")
    result = "<h3 style='color:#DC143C'> Aciklama : 1024 byte'lik bloklar kullanilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_l():
    f = os.popen("ls -l")
    result = "<h3 style='color:#DC143C'> Aciklama : Detayli bir sekilde listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_L():
    f = os.popen("ls -L")
    result = "<h3 style='color:#DC143C'> Aciklama : Bir sembolik bagin dosya bilgileri gösterilirken, dosya icin varolan  baglanti basvurularindan ziyade kendisi icin olan bilgileri gosterilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_m():
    f = os.popen("ls -m")
    result = "<h3 style='color:#DC143C'> Aciklama : Girdi listeleri araya virgul konularak siralanir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_n():
    f = os.popen("ls -n")
    result = "<h3 style='color:#DC143C'> Aciklama : -l gibi ama sayisal kullanici ve grup kimlikleriyle listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_N():
    f = os.popen("ls -N")
    result = "<h3 style='color:#DC143C'> Aciklama : Acik giris adlari yazdirilir(Ornegin denetim karakterleri ozel olarak sayilmaz).</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_o():
    f = os.popen("ls -o")
    result = "<h3 style='color:#DC143C'> Aciklama : -l gibi ama grup bilgileri listelenmez.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_p():
    f = os.popen("ls -p")
    result = "<h3 style='color:#DC143C'> Aciklama : Dizinlere / gostergesi eklenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_q():
    f = os.popen("ls -q")
    result = "<h3 style='color:#DC143C'> Aciklama : Grafik olmayan karakterler yerine ? yazilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_show_control_chars():
    f = os.popen("ls --show-control-chars")
    result = "<h3 style='color:#DC143C'> Aciklama : Grafik olmayan karakterler gosterilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_r():
    f = os.popen("ls -r")
    result = "<h3 style='color:#DC143C'> Aciklama : Siralama yaparken tersine siralayarak gosterilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_R():
    f = os.popen("ls -R")
    result = "<h3 style='color:#DC143C'> Aciklama : Alt dizinler tekrarlamali olarak listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_s():
    f = os.popen("ls -s")
    result = "<h3 style='color:#DC143C'> Aciklama : Bloklarin icindeki her dosya ayrilmis boyutlari ile listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_S():
    f = os.popen("ls -S")
    result = "<h3 style='color:#DC143C'> Aciklama : Dosya boyutuna gore sirali olarak listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_t():
    f = os.popen("ls -t")
    result = "<h3 style='color:#DC143C'> Aciklama : Dosyalar son degistirilme tarihlerine gore siralanarak listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_u_lt():
    f = os.popen("ls -u -lt")
    result = "<h3 style='color:#DC143C'> Aciklama : Erisim suresini siralar ve listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_u_l():
    f = os.popen("ls -u -l")
    result = "<h3 style='color:#DC143C'> Aciklama : Erisim suresini gosterir ve adlari siralar aksi takdirde erisim suresi siralanir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_U():
    f = os.popen("ls -U")
    result = "<h3 style='color:#DC143C'> Aciklama : Girdiler siralanmaz, dizindeki siralariyle listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_v():
    f = os.popen("ls -v")
    result = "<h3 style='color:#DC143C'> Aciklama : Metin icinde surum sayilariyla siralama yapilir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_x():
    f = os.popen("ls -x")
    result = "<h3 style='color:#DC143C'> Aciklama : Girdiler sutunlar ile degil satirlar ile listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_X():
    f = os.popen("ls -X")
    result = "<h3 style='color:#DC143C'> Aciklama : Girdilerin uzantilari alfabetik olarak siralanmis halde listelenir. </h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_1():
    f = os.popen("ls -1")
    result = "<h3 style='color:#DC143C'> Aciklama : Her satirda bir dosya listelenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_help():
    f = os.popen("ls --help")
    result = "<h3 style='color:#DC143C'> Aciklama : Yardim ve cikis goruntulenir.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)

def ls_version():
    f = os.popen("ls --version")
    result = "<h3 style='color:#DC143C'> Aciklama : Surum bilgilerini gosterir ve cikar.</h3>"
    for i in f.readlines():
        result += i
        result += "<br/>"
    metin.setText(result)
izgara = QGridLayout()
button_ls_a = QPushButton('ls -a')
izgara.addWidget(button_ls_a, 1, 0)
windows.connect(button_ls_a, SIGNAL('pressed()'), ls_a)

izgara.addWidget(scrollA, 1, 3, 21, 21)

button_ls_A = QPushButton('ls -A')
izgara.addWidget(button_ls_A, 2, 0)
windows.connect(button_ls_A, SIGNAL('pressed()'), ls_A)

button_ls_author = QPushButton('ls -author')
izgara.addWidget(button_ls_author, 3, 0)
windows.connect(button_ls_author, SIGNAL('pressed()'), ls_author)

button_ls_b = QPushButton('ls -b')
izgara.addWidget(button_ls_b, 4, 0)
windows.connect(button_ls_b, SIGNAL('pressed()'), ls_b)

button_ls_block = QPushButton('ls --block-size=M')
izgara.addWidget(button_ls_block, 5, 0)
windows.connect(button_ls_block, SIGNAL('pressed()'), ls_block_size)

button_ls_B = QPushButton('ls -B')
izgara.addWidget(button_ls_B, 6, 0)
windows.connect(button_ls_B, SIGNAL('pressed()'), ls_B)

button_ls_c_lt = QPushButton('ls -c -lt')
izgara.addWidget(button_ls_c_lt, 7, 0)
windows.connect(button_ls_c_lt, SIGNAL('pressed()'), ls_c_lt)

button_ls_c_l = QPushButton('ls -c -l')
izgara.addWidget(button_ls_c_l, 8, 0)
windows.connect(button_ls_c_l, SIGNAL('pressed()'), ls_c_l)

button_ls_d = QPushButton('ls -d')
izgara.addWidget(button_ls_d, 9, 0)
windows.connect(button_ls_d, SIGNAL('pressed()'), ls_d)

button_ls_D = QPushButton('ls -D')
izgara.addWidget(button_ls_D, 10, 0)
windows.connect(button_ls_D, SIGNAL('pressed()'), ls_D)

button_ls_F = QPushButton('ls -F')
izgara.addWidget(button_ls_F, 11, 0)
windows.connect(button_ls_F, SIGNAL('pressed()'), ls_F)

button_ls_file_type = QPushButton('ls --file-type')
izgara.addWidget(button_ls_file_type, 12, 0)
windows.connect(button_ls_file_type, SIGNAL('pressed()'), ls_file_type)

button_ls_g = QPushButton('ls -g')
izgara.addWidget(button_ls_g, 13, 0)
windows.connect(button_ls_g, SIGNAL('pressed()'), ls_g)

button_ls_G = QPushButton('ls -G')
izgara.addWidget(button_ls_G, 14, 0)
windows.connect(button_ls_G, SIGNAL('pressed()'), ls_G)

button_ls_h_l = QPushButton('ls -h -l')
izgara.addWidget(button_ls_h_l, 15, 0)
windows.connect(button_ls_h_l, SIGNAL('pressed()'), ls_h_l)

button_ls_si = QPushButton('ls --si')
izgara.addWidget(button_ls_si, 16, 0)
windows.connect(button_ls_si, SIGNAL('pressed()'), ls_si)

button_ls_H = QPushButton('ls -H')
izgara.addWidget(button_ls_H, 17, 0)
windows.connect(button_ls_H, SIGNAL('pressed()'), ls_H)

button_ls_i = QPushButton('ls -i')
izgara.addWidget(button_ls_i, 18, 0)
windows.connect(button_ls_i, SIGNAL('pressed()'), ls_i)

button_ls_k = QPushButton('ls -k')
izgara.addWidget(button_ls_k, 19, 0)
windows.connect(button_ls_k, SIGNAL('pressed()'), ls_k)

button_ls_l = QPushButton('ls -l')
izgara.addWidget(button_ls_l, 20, 0)
windows.connect(button_ls_l, SIGNAL('pressed()'), ls_l)

button_ls_L = QPushButton('ls -L')
izgara.addWidget(button_ls_L, 21, 0)
windows.connect(button_ls_L, SIGNAL('pressed()'), ls_L)

button_ls_m = QPushButton('ls -m')
izgara.addWidget(button_ls_m, 1, 1)
windows.connect(button_ls_m, SIGNAL('pressed()'), ls_m)

button_ls_n = QPushButton('ls -n')
izgara.addWidget(button_ls_n, 2, 1)
windows.connect(button_ls_n, SIGNAL('pressed()'), ls_n)

button_ls_N = QPushButton('ls -N')
izgara.addWidget(button_ls_N, 3, 1)
windows.connect(button_ls_N, SIGNAL('pressed()'), ls_N)

button_ls_o = QPushButton('ls -o')
izgara.addWidget(button_ls_o, 4, 1)
windows.connect(button_ls_o, SIGNAL('pressed()'), ls_o)

button_ls_p = QPushButton('ls -p')
izgara.addWidget(button_ls_p, 5, 1)
windows.connect(button_ls_p, SIGNAL('pressed()'), ls_p)

button_ls_q = QPushButton('ls -q')
izgara.addWidget(button_ls_q, 6, 1)
windows.connect(button_ls_q, SIGNAL('pressed()'), ls_q)

button_ls_show_control_chars = QPushButton('ls --show-control-chars')
izgara.addWidget(button_ls_show_control_chars, 7, 1)
windows.connect(button_ls_show_control_chars, SIGNAL('pressed()'), ls_show_control_chars)

button_ls_r = QPushButton('ls -r')
izgara.addWidget(button_ls_r, 8, 1)
windows.connect(button_ls_r, SIGNAL('pressed()'), ls_r)

button_ls_R = QPushButton('ls -R')
izgara.addWidget(button_ls_R, 9, 1)
windows.connect(button_ls_R, SIGNAL('pressed()'), ls_R)

button_ls_s = QPushButton('ls -s')
izgara.addWidget(button_ls_s, 10, 1)
windows.connect(button_ls_s, SIGNAL('pressed()'), ls_s)

button_ls_S = QPushButton('ls -S')
izgara.addWidget(button_ls_S, 11, 1)
windows.connect(button_ls_S, SIGNAL('pressed()'), ls_S)

button_ls_t = QPushButton('ls -t')
izgara.addWidget(button_ls_t, 12, 1)
windows.connect(button_ls_t, SIGNAL('pressed()'), ls_t)

button_ls_u_lt = QPushButton('ls -u -lt')
izgara.addWidget(button_ls_u_lt, 13, 1)
windows.connect(button_ls_u_lt, SIGNAL('pressed()'), ls_u_lt)

button_ls_u_l = QPushButton('ls -u -l')
izgara.addWidget(button_ls_u_l, 14, 1)
windows.connect(button_ls_u_l, SIGNAL('pressed()'), ls_u_l)

button_ls_U = QPushButton('ls -U')
izgara.addWidget(button_ls_U, 15, 1)
windows.connect(button_ls_U, SIGNAL('pressed()'), ls_U)

button_ls_v = QPushButton('ls -v')
izgara.addWidget(button_ls_v, 16, 1)
windows.connect(button_ls_v, SIGNAL('pressed()'), ls_v)

button_ls_x = QPushButton('ls -x')
izgara.addWidget(button_ls_x, 17, 1)
windows.connect(button_ls_x, SIGNAL('pressed()'), ls_x)

button_ls_X = QPushButton('ls -X')
izgara.addWidget(button_ls_X, 18, 1)
windows.connect(button_ls_X, SIGNAL('pressed()'), ls_X)

button_ls_1 = QPushButton('ls -1')
izgara.addWidget(button_ls_1, 19, 1)
windows.connect(button_ls_1, SIGNAL('pressed()'), ls_1)

button_ls_help = QPushButton('ls --help')
izgara.addWidget(button_ls_help, 20, 1)
windows.connect(button_ls_help, SIGNAL('pressed()'), ls_help)

button_ls_version = QPushButton('ls --version')
izgara.addWidget(button_ls_version, 21, 1)
windows.connect(button_ls_version, SIGNAL('pressed()'), ls_version)

windows.setLayout(izgara)
windows.setWindowTitle('LS')
windows.setFixedSize(1400,710)
windows.show()

uygulama.exec_()
