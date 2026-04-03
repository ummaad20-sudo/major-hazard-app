from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# ================= DATA =================
daftar_hazard = [
{"judul": "Bekerja dengan logam panas",
"detail": """FURNACE
1. Dilarang masuk area tanpa izin
2. Jaga jarak saat tapping
3. Gunakan APD lengkap tahan panas

CASTING
- Dilarang naik mesin saat berputar
- Pastikan area aman

SLAG POND
- Gunakan 3 titik kontak
- Dilarang mendekat saat proses
"""},

{"judul": "Bekerja di Ruang Terbatas",
"detail": """CONFINED SPACE
1. Cek gas sebelum masuk
2. Gunakan blower
3. Sistem kerja berpasangan
4. Gunakan APD lengkap
"""},

{"judul": "Bekerja di ketinggian",
"detail": """WORKING AT HEIGHT
1. Gunakan full body harness
2. Gunakan lifeline
3. Pastikan pekerja terlatih
"""},

{"judul": "Lock Out & Tag Out (LOTO)",
"detail": """LOTO
1. Isolasi semua energi
2. Gunakan lock pribadi
3. Dilarang buka LOTO orang lain
"""},

{"judul": "Boiler dan bejana tekan",
"detail": """BOILER
1. Cek safety valve
2. Monitor tekanan
3. Operator wajib bersertifikat
"""},

{"judul": "Peralatan berputar",
"detail": """ROTATING EQUIPMENT
1. Gunakan guard
2. Hindari pakaian longgar
3. Gunakan emergency stop
"""},

{"judul": "Lifting activity",
"detail": """LIFTING
1. Gunakan sling sesuai SWL
2. Area harus steril
3. Operator bersertifikat
"""},

{"judul": "Kelistrikan",
"detail": """ELECTRICAL
1. Gunakan APD listrik
2. LOTO wajib
3. Gunakan alat deteksi listrik
"""},

{"judul": "Kendaraan & alat berat",
"detail": """HEAVY EQUIPMENT
1. Operator wajib SIMPER
2. Lakukan P2H
3. Jaga jarak aman
"""},

{"judul": "Perlengkapan roda",
"detail": """TYRE
1. Gunakan tyre cage
2. Jaga jarak aman
3. Gunakan alat ukur tekanan
"""},

{"judul": "Lereng tebing",
"detail": """SLOPE
1. Waspada longsor
2. Gunakan safety berm
3. Hentikan saat hujan
"""},

{"judul": "Sekitar air",
"detail": """WATER AREA
1. Gunakan life jacket
2. Jangan kerja sendiri
3. Siapkan alat darurat
"""},

{"judul": "Bahan kimia",
"detail": """CHEMICAL
1. Gunakan MSDS
2. Gunakan APD
3. Simpan sesuai standar
"""},
]


# ================= SCREEN MENU =================
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(
            text="13 MAJOR HAZARD",
            size_hint_y=None,
            height=60,
            font_size=22,
            bold=True
        )

        layout.add_widget(title)

        scroll = ScrollView()

        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))

        for i, item in enumerate(daftar_hazard):
            btn = Button(
                text=f"{i+1}. {item['judul']}",
                size_hint_y=None,
                height=60
            )
            btn.bind(on_press=lambda x, idx=i: self.buka_detail(idx))
            grid.add_widget(btn)

        scroll.add_widget(grid)
        layout.add_widget(scroll)

        self.add_widget(layout)

    def buka_detail(self, index):
        self.manager.get_screen("detail").tampilkan(index)
        self.manager.current = "detail"


# ================= SCREEN DETAIL =================
class DetailScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title = Label(
            text="",
            size_hint_y=None,
            height=50,
            font_size=18,
            bold=True
        )

        self.content = Label(
            text="",
            size_hint_y=None,
            font_size=16
        )
        self.content.bind(texture_size=self.content.setter('size'))

        scroll = ScrollView()
        scroll.add_widget(self.content)

        btn_back = Button(
            text="Kembali",
            size_hint_y=None,
            height=60
        )
        btn_back.bind(on_press=self.kembali)

        self.layout.add_widget(self.title)
        self.layout.add_widget(scroll)
        self.layout.add_widget(btn_back)

        self.add_widget(self.layout)

    def tampilkan(self, index):
        hazard = daftar_hazard[index]
        self.title.text = hazard["judul"]
        self.content.text = hazard["detail"]

    def kembali(self, instance):
        self.manager.current = "menu"


# ================= APP =================
class HazardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(DetailScreen(name="detail"))
        return sm


if __name__ == "__main__":
    HazardApp().run()                height: 60
                on_release: app.stop()

<DetailScreen>:
    name: "detail"

    BoxLayout:
        orientation: 'vertical'

        Label:
            id: title
            font_size: 24

        ScrollView:
            Label:
                id: detail
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "Kembali"
            size_hint_y: None
            height: 60
            on_release: app.root.current = "menu"
'''

class MenuScreen(Screen):
    def on_enter(self):
        layout = self.ids.hazard_list
        layout.clear_widgets()
        from kivy.uix.button import Button

        for i, h in enumerate(daftar_hazard):
            btn = Button(text=f"{i+1}. {h['judul']}", size_hint_y=None, height=80)
            btn.bind(on_release=lambda btn, x=i: self.open_detail(x))
            layout.add_widget(btn)

    def open_detail(self, index):
        detail = self.manager.get_screen("detail")
        detail.ids.title.text = daftar_hazard[index]['judul']
        detail.ids.detail.text = daftar_hazard[index]['detail']
        self.manager.current = "detail"

class DetailScreen(Screen):
    pass

class AppUtama(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    AppUtama().run()
