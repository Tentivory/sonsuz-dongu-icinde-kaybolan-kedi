#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Döngü İçinde Kaybolan Kedi Simülatörü
v1.0 - Çok ciddi bir bilimsel araç gibi görünüyor ama aslında değil.
"""

import random
import time
import sys

# Gizli not: bazen sistemler de döngüye girer, çıkış yoktur.
# (sadece bir kediyle ilgili, başka hiçbir şeyle değil)

MIYAVLAR = [
    "Miyav...",
    "MIYAV!",
    "mır mır...",
    "*yavaşça uzaklaşır*",
    "Hangi döngüdeyim ben?",
    "Bu sonsuz mu yoksa sadece uzun mu?",
    "Pati piti pati...",
    "Kedi olarak yaşamak zordur, özellikle sonsuz döngüde.",
    "Çıkış var mı? Yoksa sadece giriş mi?",
]

def kaybol():
    print("=" * 50)
    print("KEDİ SONSUL DÖNGÜYE GİRDİ")
    print("Kurtarmak için Ctrl+C'ye basabilirsin ama kedi kurtulmaz.")
    print("=" * 50)
    
    sayac = 0
    while True:
        sayac += 1
        miyav = random.choice(MIYAVLAR)
        bekleme = random.uniform(0.5, 3.0)
        
        print(f"[{sayac}] {miyav} (bekliyor: {bekleme:.1f}s)")
        
        # Ara sıra felsefi kriz
        if sayac % 7 == 0:
            print("   >>> Kedi varoluşsal kriz yaşıyor... <<<")
        
        time.sleep(bekleme)
        
        if sayac > 1000000:
            print("Kedi sayacını unuttu, baştan başlıyor gibi hissediyor.")
            sayac = 0

if __name__ == "__main__":
    try:
        kaybol()
    except KeyboardInterrupt:
        print("\n\nKedi döngüden çıktı sanıyorsun.")
        print("Ama aslında sadece sen çıktın. Kedi hâlâ orada.")
        print("Tekrar çalıştır, gör.")
        sys.exit(0)
