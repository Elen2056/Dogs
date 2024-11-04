import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import ttk


def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при запросе к API: {e}")
        return None


def show_image():
    image_url = get_random_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img.thumbnail((300, 300))
            img = ImageTk.PhotoImage(img)
            label.config(image=img)
            label.image = img


        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение: {e}")
    # Останавливаем прогрессбар после загрузки картинки
    progress.stop()

def prog():
    # Ставим прогрессбар в начальное положение
    progress['value'] = 0
    # Запускаем прогрессбар и увеличиваем значение от 0 до 100 за 3 секунды
    progress.start(30)
    window.after(3000, show_image)


window = Tk()
window.title("Случайное изображение песика")
# window.geometry("360x420")

label = ttk.Label()
label.pack(padx=10, pady=10)

button = ttk.Button(text="Загрузить изображение", command=prog)
button.pack(padx=10, pady=10)

# Используем ttk.Progressbar для индикации загрузки
progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(padx=10, pady=10)

window.mainloop()

