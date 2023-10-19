import os
import requests
from dotenv import load_dotenv
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast
from kivy.utils import rgba

load_dotenv()


class MenuScreen(MDScreen):
    pass


class UltimoResultadoScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(UltimoResultadoScreen, self).__init__(*args, **kwargs)
        app_running = MDApp.get_running_app()

        self.API_BASE_URL = app_running.API_BASE_URL
        self.API_VERSION = app_running.API_VERSION
        self.API_JWT_TOKEN = app_running.API_JWT_TOKEN
        self.primary_color = app_running.primary_color
        self.secundary_color = app_running.secundary_color
        self.toast_timer = app_running.toast_timer

    def on_pre_enter(self):
        # Forçar pintar os inputs
        for key in self.ids.keys():
            if isinstance(self.ids[key], MDTextField):
                self.ids[key].focus = True
                self.ids[key].focus = False
                self.ids[key].bind(focus=self.on_textfield_focus)

    def on_enter(self):
        self.preenche_ultimo_sorteio()

    def get_ultimo_sorteio(self):
        req = requests.get(f'{self.API_BASE_URL}/{self.API_VERSION}/megasena/resultados?sorteio=ultimo',
                           headers={'Accept': 'application/json', 'Authorization': f'Bearer {self.API_JWT_TOKEN}'})
        return req.json(), req.status_code

    def preenche_ultimo_sorteio(self):
        req_json, status_code = self.get_ultimo_sorteio()
        if status_code == 200:
            req_json = req_json[0]
            self.ids.txt_ultimo_resultado_sorteio.text = str(
                req_json['sorteio'])
            self.ids.txt_ultimo_resultado_data.text = str(req_json['data'])
            self.ids.txt_ultimo_resultado_dezena1.text = str(
                req_json['dezena1'])
            self.ids.txt_ultimo_resultado_dezena2.text = str(
                req_json['dezena2'])
            self.ids.txt_ultimo_resultado_dezena3.text = str(
                req_json['dezena3'])
            self.ids.txt_ultimo_resultado_dezena4.text = str(
                req_json['dezena4'])
            self.ids.txt_ultimo_resultado_dezena5.text = str(
                req_json['dezena5'])
            self.ids.txt_ultimo_resultado_dezena6.text = str(
                req_json['dezena6'])
        else:
            toast(str(req_json['msgErro']), rgba(
                self.secundary_color), self.toast_timer)

    def btn_ultimo_resultado_click(self):
        self.preenche_ultimo_sorteio()

    def on_textfield_focus(self, instance_text_field, focus: bool):
        # pass
        if instance_text_field.label_id is not '':
            self.ids[instance_text_field.label_id].color = self.secundary_color if focus == True else self.primary_color


class ResultadosScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(ResultadosScreen, self).__init__(*args, **kwargs)
        app_running = MDApp.get_running_app()

        self.API_BASE_URL = app_running.API_BASE_URL
        self.API_VERSION = app_running.API_VERSION
        self.API_JWT_TOKEN = app_running.API_JWT_TOKEN
        self.primary_color = app_running.primary_color
        self.secundary_color = app_running.secundary_color
        self.toast_timer = app_running.toast_timer

    def on_enter(self):
        self.ids.txt_resultados_sorteio.text = '0'
        # Forçar pintar os inputs
        self.ids.txt_resultados_sorteio.focus = True
        self.ids.txt_resultados_sorteio.focus = False

    def btn_resultados_limpar_click(self):
        self.ids.txt_resultados_sorteio.text = '0'
        self.ids.txt_resultados_data.text = ''
        self.ids.txt_resultados_dezena1.text = ''
        self.ids.txt_resultados_dezena2.text = ''
        self.ids.txt_resultados_dezena3.text = ''
        self.ids.txt_resultados_dezena4.text = ''
        self.ids.txt_resultados_dezena5.text = ''
        self.ids.txt_resultados_dezena6.text = ''
        self.ids.txt_resultados_sorteio.focus = True

    def btn_resultados_pesquisar_click(self):
        if self.ids.txt_resultados_sorteio.text is None or self.ids.txt_resultados_sorteio.text is '':
            toast('Informe o número do sorteio', rgba(
                self.secundary_color), self.toast_timer)
            return
        else:
            sorteio = int(self.ids.txt_resultados_sorteio.text)

            if sorteio <= 0:
                toast('Número do sorteio inválido', rgba(
                    self.secundary_color), self.toast_timer)
                return

            req_json, status_code = self.get_sorteio(sorteio)
            if status_code == 200:
                req_json = req_json[0]
                self.ids.txt_resultados_data.text = str(req_json['data'])
                self.ids.txt_resultados_data.focus = True
                self.ids.txt_resultados_data.focus = False
                self.ids.txt_resultados_dezena1.text = str(
                    req_json['dezena1'])
                self.ids.txt_resultados_dezena1.focus = True
                self.ids.txt_resultados_dezena1.focus = False
                self.ids.txt_resultados_dezena2.text = str(
                    req_json['dezena2'])
                self.ids.txt_resultados_dezena2.focus = True
                self.ids.txt_resultados_dezena2.focus = False
                self.ids.txt_resultados_dezena3.text = str(
                    req_json['dezena3'])
                self.ids.txt_resultados_dezena3.focus = True
                self.ids.txt_resultados_dezena3.focus = False
                self.ids.txt_resultados_dezena4.text = str(
                    req_json['dezena4'])
                self.ids.txt_resultados_dezena4.focus = True
                self.ids.txt_resultados_dezena4.focus = False
                self.ids.txt_resultados_dezena5.text = str(
                    req_json['dezena5'])
                self.ids.txt_resultados_dezena5.focus = True
                self.ids.txt_resultados_dezena5.focus = False
                self.ids.txt_resultados_dezena6.text = str(
                    req_json['dezena6'])
                self.ids.txt_resultados_dezena6.focus = True
                self.ids.txt_resultados_dezena6.focus = False
            else:
                toast(str(req_json['msgErro']), rgba(
                    self.secundary_color), self.toast_timer)

    def get_sorteio(self, sorteio):
        req = requests.get(f'{self.API_BASE_URL}/{self.API_VERSION}/megasena/resultados?sorteio={sorteio}',
                           headers={'Accept': 'application/json', 'Authorization': f'Bearer {self.API_JWT_TOKEN}'})
        return req.json(), req.status_code


class ContagemNumerosScreen(MDScreen):
    pass


class LoteriaCefApp(MDApp):
    def __init__(self, **kwargs):
        super(LoteriaCefApp, self).__init__(**kwargs)
        self.API_BASE_URL = os.getenv('API_BASE_URL')
        self.API_JWT_TOKEN = os.getenv('API_JWT_TOKEN')
        self.API_VERSION = '/api/v1'
        self.toast_timer = 3.0

    def build(self):
        self.primary_color = "#0054a6"
        self.secundary_color = "#f5821f"
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        sm = MDScreenManager()
        sm.add_widget(UltimoResultadoScreen())
        sm.add_widget(MenuScreen())
        sm.add_widget(ResultadosScreen())
        sm.add_widget(ContagemNumerosScreen())

        sm.current = 'menu_screen'

        return sm

    # def bt_ultimo_resultado_click(self):
    #     print(self.API_BASE_URL)
    #     print(self.API_JWT_TOKEN)

    def bt_resultado_click(self):
        print(self.API_BASE_URL)
        print(self.API_JWT_TOKEN)


if __name__ == '__main__':
    LoteriaCefApp().run()
