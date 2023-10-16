import os
from dotenv import load_dotenv
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

load_dotenv()

# primary_color: #0054a6
# secundarY_color: #f5821f


class MenuScreen(MDScreen):
    pass


class ResultadosScreen(MDScreen):
    pass


class ContagemNumerosScreen(MDScreen):
    pass


class LoteriaCefApp(MDApp):
    def __init__(self, **kwargs):
        super(LoteriaCefApp, self).__init__(**kwargs)
        self.API_BASE_URL = os.getenv('API_BASE_URL')
        self.API_JWT_TOKEN = os.getenv('API_JWT_TOKEN')

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"

        sm = MDScreenManager()
        sm.add_widget(MenuScreen())
        sm.add_widget(ResultadosScreen())
        sm.add_widget(ContagemNumerosScreen())

        return sm

    def bt_ultimo_resultado_click(self):
        print(self.API_BASE_URL)
        print(self.API_JWT_TOKEN)


if __name__ == '__main__':
    LoteriaCefApp().run()
