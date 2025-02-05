# OCR Image Translator

OCR Image Translator adalah sebuah skrip Python yang menggunakan kombinasi Selenium, Google Translate API, dan Yandex OCR untuk menerjemahkan teks dari gambar yang disalin ke clipboard. Skrip ini secara otomatis mendeteksi gambar baru di clipboard, mengambil teks dari gambar menggunakan Yandex OCR, dan menerjemahkannya ke bahasa Indonesia menggunakan Google Translate.

## Fitur Utama
- **Deteksi Gambar Baru di Clipboard**: Skrip akan terus memantau clipboard untuk gambar baru.
- **Ekstraksi Teks dengan OCR**: Menggunakan layanan OCR dari Yandex Translate untuk mengekstrak teks dari gambar.
- **Terjemahan Otomatis**: Menerjemahkan teks yang diekstraksi ke bahasa Indonesia (atau bahasa lainnya jika diinginkan).
- **Kompresi Gambar**: Gambar yang diambil dari clipboard dikompresi sebelum diproses untuk mengurangi ukuran file.

## Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda telah menginstal dependensi berikut:

1. **Python 3.x**
2. **Google Chrome** dan **ChromeDriver** (untuk Selenium)
3. **Pustaka Python**:
   - `selenium`
   - `googletrans==4.0.0-rc1`
   - `Pillow`

Anda dapat menginstal pustaka Python yang diperlukan menggunakan pip:

```bash
pip install selenium googletrans==4.0.0-rc1 pillow
