from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.camera import Camera
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from PIL import Image as PILImage
import numpy as np

# ASCII символы от темного к светлому
ASCII_CHARS = "@%#*+=-:. "

class AsciiCameraLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Виджет для отображения ASCII-арта
        self.ascii_label = Label(
            text="Initializing Camera...",
            font_name='monospace',  # Используем моноширинный шрифт
            font_size='8sp', # Размер шрифта можно подобрать
            halign='center',
            valign='middle'
        )
        self.add_widget(self.ascii_label)

        # Виджет камеры (может быть скрыт)
        self.camera = Camera(resolution=(640, 480), play=True)
        self.camera.size_hint_y = 0 # Скрываем виджет камеры
        self.camera.opacity = 0
        self.add_widget(self.camera)

        # Обновляем кадр каждую 1/30 секунды
        Clock.schedule_interval(self.update, 1.0 / 30.0)

    def update(self, dt):
        texture = self.camera.texture
        if not texture:
            return

        # Конвертируем текстуру камеры в изображение PIL
        size = texture.size
        pixels = texture.pixels
        pil_image = PILImage.frombytes(mode='RGBA', size=size, data=pixels)

        # Конвертируем в ASCII
        ascii_art = self.image_to_ascii(pil_image)
        self.ascii_label.text = ascii_art

    def image_to_ascii(self, image):
        # 1. Изменение размера
        width, height = image.size
        aspect_ratio = height / width
        new_width = 100 # Ширина ASCII-арта
        new_height = int(aspect_ratio * new_width * 0.55) # Коррекция для символов
        resized_image = image.resize((new_width, new_height))

        # 2. Конвертация в оттенки серого
        grayscale_image = resized_image.convert("L")

        # 3. Преобразование пикселей в символы
        pixels = np.array(grayscale_image)
        ascii_str = ""
        for row in pixels:
            for pixel_value in row:
                # Нормализуем значение пикселя и выбираем символ
                index = int((pixel_value / 255) * (len(ASCII_CHARS) - 1))
                ascii_str += ASCII_CHARS[index]
            ascii_str += "\n"
        
        return ascii_str

class AsciiCamApp(App):
    def build(self):
        return AsciiCameraLayout()

if __name__ == '__main__':
    AsciiCamApp().run()
