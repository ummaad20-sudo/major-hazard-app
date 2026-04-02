from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# ================= FULL DATA =================
daftar_hazard = [
{"judul": "Bekerja dengan logam panas",
"detail": """================ FURNACE ================
1. Bagi yang tidak berkepentingan DILARANG KERAS memasuki area tungku pembakaran atau furnace.
2. Pada saat proses aktivitas tapping pekerja harus menjaga jarak aman dari titik keluarnya metal atau slag.
3. Dilarang keras meloncati launder saat tapping kecuali akses tersedia.
4. Gunakan APD tahan api lengkap.
5. Pastikan celana menutupi sepatu.
6. Pastikan pipa oksigen tidak bocor.
7. Jika ada getaran/suhu naik segera tinggalkan area.
8. Thermocouple wajib APD lengkap.
NB: Jika furnace abnormal segera evakuasi.

================ CASTING ================
1. Dilarang menaiki mesin saat berputar.
2. Hindari titik jepit.
3. Pastikan mesin kering.
4. Dilarang di area jatuh produk.

================ SLAG POND ================
1. Pastikan pagar terpasang.
2. Gunakan 3 titik kontak.
3. Bunyikan alarm sebelum tapping.

================ HOT STOVE ================
1. Gunakan APD lengkap.
2. Dilarang merokok.

================ TIPS ================
- Bunyi sirine sebelum tapping
- Pastikan APD lengkap
"""},

{"judul": "Bekerja di Ruang Terbatas",
"detail": """================ CONFINED SPACE ================
1. Wajib APD.
2. Cek gas sebelum masuk.
3. Gunakan blower.
4. Sistem body pair.
5. Isolasi energi (LOTO).
6. SCBA tersedia.

================ TIPS ================
- Pastikan izin kerja
- Pastikan alat darurat tersedia
"""},

{"judul": "Bekerja di ketinggian",
"detail": """================ WORKING AT HEIGHT ================
1. Wajib permit kerja.
2. Gunakan full body harness.
3. Gunakan lifeline.
4. Gunakan 3 titik kontak.
5. Pastikan scaffolding aman.

================ TIPS ================
- Pastikan harness terpasang
"""},

{"judul": "LOTO",
"detail": """================ LOTO ================
1. Isolasi energi.
2. Gunakan SOP.
3. Tidak boleh buka LOTO orang lain.
4. Gunakan alat non logam.

================ TIPS ================
- Identifikasi semua energi
"""},

{"judul": "Boiler",
"detail": """================ BOILER ================
1. Monitor tekanan.
2. Safety valve harus aktif.
3. Air cukup.
4. Sertifikasi wajib.

================ TIPS ================
- Monitor rutin
"""},

{"judul": "Peralatan berputar",
"detail": """================ ROTATING ================
1. Gunakan guard.
2. LOTO saat maintenance.
3. Gunakan emergency stop.
4. Hindari area berputar.

================ TIPS ================
- Pastikan semua aman
"""},

{"judul": "Lifting",
"detail": """================ LIFTING ================
1. Gunakan SWL sesuai.
2. Operator bersertifikat.
3. Komunikasi rigger.
4. Area steril.

================ TIPS ================
- Gunakan permit
"""},

{"judul": "Kelistrikan",
"detail": """================ ELECTRICAL ================
1. Gunakan APD.
2. Gunakan LOTO.
3. Gunakan body pair.
4. Gunakan alat deteksi listrik.

================ TIPS ================
- Pastikan SOP
"""},

{"judul": "Alat berat",
"detail": """================ HEAVY EQUIPMENT ================
1. Operator wajib SIO/SIMPER.
2. Lakukan P2H.
3. Jaga jarak aman.
4. Ikuti rambu.

================ TIPS ================
- Pastikan kondisi unit
"""},

{"judul": "Roda",
"detail": """================ TYRE ================
1. Gunakan tyre cage.
2. Jaga jarak.
3. Gunakan pressure gauge.

================ TIPS ================
- Pastikan tekanan sesuai
"""},

{"judul": "Tebing",
"detail": """================ SLOPE ================
1. Pantau longsor.
2. Gunakan safety berm.
3. Hindari area bawah tebing.

================ TIPS ================
- Inspeksi rutin
"""},

{"judul": "Air",
"detail": """================ WATER ================
1. Gunakan life jacket.
2. Gunakan lifebuoy.
3. Tidak bekerja sendiri.

================ TIPS ================
- Pastikan aman
"""},

{"judul": "Bahan kimia",
"detail": """================ CHEMICAL ================
1. Gunakan MSDS.
2. Gunakan APD.
3. Ikuti SOP.

================ TIPS ================
- Jangan panik saat darurat
"""},
]

KV = '''
ScreenManager:
    MenuScreen:
    DetailScreen:

<MenuScreen>:
    name: "menu"

    ScrollView:
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height

            Label:
                text: "13 MAJOR HAZARD"
                font_size: 28
                size_hint_y: None
                height: 80

            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                id: hazard_list

            Button:
                text: "Keluar"
                size_hint_y: None
                height: 60
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
