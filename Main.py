from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests


class NiftyApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.label = Label(
            text="Loading NIFTY...",
            font_size='32sp'
        )
        self.add_widget(self.label)
        # Update every 5 seconds
        Clock.schedule_interval(self.update_nifty, 5)

    def update_nifty(self, dt):
        try:
            # NSE India API
            url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
            headers = {"User-Agent": "Mozilla/5.0"}
            r = requests.get(url, headers=headers, timeout=5)
            data = r.json()
            price = data["data"][0]["lastPrice"]
            change = data["data"][0]["change"]

            # Green if up, Red if down
            color = "[color=00ff00]" if change >= 0 else "[color=ff0000]"
            self.label.markup = True
            self.label.text = f"{color}NIFTY 50\n{price}\n{change}[/color]"

        except Exception:
            self.label.text = "Waiting for data..."


class NiftyLiveApp(App):
    def build(self):
        return NiftyApp()


if __name__ == "__main__":
    NiftyLiveApp().run()
