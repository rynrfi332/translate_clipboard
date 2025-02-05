import time
import os
from PIL import ImageGrab, Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator

def translate_text(text, target_language='id'):
    translator = Translator()
    detected_lang = translator.detect(text).lang
    translated = translator.translate(text, src=detected_lang, dest=target_language)
    return translated.text

def translate_image(driver):
    try:
        # Ambil gambar dari clipboard
        image = ImageGrab.grabclipboard()
        if isinstance(image, Image.Image):
            image_path = "clipboard_image.png"
            image.thumbnail((800, 600))  # Kompres gambar
            image.save(image_path)
            
            # Akses Yandex Translate
            driver.get("https://translate.yandex.com/en/ocr")
            
            # Tunggu hingga elemen <input type="file"> muncul
            upload_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'fileInput'))
            )
            upload_button.send_keys(os.path.abspath(image_path))
            
            # Tunggu hasil terjemahan
            translated_text_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ocr-text__result'))
            )
            translated_text = translated_text_element.text
            
            # Deteksi bahasa dan terjemahkan ke bahasa Indonesia
            final_translation = translate_text(translated_text)
            print("Translated Text:", final_translation)
            os.remove(image_path)
        else:
            print("No image found in clipboard.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menerjemahkan gambar: {e}")

last_image_hash = None

def is_new_image():
    global last_image_hash
    image = ImageGrab.grabclipboard()
    if isinstance(image, Image.Image):
        current_hash = hash(image.tobytes())
        if current_hash != last_image_hash:
            last_image_hash = current_hash
            return True
    return False

def main():
    driver = webdriver.Chrome()
    try:
        while True:
            if is_new_image():
                translate_image(driver)
            time.sleep(0.5)  # Cek clipboard setiap 0.5 detik
    except KeyboardInterrupt:
        print("Program dihentikan.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
