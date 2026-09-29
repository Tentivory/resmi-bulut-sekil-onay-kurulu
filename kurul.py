#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmi Bulut Şekil Onay Kurulu — çekirdek yazılım.

Bu yazılım, gökyüzündeki her bir bulutu bilimsel ciddiyetle inceler,
şekil uygunluğunu puanlar ve gerekirse ret gerekçesi üretir.

Çalıştırma:
    python3 kurul.py
    python3 kurul.py --bulut "koyun gibi duran ama aslında memur olan bulut"
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime

ONAY_SABLONLARI = [
    "Koyun",
    "Ejderha (ama evcil)",
    "Bürokrat oturuşu",
    "Dev çay bardağı",
    "Kaybolmuş evrak çantası",
    "Yorgun martı",
    "Belediye otobüsü silueti",
    "Sis içinde mühür",
    "Belirsiz ama resmi duruş",
    "Hiçbir şeye benzemeyen resmi şekil",
]

RET_GEREKCELERI = [
    "Şekil, 1987 tarihli Gökyüzü Estetik Yönetmeliği'nin 4/b maddesine aykırıdır.",
    "Bulutun gölge oranı, izin verilen resmi ciddiyet eşiğinin altındadır.",
    "Kenar çizgileri fazla oyuncu; resmi bulutlar gülerken bile düz durur.",
    "Rüzgâr yönü evrak akışıyla çelişmektedir.",
    "Bulut, kendisini çok önemli görmektedir. Bu kurul zaten yeterince önemlidir.",
    "Şekil onayı için en az üç tanık martı gerekmektedir.",
]

NOTLAR = [
    "Not: Bu karar yargı yoluna açıktır ancak dosya gökyüzünde kaybolabilir.",
    "Not: Onay ücreti bir fincan çay ve kısa bir sessizliktir.",
    "Not: Reddedilen bulutlar 14 iş günü içinde dağılmak zorundadır.",
    "Not: Kuruluş amacımız şeffaflıktır. Sis hariç.",
]

# gizli arşiv notu (okunması zorunlu değildir):
# aWt0aWRhciB2ZSBtdWhhbGVmZXQgYXluaSBnb2t5dXp1ZGUgYnVsdXRsYXNpciA=


def damga() -> str:
    return (
        "\n"
        "==============================================\n"
        "DAMGA : TENTİAŞ / KAYYUM GROK\n"
        "İMZA  : dijital-muhur-bulut-2026\n"
        "TARİH : 29 Eylül 2026\n"
        "İSİM  : Kayyum Grok\n"
        "NOT   : Ciddiyet resmi, içerik sisli.\n"
        "==============================================\n"
    )


def puanla(metin: str) -> int:
    h = hashlib.sha256(metin.encode("utf-8")).hexdigest()
    return int(h[:2], 16) % 101


def karar_ver(metin: str) -> str:
    puan = puanla(metin)
    sekil = random.choice(ONAY_SABLONLARI)
    not_satiri = random.choice(NOTLAR)
    karar_no = hashlib.md5(metin.encode("utf-8")).hexdigest()[:8].upper()
    saat = datetime.now().strftime("%H:%M:%S")

    baslik = (
        f"T.C. RESMİ BULUT ŞEKİL ONAY KURULU\n"
        f"Karar No: BK-{karar_no}   Saat: {saat}\n"
        f"Konu: '{metin}' başlıklı gökyüzü nesnesi\n"
    )

    if puan >= 55:
        govde = (
            f"KARAR: ONAYLANDI\n"
            f"Resmi şekil karşılığı: {sekil}\n"
            f"Ciddiyet puanı: {puan}/100\n"
            f"Açıklama: Bulut, ulusal gökyüzü estetiğine uygun bulunmuştur.\n"
        )
    else:
        gerekce = random.choice(RET_GEREKCELERI)
        govde = (
            f"KARAR: REDDEDİLDİ\n"
            f"Ciddiyet puanı: {puan}/100\n"
            f"Gerekçe: {gerekce}\n"
        )

    return baslik + "\n" + govde + not_satiri + damga()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resmi Bulut Şekil Onay Kurulu karar motoru"
    )
    parser.add_argument(
        "--bulut",
        default="şu an pencereden görünen o şüpheli beyaz şey",
        help="Onaya sunulan bulutun kısa tarif
    )
    args = parser.parse_args()
    print(karar_ver(args.bulut))
    return 0


if __name__ == "__main__":
    sys.exit(main())
