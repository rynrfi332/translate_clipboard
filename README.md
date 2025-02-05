OCR Image Translator
OCR Image Translator adalah sebuah skrip Python yang menggunakan kombinasi Selenium, Google Translate API, dan Yandex OCR untuk menerjemahkan teks dari gambar yang disalin ke clipboard. Skrip ini secara otomatis mendeteksi gambar baru di clipboard, mengambil teks dari gambar menggunakan Yandex OCR, dan menerjemahkannya ke bahasa Indonesia menggunakan Google Translate.

Fitur Utama
Deteksi Gambar Baru di Clipboard : Skrip akan terus memantau clipboard untuk gambar baru.
Ekstraksi Teks dengan OCR : Menggunakan layanan OCR dari Yandex Translate untuk mengekstrak teks dari gambar.
Terjemahan Otomatis : Menerjemahkan teks yang diekstraksi ke bahasa Indonesia (atau bahasa lainnya jika diinginkan).
Kompresi Gambar : Gambar yang diambil dari clipboard dikompresi sebelum diproses untuk mengurangi ukuran file.
Prasyarat
Sebelum menjalankan skrip ini, pastikan Anda telah menginstal dependensi berikut:

Python 3.x
Google Chrome dan ChromeDriver (untuk Selenium)
Pustaka Python :
selenium
googletrans==4.0.0-rc1
Pillow
Anda dapat menginstal pustaka Python yang diperlukan menggunakan pip:

bash
Copy
1
pip install selenium googletrans==4.0.0-rc1 pillow
Instalasi ChromeDriver
Pastikan Anda telah mengunduh ChromeDriver yang sesuai dengan versi Google Chrome yang terinstal di sistem Anda. Letakkan file chromedriver di direktori yang termasuk dalam variabel lingkungan PATH, atau tentukan lokasinya secara eksplisit dalam kode.

Cara Menggunakan
Salin Gambar ke Clipboard : Salin gambar yang ingin Anda terjemahkan ke clipboard (misalnya, dengan menekan Ctrl + C pada gambar).
Jalankan Skrip : Jalankan skrip Python dengan perintah berikut:
bash
Copy
1
python ocr_image_translator.py
Hasil Terjemahan : Skrip akan mendeteksi gambar di clipboard, mengekstrak teks menggunakan OCR, dan mencetak hasil terjemahan ke konsol.
Menghentikan Program : Tekan Ctrl + C untuk menghentikan program.
Konfigurasi Tambahan
Bahasa Tujuan : Secara default, skrip menerjemahkan teks ke bahasa Indonesia (id). Jika Anda ingin menerjemahkan ke bahasa lain, ubah parameter target_language di fungsi translate_text().
python
Copy
1
2
⌄
def translate_text(text, target_language='en'):  # Ubah 'en' untuk bahasa Inggris
    ...
Interval Pemantauan : Interval pemantauan clipboard saat ini diatur ke 0.5 detik. Anda dapat mengubah nilai ini di baris berikut:
python
Copy
1
time.sleep(0.5)  # Ubah nilai ini sesuai kebutuhan
Keterbatasan
Ketergantungan pada Layanan Eksternal : Skrip ini bergantung pada layanan OCR dari Yandex dan Google Translate. Pastikan Anda memiliki akses internet yang stabil.
Batasan API : Beberapa layanan OCR atau terjemahan mungkin memiliki batasan penggunaan harian atau kuota tertentu.

Kontribusi
Kontribusi sangat diterima! Jika Anda menemukan bug atau memiliki fitur baru yang ingin ditambahkan, silakan buat issue atau pull request di repositori ini.

Pengembang
Skrip ini dibuat oleh AI Deepseek dan dwenlm.
