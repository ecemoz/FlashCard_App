# 📚 Flash Card App

Bu proje, Fransızca-Türkçe kelimeleri öğrenmek için geliştirilmiş eğlenceli bir 🧠 *Flash Card* uygulamasıdır. Tkinter kullanılarak oluşturulan bu masaüstü uygulama, kullanıcılara rastgele bir Fransızca kelime gösterir ve ⏳ 3 saniye sonra bu kelimenin Türkçe anlamını otomatik olarak açıklar.

## ✨ Özellikler

- ⏳ 3 saniye içinde kart otomatik olarak ters döner.
- ✅ Kullanıcı, kelimeyi biliyorsa kalıcı olarak kelime listesinden kaldırabilir.
- ❌✅ "Doğru" ve "Yanlış" butonları ile etkileşimlidir.
- 📂 Kelime listesi CSV dosyasından yüklenir.
- 💾 Bilinen kelimeler, "french_words.csv" dosyasına kaydedilir.

## 🛠️ Gereksinimler

- Python 3.x
- pandas
- tkinter

## 📁 Dosya Yapısı

```
.
├── data
│   ├── french_words.csv          # Orijinal kelime listesi
│   └── words_to_learn.csv       # Bilinmeyen kelimeler burada tutulur
├── images
│   ├── card_front.png           # Kartın ön yüzü
│   ├── card_back.png            # Kartın arka yüzü
│   ├── right.png                # Doğru butonu görseli
│   └── wrong.png                # Yanlış butonu görseli
├── main.py                      # Ana uygulama dosyası
```

## ▶️ Nasıl Çalıştırılır

1. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas
```

2. Proje dizininde terminali açın ve aşağıdaki komutu çalıştırın:
```bash
python main.py
```

3. Uygulama çalıştığında aşağıdaki gibi bir ekranla karşılaşırsınız:
![image](https://github.com/user-attachments/assets/eb104864-a4b6-42b4-8a1a-200255fc28fe)
![image](https://github.com/user-attachments/assets/b14d5bea-9208-4a9d-a810-c0a1ab58a0f2)

## 🤝 Katkı
Yeni kelime listeleri ekleyebilir, uygulamaya zamanlayıcı seçenekleri, skor sistemi ⭐️ veya kullanıcı puanı gibi yeni özellikler entegre edebilirsiniz.

Pull Request göndermek için lütfen önce bir issue oluşturun.

## 📄 Lisans
Bu proje kişisel eğitim amaçlıdır. Ticari kullanım dışı özgürce kullanabilir, geliştirebilir ve paylaşabilirsiniz.

