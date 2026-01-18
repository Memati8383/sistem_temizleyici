# Sistem Temizleyici (Python)

Bu araç, Windows işletim sisteminde gereksiz dosyaları temizlemek ve sistem performansını artırmak için tasarlanmış modern bir Python betiğidir.

## Özellikler

- **Gereksiz Dosya Temizliği:** Kullanıcı geçici dosyaları (TEMP), Windows geçici dosyaları ve Prefetch klasörünü temizler.
- **Geri Dönüşüm Kutusu:** Geri dönüşüm kutusunu boşaltır.
- **Log Dosyaları:** Sistem kök dizinindeki `.log` dosyalarını temizler.
- **DNS Temizliği:** DNS önbelleğini temizleyerek internet bağlantısını tazelemeye yardımcı olur.
- **Görsel İlerleme Çubuğu:** `tqdm` kütüphanesi ile işlemleri görsel olarak takip edebilirsiniz.
- **Otomatik Yönetici Yetkisi:** Gerekli izinler için otomatik olarak yönetici yetkisi ister.

## Kurulum

1. Python'un yüklü olduğundan emin olun.
2. Gerekli kütüphaneleri yüklemek için (isteğe bağlı, program otomatik yüklemeye çalışacaktır):
   ```bash
   pip install tqdm
   ```

## Kullanım

Betiği doğrudan çalıştırın:

```bash
python temizle.py
```

## Notlar

- Bu araç sadece **Windows** üzerinde çalışmak üzere tasarlanmıştır.
- Bazı dosyalar kullanımda olduğu için silinemeyebilir (bu normaldir ve hata oluşturmadan atlanır).
