import os
import requests
from dotenv import load_dotenv
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

load_dotenv()


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
        self.API_VERSION = '/api/v1'

    def build(self):
        self.primary_color = "#0054a6"
        self.secundary_color = "#f5821f"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = MDScreenManager()
        sm.add_widget(MenuScreen())
        sm.add_widget(ResultadosScreen())
        sm.add_widget(ContagemNumerosScreen())

        sm.current = 'menu_screen'

        return sm

    def bt_ultimo_resultado_click(self):
        print(self.API_BASE_URL)
        print(self.API_JWT_TOKEN)
        r = requests.get(f'{self.API_BASE_URL}/{self.API_VERSION}/megasena/resultados?sorteio=ultimo',
                         headers={'Accept': 'application/json', 'Authorization': f'Bearer {self.API_JWT_TOKEN}'})
        print(r.json())
        print(f'status code: {r.status_code}')


if __name__ == '__main__':
    LoteriaCefApp().run()
