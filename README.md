readme_content = """# 🛒 Market Stok Takip Otomasyonu

Bu proje, bir marketin ürün stoklarını yönetmek, satış işlemlerini gerçekleştirmek ve detaylı finansal raporlar almak amacıyla geliştirilmiş **modern arayüzlü (Dark Mode) bir masaüstü Enterprise Resource Planning (ERP) yazılımı simülasyonudur.** Python'ın dahili `tkinter` ve `ttk` kütüphaneleri kullanılarak geliştirilmiş olup, herhangi bir harici kütüphane bağımlılığı (veritabanı veya UI kütüphanesi) gerektirmeden doğrudan çalıştırılabilir.

---

## 🚀 Öne Çıkan Özellikler

### 🔑 1. Rol Tabanlı Giriş ve Güvenlik (RBAC)
- Uygulama açılışında kullanıcıyı modern bir giriş ekranı karşılar.
- **SHA-256 şifreleme algoritması** kullanılarak şifreler güvenli bir şekilde doğrulanır.
- Kullanıcı rolüne göre (`Admin` veya `Kasiyer`) menü dinamik olarak şekillenir.

### 📦 2. Gelişmiş Stok Takip Modülü
- **Anlık Arama:** Ürün adı veya barkod numarasına göre gerçek zamanlı filtreleme.
- **Akıllı Sıralama:** Tablo başlıklarına tıklayarak fiyata, stoğa veya barkoda göre artan/azalan sıralama. Orijinal sıralamaya geri dönebilme mekanizması.
- **Hızlı Kopyalama:** Ürüne çift tıklandığında barkod otomatik olarak panoya kopyalanır ve ekranda animasyonlu bir **Toast Bildirimi** belirir.

### 🛍️ 3. Satış ve Stok İade Yönetimi
- **Barkod Okuyucu Simülasyonu:** Barkod okuyucusu olmayan cihazlar için tek tıkla rastgele ürün barkodu getiren "Barkod Okut" sistemi.
- **Anlık Kontrol:** Satış formuna barkod girildiği an ürün adı, fiyatı ve kalan stok bilgisi anlık olarak formda önizlenir.
- **Stok İade Destekli Satış İptali:** Yapılan son satışlar listesinden seçilen bir işlem silindiğinde, satılan adet otomatik olarak ilgili ürünün stoğuna iade edilir.

### 📥 4. Excel / CSV Aktarım Desteği
- Stok listesi tek bir tıkla, Excel ile tam uyumlu ve Türkçe karakter sorunu yaşatmayan `UTF-8-SIG` kodlamalı ve `;` ayraçlı bir CSV dosyası olarak diske aktarılabilir.

### 📊 5. Gelişmiş Raporlama Paneli (Yalnızca Admin)
- **Metrik Kartları:** Toplam Ciro (₺), Toplam İşlem Sayısı ve Satılan Toplam Ürün Adedi modern renkli kartlarla özetlenir.
- Kronolojik sırada tüm satış geçmişi listelenir.

### ⚠️ 6. Kritik Stok Uyarısı (Yalnızca Admin)
- Belirlenen limitin (**stok < 20**) altına düşen ürünler Stok Takibi ekranında kırmızı renkle vurgulanır.
- Kritik Stok sayfasında bu ürünler, eksik adetleriyle birlikte listelenerek tedarik yönetimi kolaylaştırılır.

### 💾 7. Otomatik Veri Güvenliği
- Uygulamadan çıkış yapıldığında veya oturum kapatıldığında, tüm stok ve satış verileri otomatik olarak `urunler.csv` ve `satislar.csv` dosyalarına kalıcı olarak yazılır. Uygulama açılırken bu dosyalardan otomatik olarak yüklenir. Eğer dosyalar yoksa, sistem 100'e yakın hazır temel market ürünüyle otomatik olarak başlar.

---

## 🛠️ Kullanılan Teknolojiler

- **Dil:** Python 3.x
- **Arayüz (GUI):** Tkinter & TTK (Custom Dark Theme Tasarımı)
- **Veri Saklama:** CSV (Comma-Separated Values) Veri Modeli
- **Şifreleme:** Hashlib (SHA-256)
- **Dosya Yönetimi:** OS & FileDialog

---

## 📦 Kurulum ve Çalıştırma

1. Projeyi bilgisayarınıza klonlayın veya indirin: