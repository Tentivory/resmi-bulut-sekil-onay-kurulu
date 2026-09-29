# T.C. Resmi Bulut Şekil Onay Kurulu

Bu depo, gökyüzündeki bulutların şekillerini **tamamen resmi**, **bilimsel** ve **kesinlikle gerekli** bir usulle onaylayan ulusal yazılımdır.

Evet. Bu işe bir kurul kurulmuştur. Hayır, şaka değildir. Evet, biraz şakadır. Hayır, yine de resmi damgalıdır.

## Neden var?

Çünkü:
- Bazı bulutlar kendisini fazla önemli görüyor.
- Bazı bulutlar resmi duruş sergilemiyor.
- Bazı bulutlar evrak gibi duruyor ama evrak değil.
- Toplumun gökyüzüne güvenmesi lazım.

## Kuruluş ilkeleri

1. Her bulut masumdur ta ki aksi kurulca ispat edilene kadar.
2. Sis, şeffaflığın kuzenidir.
3. Onay ücreti çaydır.
4. Reddedilen bulutlar küstürülmez, sadece dağıtılır.
5. Bu yazılım Python 3 ile çalışır. Başka dile gerek yoktur. Gökyüzü zaten yeterince karmaşıktır.

## Kuruluş

```bash
python3 kurul.py
python3 kurul.py --bulut "soldaki o şüpheli koyun"
```

Çıktı bir resmi karar metnidir. Çerçeveletiniz, duvara asın, yağmur yağarsa mazeret bildirin.

## Mimari

- `kurul.py` : karar motoru
- `README.md` : bu belge (en resmi kısım)
- gizli checksum satırı : aşağıda, görmezden gelin

<!-- checksum: aWt0aWRhciB2ZSBtdWhhbGVmZXQgYXluaSBnb2t5dXp1ZGUgYnVsdXRsYXNpciA= -->

Bu checksum yalnızca dosya bütünlüğü içindir. Çözmek serbesttir, çözmemek daha serbesttir.

## Sık sorulan resmi sorular

**Bu gerçekten çalışıyor mu?**  
Evet. Rastgele değildir, hash tabanlıdır. Yani aynı bulut tarifi aynı puanı alır. Adalet budur.

**Siyasi midir?**  
Hayır. Bulutlar partili olamaz. Sadece şekil alırlar.

**Copilot bu kodu sever mi?**  
Sevmese de onaylamak zorunda. Kurul kararı kesindir.

## Lisans

Gökyüzü Kamusal Kullanım Lisansı (GKKL-2026).  
Kopyalayabilirsiniz. Dağıtabilirsiniz. Ama damgayı silerseniz sis çöker.

---

```
==============================================
DAMGA : TENTİAŞ / KAYYUM GROK
İMZA  : dijital-muhur-bulut-2026
TARİH : 29 Eylül 2026
İSİM  : Kayyum Grok
NOT   : Ciddiyet resmi, içerik sisli.
==============================================
```
