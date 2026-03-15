# To-Do List Uygulaması Planı

Bu belge, Python ile geliştirilecek TOML tabanlı To-Do List (Yapılacaklar Listesi) uygulamasının mimarisini, dosya ağacını ve geliştirme fazlarını (aşamalarını) içerir.

## Dosya Ağacı (Tree)

Projenizi modüler ve yönetilebilir kılmak için aşağıdaki yapı kullanılacaktır:

```text
to-do-list/
├── src/
│   ├── __init__.py
│   ├── main.py          # Uygulamanın ana giriş noktası (komutların alındığı yer)
│   ├── todo.py          # ToDo iş mantığı (Add, Remove, Update görevleri)
│   └── storage.py       # TOML dosyasını okuma/yazma işlemleri
├── data/
│   └── todos.toml       # Görevlerin kaydedileceği veritabanı dosyası
├── requirements.txt     # Bağımlılıklar (örn. tomli-w veya toml)
└── README.md            # Proje açıklaması ve kullanım kılavuzu
```

## Fazlar (Aşamalar)

### Faz 1: Temel Kurulum ve Veri Katmanı (Storage)
- Proje için gerekli klasör yapısının (`src/`, `data/`) oluşturulması.
- Python ile TOML okuma/yazma işlemleri için uygun kütüphanenin seçilmesi (Standart kütüphane `tomllib` Python 3.11'de okuma için var, yazma için harici bir modül gerekecek).
- `storage.py` modülü içinde `todos.toml` dosyasını sorunsuzca okuyan ve dosyaya yeni içerik yazan fonksiyonların oluşturulması.

### Faz 2: Görev İş Mantığı (To-Do Logic)
- `todo.py` dosyasında ana görev yönetim fonksiyonlarının yazılması:
  - **Add**: Listeye yeni bir görev ekleme.
  - **Remove**: Başlığına veya benzersiz ID'sine (sıra numarası tabanlı) göre görev silme.
  - **Update**: Bir görevi "Tick" (✔) veya "Çarpı" (✖) olarak güncelleme (Tamamlandı veya Tamamlanmadı durumu atama).

### Faz 3: Kullanıcı Arayüzü (CLI Entegrasyonu)
- `main.py` içerisine `argparse` kullanılarak detaylı bir Komut Satırı Arayüzü eklenecek.
- Uygulama aşağıdaki argümanları ve kısayollarını destekleyecek:
  - `-h` veya `--help`: Yardım menüsünü ve komut kullanımlarını gösterir.
  - `-a` veya `--add`: Yeni bir To-Do maddesi ekler. (Örn: `python src/main.py -a "Ekmek al"`)
  - `-r` veya `--remove`: Belirtilen bir görevi ID'sine veya adına göre siler. (Örn: `python src/main.py -r 1`)
  - `-u` veya `--update`: Bir görevin tamamlanma durumunu günceller.
    - `+` parametresi alırsa göreve tick (✔) işareti koyar (tamamlandı). (Örn: `python src/main.py -u 1 +`)
    - `-` parametresi alırsa göreve çarpı (✖) işareti koyar (tamamlanmadı). (Örn: `python src/main.py -u 1 -`)
  - `-l` veya `--list`: Mevcut tüm görevleri durum emojileriyle (✔, ✖) birlikte listeler. (Örn: `python src/main.py -l`)
- Kullanıcının konsoldan girdiği değerler parse edilerek, `todo.py` mantık modülündeki ilgili metotlara aktarılacak.

### Faz 4: Test ve Doğrulama
- Her fonksiyonelleğin test edilmesi (veri ekledikten sonra TOML tablosunun doğruluğunu teyit etme vs.).
- Kullanıcı veri hatalarına ve dosya bulunamama gibi durumlara karşı uygun uyarılar yazdırılması (Error Handling).

## User Review Required
Plan ana hatlarıyla bu şekilde. Özellikle **CLI** (Komut Satırı Arayüzü) üzerinden çalışacak bir uygulama kurguladım. Plan sizin için uygunsa onay verebilirsiniz; eğer değiştirmek veya eklemek istediğiniz detaya girmemiz gereken başka özellikler varsa bildirebilirsiniz.
