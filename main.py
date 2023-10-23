from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from pytube import YouTube

whole = '''
MDScreen:

    MDLabel:
        text: "Video Downloader"
        text_size: self.size
        halign: "center"
        valign: "top"
        theme_text_color: "Custom" 
        text_color: (237/255.0, 125/255.0, 49/255.0) 
        font_style: "H2"

'''
text = """
MDTextField:
    hint_text:"Enter The URL" 
    pos_hint:{"center_x": 0.5, "center_y": 0.55}
    icon_right: "youtube"
    size_hint_x:None
    width: 300
"""


class Test(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        self.display = Builder.load_string(text)

        button = MDFloatingActionButton(
            text="Download", icon="download-box", pos_hint={"center_x": 0.5, "center_y": 0.3}, on_release=self.download)
        screen.add_widget(button)
        screen.add_widget(self.display)
        screen.add_widget(Builder.load_string(whole))
        return screen

    def download(self, obj):
        if self.display.text == "":
            check = "Please enter the URL"
        else:
            check = "Video Downloaded"
            yt = YouTube(self.display.text)
            stream = yt.streams.get_highest_resolution()
            stream.download()
        close = MDRectangleFlatButton(
            text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(text=check,
                               size_hint=(0.7, 1), buttons=[close])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


Test().run()
