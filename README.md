T.C.
ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ
BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ

2020-2021 Eğitim-Öğretim Yılı
152117124-ENGINEERING RESEARCH ON
WIRELESS NETWORKS
FİNAL RAPORU
Proje Başlığı
“Çoklu Dil Destekli Web Tabanlı Sözlük Platformu”


Projeyi Hazırlayanlar:
ERDİ YAMAN, 152120131066, Bilgisayar Mühendisliği
OĞUZ ÇOLAK, 152120161109, Bilgisayar Mühendisliği

Görevliler:
Arş. Gör. Dr. ZUHAL CAN
Dr. Öğr. Üyesi Sinem BOZKURT KESER

Danışman:
Arş. Gör. Dr. ZUHAL CAN


### Kurulum rehberi
Repo clone edildikten hemen sonra config/setting alanında .env dosyası
oluşturulmalıdır. İçeriği şu şekildedir.

```text
SECRET_KEY=ajddkajdsdajfsmfjsadbfhlkuhfsfd
DB_NAME=ea_db
DB_USER=u_admin
DB_PASSWORD=********************
DB_HOST=127.0.0.1

EMAIL_USE_TLS=True
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=***********@gmail.com
EMAIL_HOST_PASSWORD=*****************
EMAIL_PORT=587

```

Sonra bu komutlar sırasıyla çalıştırılmalıdır.

```bash
$ cd ea
$ sudo apt install virtualenv
$ virtualenv --python=python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

