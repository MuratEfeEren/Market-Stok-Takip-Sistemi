import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
import io
import hashlib
import random
from datetime import datetime
from tkinter import filedialog
import os
from turtle import left  


CSV_DATA = """barkod_no,urun_adi,fiyat,stok_adedi
8690277460824,Yarım Yağlı Süt 1L,31.66,27
8690482474896,Tam Yağlı Süt 1L,36.9,135
8690772237702,Süzme Peynir 500g,107.48,104
8690876425522,Beyaz Peynir 1kg,253.86,72
8690647704458,Kaşar Peyniri 500g,155.25,135
8690491502794,Yoğurt 2kg,80.68,177
8690688789996,Süzme Yoğurt 900g,76.9,145
8690652248033,Ayran 1.5L,46.03,40
8690229864764,Tereyağı 500g,186.45,86
8690537923674,Yumurta 30'lu,132.72,65
8690144390871,Pilavlık Pirinç 1kg,77.39,27
8690260477755,Kırmızı Mercimek 1kg,53.54,67
8690241052734,Nohut 1kg,57.02,36
8690132756422,Pilavlık Bulgur 1kg,38.75,169
8690218672364,Kuru Fasulye 1kg,80.13,77
8690844533678,Çubuk Makarna 500g,16.17,125
8690169607219,Burgu Makarna 500g,23.35,80
8690210399976,Boncuk Makarna 500g,22.24,131
8690943357899,Ayçiçek Yağı 5L,231.92,117
8690641931692,Zeytinyağı Sızma 1L,369.13,114
8690827930207,Toz Şeker 5kg,178.48,65
8690871199322,Küp Şeker 1kg,42.87,21
8690490716820,Buğday Unu 5kg,111.41,88
8690105043567,Siyah Çay 1kg,174.5,168
8690107040491,Türk Kahvesi 100g,37.07,80
8690642843342,Granül Kahve 200g,149.47,121
8690421340831,Domates Salçası 830g,40.41,47
8690656215247,Siyah Zeytin 1kg,171.1,148
8690668178551,Yeşil Zeytin 400g,73.65,172
8690223015144,Çiçek Balı 850g,198.85,24
8690543265279,Çilek Reçeli 380g,48.97,128
8690137248111,Kakaolu Fındık Kreması 700g,135.17,177
8690251926761,Fıstık Ezmesi 350g,109.39,130
8690342038708,Gofret Çikolatalı,14.5,25
8690797286805,Sütlü Çikolata 80g,28.91,105
8690998302948,Bitter Çikolata 80g,31.48,34
8690684915180,Patates Cipsi Klasik,43.95,57
8690595800884,Mısır Cipsi Peynirli,37.32,26
8690519098752,Tuzlu Fıstık 200g,68.6,38
8690188389207,Karışık Kuruyemiş 150g,75.5,80
8690923856897,Kremalı Bisküvi 3'lü,36.97,159
8690297164019,Pötibör Bisküvi 1kg,57.26,104
8690386092203,Tuzlu Kraker,12.65,71
8690166965831,Kek Kakaolu,15.58,15
8690462758073,Coca-Cola 2.5L,57.0,110
8690127847042,Fanta 2.5L,59.83,50
8690289450865,Sprite 2L,54.49,15
8690573900717,Soğuk Çay Şeftali 1.5L,46.77,81
8690471600226,Meyve Suyu Karışık 1L,39.51,29
8690706549781,Meyve Suyu Vişne 1L,39.05,94
8690282289337,Maden Suyu 6'lı,40.0,175
8690900410801,Meyveli Maden Suyu 6'lı,52.93,101
8690606714584,Doğal Kaynak Suyu 5L,25.1,151
8690653850350,Doğal Kaynak Suyu 1.5L,13.08,120
8690207251078,Şalgam Suyu Acılı 1L,25.41,110
8690953430109,Toz Çamaşır Deterjanı 10kg,371.21,107
8690770854574,Sıvı Çamaşır Deterjanı 3L,154.61,14
8690215528584,Yumuşatıcı 5L,107.41,111
8690492249256,Çamaşır Suyu 4L,71.67,73
8690645453509,Bulaşık Makinesi Tableti 50'li,224.9,53
8690610468723,Elde Bulaşık Deterjanı 1L,42.82,136
8690816096277,Yüzey Temizleyici 2.5L,64.33,73
8690195283981,Cam Temizleyici 750ml,44.96,162
8690762534176,Sıvı Sabun 4L,94.71,49
8690655570271,Katı Sabun 4'lü,47.76,177
8690198083255,Şampuan 500ml,96.32,13
8690299177755,Saç Kremi 400ml,92.24,133
8690631703894,Duş Jeli 500ml,60.94,70
8690947823768,Diş Macunu 75ml,107.1,116
8690899965034,Diş Fırçası,72.71,82
8690227264382,Deodorant Sprey 150ml,119.33,120
8690175036160,Tuvalet Kağıdı 32'li,211.43,25
8690155445522,Kağıt Havlu 12'li,102.87,104
8690623794199,Peçete 100'lü,24.98,80
8690514632031,Islak Mendil 90'lı,30.04,114
8690862972945,Bebek Bezi No:4 60'lı,341.24,166
8690991825176,Bebek Şampuanı 500ml,74.99,106
8690805301120,Tıraş Bıçağı 3'lü,60.53,52
8690125800953,Tıraş Köpüğü 200ml,56.2,15
8690536068750,Sıvı Krem Temizleyici 750ml,38.42,62
8690216596285,Mayonez 600g,64.53,85
8690684144656,Ketçap 650g,64.65,124
8690124910014,Pul Biber 250g,57.04,75
8690831294602,Karabiber 100g,65.65,75
8690857747395,Kimyon 100g,58.86,12
8690915366382,Kuru Nane 100g,39.59,99
8690934284682,Tuz 750g,17.24,127
8690509267098,Elma Sirkesi 500ml,28.71,165
8690106723847,Limon Suyu 500ml,19.38,153
8690397016709,Kornişon Turşu 680g,64.68,73
8690336367422,Ton Balığı Konservesi 2x160g,109.21,179
8690666013396,Mısır Konservesi 3'lü,52.74,22
8690557975832,Hazır Çorba Mercimek,13.44,159
8690335898277,Hazır Çorba Ezogelin,17.83,24
8690117697202,Müsli/Yulaf Ezmesi 500g,49.98,109
8690721504665,Corn Flakes 500g,62.68,25
8690759867037,Tahin 600g,126.57,68
8690693261965,Pekmez 700g,111.78,109
8690930371258,Labne Peyniri 400g,74.74,106
8690611042366,Krem Peynir 300g,67.94,65"""


COLORS = {
    "bg_dark":      "#0F172A",
    "bg_card":      "#1E293B",
    "bg_sidebar":   "#1E293B",
    "accent":       "#6366F1",
    "accent_hover": "#4F46E5",
    "accent2":      "#10B981",
    "danger":       "#EF4444",
    "warning":      "#F59E0B",
    "text_primary": "#F1F5F9",
    "text_secondary":"#94A3B8",
    "border":       "#334155",
    "row_even":     "#1E293B",
    "row_odd":      "#263348",
    "critical":     "#7F1D1D",
    "critical_fg":  "#FCA5A5",
    "header_bg":    "#312E81",
}

FONTS = {
    "title":    ("Segoe UI", 22, "bold"),
    "subtitle": ("Segoe UI", 14, "bold"),
    "body":     ("Segoe UI", 11),
    "small":    ("Segoe UI", 9),
    "mono":     ("Consolas", 10),
    "btn":      ("Segoe UI", 10, "bold"),
    "badge":    ("Segoe UI", 9, "bold"),
}

CRITICAL_LIMIT = 20


class DataStore:
    def __init__(self):
        self.products: dict[str, dict] = {}
        self.sales: list[dict] = []
        self.users = {
            "admin":   {"password": self._hash("123"),  "role": "admin"},
            "kasiyer": {"password": self._hash("123"), "role": "kasiyer"},
        }
        self.products_file = "urunler.csv"
        self.sales_file = "satislar.csv"
        self._load_data()

    def _hash(self, pw: str) -> str:
        return hashlib.sha256(pw.encode()).hexdigest()

    def verify(self, username: str, password: str):
        u = self.users.get(username)
        if u and u["password"] == self._hash(password):
            return u["role"]
        return None

    def _load_data(self):

        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, mode="r", encoding="utf-8-sig") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        barkod = row["barkod_no"].strip()
                        self.products[barkod] = {
                            "barkod":  barkod,
                            "ad":      row["urun_adi"].strip(),
                            "fiyat":   float(row["fiyat"]),
                            "stok":    int(row["stok_adedi"]),
                        }
            except Exception:
                self._load_default_csv()
        else:
            self._load_default_csv()

        
        if os.path.exists(self.sales_file):
            try:
                with open(self.sales_file, mode="r", encoding="utf-8-sig") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.sales.append({
                            "tarih":  row["tarih"],
                            "barkod": row["barkod"],
                            "ad":     row["urun_adi"],
                            "adet":   int(row["adet"]),
                            "fiyat":  float(row["fiyat"]),
                            "toplam": float(row["toplam"]),
                        })
            except Exception:
                pass

    def _load_default_csv(self):
        reader = csv.DictReader(io.StringIO(CSV_DATA))
        for row in reader:
            barkod = row["barkod_no"].strip()
            self.products[barkod] = {
                "barkod":  barkod,
                "ad":      row["urun_adi"].strip(),
                "fiyat":   float(row["fiyat"]),
                "stok":    int(row["stok_adedi"]),
            }

    def save_data(self):
        """Tüm verileri yerel CSV dosyalarına güvenli bir şekilde yazar."""
        try:
           
            with open(self.products_file, mode="w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["barkod_no", "urun_adi", "fiyat", "stok_adedi"])
                for p in self.products.values():
                    writer.writerow([p["barkod"], p["ad"], p["fiyat"], p["stok"]])
            

            with open(self.sales_file, mode="w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerow(["tarih", "barkod", "urun_adi", "adet", "fiyat", "toplam"])
                for s in self.sales:
                    writer.writerow([s["tarih"], s["barkod"], s["ad"], s["adet"], s["fiyat"], s["toplam"]])
        except Exception as e:
            print(f"Veriler disk üzerine yazılırken bir hata oluştu: {e}")

   
    def get_all(self) -> list[dict]:
        return list(self.products.values())

    def add(self, barkod, ad, fiyat, stok) -> str:
        if barkod in self.products:
            return "Bu barkod zaten mevcut!"
        self.products[barkod] = {"barkod": barkod, "ad": ad,
                                  "fiyat": float(fiyat), "stok": int(stok)}
        return "ok"

    def update(self, barkod, ad, fiyat, stok) -> str:
        if barkod not in self.products:
            return "Ürün bulunamadı!"
        self.products[barkod].update({"ad": ad, "fiyat": float(fiyat), "stok": int(stok)})
        return "ok"

    def delete(self, barkod) -> str:
        if barkod not in self.products:
            return "Ürün bulunamadı!"
        del self.products[barkod]
        return "ok"

    def sell(self, barkod, adet) -> str:
        p = self.products.get(barkod)
        if not p:
            return "Ürün bulunamadı!"
        if p["stok"] < adet:
            return f"Yetersiz stok! Mevcut: {p['stok']}"
        p["stok"] -= adet 
        self.sales.append({
            "tarih":  datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "barkod": barkod,
            "ad":     p["ad"],
            "adet":   adet,
            "fiyat":  p["fiyat"],
            "toplam": round(p["fiyat"] * adet, 2),
        })
        return "ok"

    def total_revenue(self) -> float:
        return round(sum(s["toplam"] for s in self.sales), 2)

    def critical_stock(self) -> list[dict]:
        return [p for p in self.products.values() if p["stok"] < CRITICAL_LIMIT]



class LoginScreen(tk.Toplevel):
    def __init__(self, master, store: DataStore, on_success):
        super().__init__(master)
        self.store = store
        self.on_success = on_success
        self.title("Market Stok Takip — Giriş")
        self.configure(bg=COLORS["bg_dark"])
        self.resizable(False, False)
        self._center(420, 520)
        self._build()
        self.grab_set()

    def _center(self, w, h):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    def _build(self):
        top = tk.Frame(self, bg=COLORS["accent"], height=130)
        top.pack(fill="x")
        tk.Label(top, text="🛒", font=("Segoe UI Emoji", 36),
                 bg=COLORS["accent"], fg="white").pack(pady=(22, 4))
        tk.Label(top, text="Market Stok Takip", font=FONTS["title"],
                 bg=COLORS["accent"], fg="white").pack()

        card = tk.Frame(self, bg=COLORS["bg_card"], padx=36, pady=30)
        card.pack(fill="both", expand=True, padx=30, pady=24)

        tk.Label(card, text="Kullanıcı Adı", font=FONTS["body"],
                 bg=COLORS["bg_card"], fg=COLORS["text_secondary"]).pack(anchor="w")
        self.usr_var = tk.StringVar()
        self._entry(card, self.usr_var).pack(fill="x", pady=(4, 14))

        tk.Label(card, text="Şifre", font=FONTS["body"],
                 bg=COLORS["bg_card"], fg=COLORS["text_secondary"]).pack(anchor="w")
        self.pw_var = tk.StringVar()
        self._entry(card, self.pw_var, show="●").pack(fill="x", pady=(4, 6))

        self.err_lbl = tk.Label(card, text="", font=FONTS["small"],
                                bg=COLORS["bg_card"], fg=COLORS["danger"])
        self.err_lbl.pack(anchor="w", pady=(0, 16))

        btn = tk.Button(card, text="GİRİŞ YAP", font=FONTS["btn"],
                        bg=COLORS["accent"], fg="white", relief="flat",
                        activebackground=COLORS["accent_hover"], activeforeground="white",
                        cursor="hand2", height=2, command=self._login)
        btn.pack(fill="x", ipady=4)

        hint = tk.Frame(card, bg=COLORS["bg_card"])
        hint.pack(fill="x", pady=(20, 0))
        tk.Label(hint, text="Admin: admin / admin123",
                 font=FONTS["small"], bg=COLORS["bg_card"],
                 fg=COLORS["text_secondary"]).pack(anchor="w")
        tk.Label(hint, text="Kasiyer: kasiyer / kasiyer123",
                 font=FONTS["small"], bg=COLORS["bg_card"],
                 fg=COLORS["text_secondary"]).pack(anchor="w")

        self.bind("<Return>", lambda e: self._login())

    def _entry(self, parent, var, show=None):
        e = tk.Entry(parent, textvariable=var, font=FONTS["body"],
                     bg=COLORS["bg_dark"], fg=COLORS["text_primary"],
                     insertbackground=COLORS["text_primary"],
                     relief="flat", bd=0, highlightthickness=2,
                     highlightbackground=COLORS["border"],
                     highlightcolor=COLORS["accent"])
        if show:
            e.config(show=show)
        e.pack_configure(ipady=8)
        return e

    def _login(self):
        role = self.store.verify(self.usr_var.get().strip(), self.pw_var.get())
        if role:
            self.destroy()
            self.on_success(role, self.usr_var.get().strip())
        else:
            self.err_lbl.config(text="⚠  Kullanıcı adı veya şifre hatalı!")



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()
        self.store = DataStore()
        self.role = None
        self.username = None
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self._show_login()

    def _show_login(self):
        login = LoginScreen(self, self.store, self._on_login)
        login.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _on_login(self, role, username):
        self.role = role
        self.username = username
        self.deiconify()
        self._build_main()

    def _on_closing(self):
        """Uygulama kapatılırken verileri diske kaydeder."""
        self.store.save_data()
        self.destroy()

    def _build_main(self):
        self.title(f"Market Stok Takip — {self.username.title()} ({self.role.upper()})")
        self.configure(bg=COLORS["bg_dark"])
        self.state("zoomed")

        topbar = tk.Frame(self, bg=COLORS["bg_card"], height=56)
        topbar.pack(fill="x", side="top")
        topbar.pack_propagate(False)

        tk.Label(topbar, text="🛒  Market Stok Takip",
                 font=FONTS["subtitle"], bg=COLORS["bg_card"],
                 fg=COLORS["text_primary"]).pack(side="left", padx=20, pady=12)

        self.clock_lbl = tk.Label(topbar, font=FONTS["body"],
                                   bg=COLORS["bg_card"], fg=COLORS["text_secondary"])
        self.clock_lbl.pack(side="right", padx=20)

        role_badge = tk.Label(topbar,
                              text=f"  {self.role.upper()}  ",
                              font=FONTS["badge"],
                              bg=COLORS["accent"] if self.role == "admin" else COLORS["accent2"],
                              fg="white", padx=8, pady=3)
        role_badge.pack(side="right", padx=(0, 10), pady=14)

        tk.Label(topbar, text=f"👤 {self.username}",
                 font=FONTS["body"], bg=COLORS["bg_card"],
                 fg=COLORS["text_secondary"]).pack(side="right", padx=(0, 6))

        logout_btn = tk.Button(topbar, text="Çıkış", font=FONTS["small"],
                               bg=COLORS["danger"], fg="white", relief="flat",
                               cursor="hand2", command=self._logout)
        logout_btn.pack(side="right", padx=20, pady=14)

        body = tk.Frame(self, bg=COLORS["bg_dark"])
        body.pack(fill="both", expand=True)

        sidebar = tk.Frame(body, bg=COLORS["bg_sidebar"], width=210)
        sidebar.pack(fill="y", side="left")
        sidebar.pack_propagate(False)

        self.content = tk.Frame(body, bg=COLORS["bg_dark"])
        self.content.pack(fill="both", expand=True, side="left")

        self._build_sidebar(sidebar)
        self._update_clock()

        self._show_stock()

    def _build_sidebar(self, sidebar):
        tk.Label(sidebar, text="MENÜ", font=FONTS["small"],
                 bg=COLORS["bg_sidebar"], fg=COLORS["text_secondary"],
                 pady=16).pack(fill="x", padx=16)

        menus = [("📦  Stok Takibi",    self._show_stock),
                 ("🛍  Satış Yap",       self._show_sale)]

        if self.role == "admin":
            menus += [
                ("➕  Ürün Ekle",       self._show_add),
                ("✏️  Stok Güncelle",   self._show_update),
                ("🗑  Ürün Sil",         self._show_delete),
                ("📊  Satış Raporu",    self._show_report),
                ("⚠️  Kritik Stok",     self._show_critical),
            ]

        self.sidebar_btns = []
        for label, cmd in menus:
            btn = tk.Button(sidebar, text=label, font=FONTS["body"],
                            bg=COLORS["bg_sidebar"], fg=COLORS["text_primary"],
                            activebackground=COLORS["accent"],
                            activeforeground="white",
                            relief="flat", anchor="w", padx=18, pady=12,
                            cursor="hand2", command=cmd)
            btn.pack(fill="x", pady=1)
            self.sidebar_btns.append((btn, cmd))

    def _set_active(self, active_cmd):
        for btn, cmd in self.sidebar_btns:
            btn.config(bg=COLORS["accent"] if cmd == active_cmd else COLORS["bg_sidebar"])

    def _clear_content(self):
        for w in self.content.winfo_children():
            w.destroy()

    def _page_header(self, title, subtitle=""):
        hdr = tk.Frame(self.content, bg=COLORS["bg_dark"])
        hdr.pack(fill="x", padx=28, pady=(22, 0))
        tk.Label(hdr, text=title, font=FONTS["title"],
                 bg=COLORS["bg_dark"], fg=COLORS["text_primary"]).pack(side="left")
        if subtitle:
            tk.Label(hdr, text=subtitle, font=FONTS["body"],
                     bg=COLORS["bg_dark"], fg=COLORS["text_secondary"]).pack(side="left", padx=12, pady=6)
        ttk.Separator(self.content, orient="horizontal").pack(fill="x", padx=28, pady=8)

    def _update_clock(self):
        self.clock_lbl.config(text=datetime.now().strftime("🕐  %d.%m.%Y  %H:%M:%S"))
        self.after(1000, self._update_clock)

    def _logout(self):
        if messagebox.askyesno("Çıkış", "Çıkmak istediğinize emin misiniz?"):
            self.store.save_data()
            
            for widget in self.winfo_children():
                widget.destroy()
            self.withdraw()
            
            self.role = None
            self.username = None
            self._show_login()

    
    def _make_tree(self, parent, columns, heights=18):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                        background=COLORS["row_even"],
                        foreground=COLORS["text_primary"],
                        fieldbackground=COLORS["row_even"],
                        rowheight=32,
                        font=FONTS["body"],
                        borderwidth=0)
        style.configure("Custom.Treeview.Heading",
                        background=COLORS["header_bg"],
                        foreground="white",
                        font=("Segoe UI", 10, "bold"),
                        relief="flat")
        style.map("Custom.Treeview",
                  background=[("selected", COLORS["accent"])],
                  foreground=[("selected", "white")])

        frame = tk.Frame(parent, bg=COLORS["bg_dark"])
        frame.pack(fill="both", expand=True, padx=28, pady=(0, 16))

        tree = ttk.Treeview(frame, columns=columns, show="headings",
                             height=heights, style="Custom.Treeview")

        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

        tree.tag_configure("odd",      background=COLORS["row_odd"])
        tree.tag_configure("even",     background=COLORS["row_even"])
        tree.tag_configure("critical", background=COLORS["critical"],
                           foreground=COLORS["critical_fg"])

        return tree

    
    def _make_search(self, parent, placeholder, on_change):
        frame = tk.Frame(parent, bg=COLORS["bg_dark"])
        frame.pack(fill="x", padx=28, pady=(0, 10))

        tk.Label(frame, text="🔍", font=("Segoe UI Emoji", 12),
                 bg=COLORS["bg_dark"], fg=COLORS["text_secondary"]).pack(side="left")

        var = tk.StringVar()
        entry = tk.Entry(frame, textvariable=var, font=FONTS["body"],
                         bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                         insertbackground=COLORS["text_primary"],
                         relief="flat", bd=0, highlightthickness=2,
                         highlightbackground=COLORS["border"],
                         highlightcolor=COLORS["accent"])
        entry.pack(side="left", fill="x", expand=True, ipady=7, padx=(6, 0))
        entry.insert(0, placeholder)
        entry.config(fg=COLORS["text_secondary"])

        def on_focus_in(e):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(fg=COLORS["text_primary"])

        def on_focus_out(e):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg=COLORS["text_secondary"])

        entry.bind("<FocusIn>",  on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
        var.trace_add("write", lambda *a: on_change(
            var.get() if var.get() != placeholder else ""))
        return var


    def _form_row(self, parent, label, default=""):
        row = tk.Frame(parent, bg=COLORS["bg_card"])
        row.pack(fill="x", pady=5)
        tk.Label(row, text=label, font=FONTS["body"], width=22, anchor="w",
                 bg=COLORS["bg_card"], fg=COLORS["text_secondary"]).pack(side="left")
        var = tk.StringVar(value=default)
        e = tk.Entry(row, textvariable=var, font=FONTS["body"],
                     bg=COLORS["bg_dark"], fg=COLORS["text_primary"],
                     insertbackground="white", relief="flat",
                     highlightthickness=2,
                     highlightbackground=COLORS["border"],
                     highlightcolor=COLORS["accent"])
        e.pack(side="left", fill="x", expand=True, ipady=7, padx=(0, 4))
        return var

    def _action_btn(self, parent, text, color, cmd):
        b = tk.Button(parent, text=text, font=FONTS["btn"],
                      bg=color, fg="white", relief="flat",
                      activebackground=COLORS["accent_hover"],
                      activeforeground="white",
                      cursor="hand2", padx=24, pady=8, command=cmd)
        b.pack(side="left", padx=6)
        return b
    
    def show_toast(self, message, duration=2000):
        toast = tk.Toplevel(self)
        toast.overrideredirect(True) 
        toast.configure(bg=COLORS["accent2"]) 
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        toast_width = 300
        toast_height = 45
        x = screen_width - toast_width - 500
        y = screen_height - toast_height - 120
        toast.geometry(f"{toast_width}x{toast_height}+{x}+{y}")
        
        lbl = tk.Label(toast, text=message, font=FONTS["body"], 
                       bg=COLORS["accent2"], fg="white", anchor="center")
        lbl.pack(fill="both", expand=True, padx=10)
        
        toast.after(duration, toast.destroy)

  
    def _show_stock(self):
        self._clear_content()
        self._set_active(self._show_stock)
        self._page_header("📦  Stok Takibi",
                          f"Toplam {len(self.store.products)} ürün")

        cols = ("Barkod", "Ürün Adı", "Fiyat (₺)", "Stok", "Durum")
        search_var = self._make_search(self.content,
                                       "Ürün adı veya barkod ile ara...",
                                       lambda q: self._populate_stock(tree, q))
        
       
        action_frame = tk.Frame(self.content, bg=COLORS["bg_dark"])
        action_frame.pack(fill="x", padx=28, pady=(0, 10))
        tk.Button(action_frame, text="📥 Excel / CSV Olarak Aktar", font=FONTS["small"],
                  bg=COLORS["accent2"], fg="white", relief="flat", cursor="hand2",
                  padx=12, pady=6, command=self._export_to_csv).pack(side="left")

        tree = self._make_tree(self.content, cols)
        for c, w in zip(cols, [160, 280, 110, 90, 110]):
            tree.heading(c, text=c,
                         command=lambda col=c: self._sort_tree(tree, col, cols))
            tree.column(c, width=w, anchor="center" if c not in ("Ürün Adı",) else "w")

        self._populate_stock(tree, "")

        def on_double_click(event):
            selected_item = tree.selection()
            if selected_item:
                barcode = tree.item(selected_item[0], "values")[0]
                product_name = tree.item(selected_item[0], "values")[1]
                
                self.clipboard_clear()
                self.clipboard_append(barcode)
                
                self.show_toast(f"📋 {product_name} barkodu kopyalandı!")

        tree.bind("<Double-1>", on_double_click)

    def _populate_stock(self, tree, query=""):
        tree.delete(*tree.get_children())
        if not hasattr(self, '_tree_original_order'):
            self._tree_original_order = {}
        self._tree_original_order[tree] = []

        products = self.store.get_all()
        if query:
            q = query.lower()
            products = [p for p in products
                        if q in p["ad"].lower() or q in p["barkod"]]
        for i, p in enumerate(products):
            tag = "critical" if p["stok"] < CRITICAL_LIMIT else ("odd" if i % 2 else "even")
            durum = "⚠ KRİTİK" if p["stok"] < CRITICAL_LIMIT else ("✔ Normal" if p["stok"] > 50 else "⚡ Az")
            item_id = tree.insert("", "end", values=(
                p["barkod"], p["ad"],
                f"{p['fiyat']:.2f} ₺", p["stok"], durum
            ), tags=(tag,))
            self._tree_original_order[tree].append(item_id)

    def _sort_tree(self, tree, col, all_cols):
        if not hasattr(self, '_sort_dir'):
            self._sort_dir = {}
        
        current_dir = self._sort_dir.get(col, None)
        
        if current_dir is None:
            next_dir = 'asc'
        elif current_dir == 'asc':
            next_dir = 'desc'
        else:
            next_dir = 'original'
            
        self._sort_dir = {col: next_dir}
        
        if next_dir == 'original':
            if hasattr(self, '_tree_original_order') and tree in self._tree_original_order:
                for idx, item_id in enumerate(self._tree_original_order[tree]):
                    if tree.exists(item_id):
                        tree.move(item_id, "", idx)
            self._sort_dir[col] = None  
            return

        items = [(tree.set(k, col), k) for k in tree.get_children("")]
        
        def sort_key(x):
            val = x[0].replace(" ₺", "").replace(",", ".").strip()
            try:
                return float(val)
            except ValueError:
                return val

        items.sort(key=sort_key, reverse=(next_dir == 'desc'))
        for idx, (_, k) in enumerate(items):
            tree.move(k, "", idx)

    def _export_to_csv(self):
        """GİRİNTİ HATASI DÜZELTİLDİ: Artık _sort_tree'den bağımsız temiz bir App metodu."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Dosyası", "*.csv"), ("Tüm Dosyalar", "*.*")],
            title="Stok Listesini Excel/CSV Olarak Aktar",
            initialfile=f"stok_listesi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )
        if not file_path:
            return
        
        try:
            products = self.store.get_all()
            with open(file_path, mode="w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f, delimiter=";")
                writer.writerow(["Barkod No", "Ürün Adı", "Fiyat", "Stok Adedi"])
                for p in products:
                    writer.writerow([p["barkod"], p["ad"], f"{p['fiyat']:.2f}", p["stok"]])
            
            messagebox.showinfo("Başarılı", "Bütün stok listesi başarıyla CSV dosyası olarak aktarıldı!")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken bir hata oluştu:\n{e}")

   
    def _show_sale(self):
        self._clear_content()
        self._set_active(self._show_sale)
        self._page_header("🛍  Satış Yap")

        main = tk.Frame(self.content, bg=COLORS["bg_dark"])
        main.pack(fill="both", expand=True, padx=28, pady=8)

        left = tk.Frame(main, bg=COLORS["bg_card"], padx=28, pady=24,
                        relief="flat", bd=0, highlightthickness=1,
                        highlightbackground=COLORS["border"])
        left.pack(side="left", fill="y", padx=(0, 16))

        tk.Label(left, text="Satış Formu", font=FONTS["subtitle"],
                 bg=COLORS["bg_card"], fg=COLORS["text_primary"]).pack(anchor="w", pady=(0, 16))

        barkod_row = tk.Frame(left, bg=COLORS["bg_card"])
        barkod_row.pack(fill="x", pady=5)
        tk.Label(barkod_row, text="Barkod No", font=FONTS["body"], width=22, anchor="w",
                 bg=COLORS["bg_card"], fg=COLORS["text_secondary"]).pack(side="left")
        barkod_var = tk.StringVar()
        tk.Entry(barkod_row, textvariable=barkod_var, font=FONTS["body"],
                 bg=COLORS["bg_dark"], fg=COLORS["text_primary"],
                 insertbackground="white", relief="flat",
                 highlightthickness=2,
                 highlightbackground=COLORS["border"],
                 highlightcolor=COLORS["accent"]).pack(side="left", fill="x", expand=True,
                                                        ipady=7, padx=(0, 4))

        def pick_random_barcode():
            products = self.store.get_all()
            if not products:
                messagebox.showinfo("Bilgi", "Kayıtlı ürün bulunamadı.")
                return
            secilen = random.choice(products)
            barkod_var.set(secilen["barkod"])

        tk.Button(barkod_row, text="🎲 Barkod Okut", font=FONTS["small"],
                  bg=COLORS["warning"], fg="white", relief="flat",
                  activebackground=COLORS["accent_hover"], activeforeground="white",
                  cursor="hand2", padx=10, pady=6,
                  command=pick_random_barcode).pack(side="left")

        adet_var = self._form_row(left, "Adet", "1")

        preview = tk.Label(left, text="", font=FONTS["body"],
                           bg=COLORS["bg_card"], fg=COLORS["accent2"],
                           wraplength=280, justify="left")
        preview.pack(anchor="w", pady=8)

        def barkod_changed(*_):
            p = self.store.products.get(barkod_var.get().strip())
            if p:
                preview.config(
                    text=f"✔  {p['ad']}\n   Fiyat: {p['fiyat']:.2f} ₺   |   Stok: {p['stok']}",
                    fg=COLORS["accent2"])
            else:
                preview.config(text="Ürün bulunamadı", fg=COLORS["text_secondary"])

        barkod_var.trace_add("write", barkod_changed)

        result_lbl = tk.Label(left, text="", font=FONTS["body"],
                              bg=COLORS["bg_card"], wraplength=280)
        result_lbl.pack(anchor="w", pady=4)

        def do_sale():
            try:
                adet = int(adet_var.get())
                if adet <= 0:
                    raise ValueError
            except ValueError:
                result_lbl.config(text="Geçersiz adet!", fg=COLORS["danger"])
                return
            r = self.store.sell(barkod_var.get().strip(), adet)
            if r == "ok":
                p = self.store.products.get(barkod_var.get().strip())
                result_lbl.config(
                    text=f"✔  Satış başarılı!\n   {p['ad']}  x{adet}  = {p['fiyat']*adet:.2f} ₺",
                    fg=COLORS["accent2"])
                self._populate_sale_history(history_tree)
                barkod_changed()
            else:
                result_lbl.config(text=f"✗  {r}", fg=COLORS["danger"])

        btn_frame = tk.Frame(left, bg=COLORS["bg_card"])
        btn_frame.pack(anchor="w", pady=12)
        self._action_btn(btn_frame, "Satışı Onayla", COLORS["accent2"], do_sale)

        right = tk.Frame(main, bg=COLORS["bg_dark"])
        right.pack(side="left", fill="both", expand=True)

        tk.Label(right, text="Son Satışlar", font=FONTS["subtitle"],
                 bg=COLORS["bg_dark"], fg=COLORS["text_primary"]).pack(anchor="w", pady=(0, 8))

        delete_btn_frame = tk.Frame(right, bg=COLORS["bg_dark"])
        delete_btn_frame.pack(side="bottom", fill="x", pady=(10, 0))

        h_cols = ("Tarih", "Ürün Adı", "Adet", "Birim ₺", "Toplam ₺")
        history_tree = ttk.Treeview(right, columns=h_cols, show="headings",
                                    height=22, style="Custom.Treeview")
        for c, w in zip(h_cols, [160, 240, 60, 90, 100]):
            history_tree.heading(c, text=c)
            history_tree.column(c, width=w, anchor="center")
        sb = ttk.Scrollbar(right, orient="vertical", command=history_tree.yview)
        history_tree.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        history_tree.pack(fill="both", expand=True)

        self.del_sale_btn = tk.Button(delete_btn_frame, text="🗑️ Seçili Satışı Sil (Stok İade Et)", font=FONTS["btn"],
                                      bg=COLORS["danger"], fg="white", relief="flat",
                                      cursor="hand2", padx=20, pady=6, 
                                      command=lambda: do_delete_sale(history_tree))

        def on_sale_select(event):
            if history_tree.selection():
                self.del_sale_btn.pack(side="right")
            else:
                self.del_sale_btn.pack_forget()

        history_tree.bind("<<TreeviewSelect>>", on_sale_select)

        def do_delete_sale(tree):
            sel = tree.selection()
            if not sel:
                return
            iid = sel[0]
            idx = int(iid.split("_")[1])
            
            if messagebox.askyesno("Satış İptali", "Bu satışı silmek ve ilgili stoğu iade etmek istediğinize emin misiniz?"):
                sale = self.store.sales[idx]
                if sale["barkod"] in self.store.products:
                    self.store.products[sale["barkod"]]["stok"] += sale["adet"]
                
                del self.store.sales[idx]
                messagebox.showinfo("Başarılı", "Satış kaydı silindi ve ürün stoğu güncellendi.")
                self.del_sale_btn.pack_forget()
                self._populate_sale_history(tree)
                barkod_changed() 

        self._populate_sale_history(history_tree)

    def _populate_sale_history(self, tree):
        tree.delete(*tree.get_children())
        start_idx = max(0, len(self.store.sales) - 50)
        for i, idx in enumerate(reversed(range(start_idx, len(self.store.sales)))):
            s = self.store.sales[idx]
            tag = "odd" if i % 2 else "even"
            tree.insert("", "end", iid=f"sale_{idx}", values=(
                s["tarih"], s["ad"], s["adet"],
                f"{s['fiyat']:.2f} ₺", f"{s['toplam']:.2f} ₺"
            ), tags=(tag,))

    
    def _show_add(self):
        self._clear_content()
        self._set_active(self._show_add)
        self._page_header("➕  Yeni Ürün Ekle")

        card = tk.Frame(self.content, bg=COLORS["bg_card"], padx=36, pady=28,
                        highlightthickness=1, highlightbackground=COLORS["border"])
        card.pack(padx=80, pady=20, anchor="n")

        barkod = self._form_row(card, "Barkod No *")
        ad     = self._form_row(card, "Ürün Adı *")
        fiyat  = self._form_row(card, "Fiyat (₺) *")
        stok   = self._form_row(card, "Stok Adedi *")

        msg = tk.Label(card, text="", font=FONTS["body"],
                       bg=COLORS["bg_card"], wraplength=380)
        msg.pack(anchor="w", pady=8)

        def submit():
           
            try:
                f = float(fiyat.get().replace(",", "."))
                s = int(stok.get())
                b= int(barkod.get())
            except ValueError:
                msg.config(text="Barkod,fiyat ve stok sayısal olmalıdır!", fg=COLORS["danger"])
                return
            
            r = self.store.add(barkod.get().strip(), ad.get().strip(), f, s)
            if r == "ok":
                msg.config(text=f"✔  '{ad.get()}' başarıyla eklendi.", fg=COLORS["accent2"])
                for v in (barkod, ad, fiyat, stok):
                    v.set("")
            else:
                msg.config(text=f"✗  {r}", fg=COLORS["danger"])

        btn_f = tk.Frame(card, bg=COLORS["bg_card"])
        btn_f.pack(anchor="w", pady=6)
        self._action_btn(btn_f, "Ürünü Kaydet", COLORS["accent"], submit)

   
    def _show_update(self):
        self._clear_content()
        self._set_active(self._show_update)
        self._page_header("✏️  Stok & Ürün Güncelle")

        top = tk.Frame(self.content, bg=COLORS["bg_dark"])
        top.pack(fill="x", padx=28, pady=(0, 8))

        tk.Label(top, text="Barkod ile ara:", font=FONTS["body"],
                 bg=COLORS["bg_dark"], fg=COLORS["text_secondary"]).pack(side="left")
        search_var = tk.StringVar()
        se = tk.Entry(top, textvariable=search_var, font=FONTS["body"],
                      bg=COLORS["bg_card"], fg=COLORS["text_primary"],
                      insertbackground="white", relief="flat",  
                      highlightthickness=2,
                      highlightbackground=COLORS["border"],
                      highlightcolor=COLORS["accent"],
                      width=30)
        se.pack(side="left", ipady=7, padx=10)

        card = tk.Frame(self.content, bg=COLORS["bg_card"], padx=36, pady=24,
                        highlightthickness=1, highlightbackground=COLORS["border"])
        card.pack(padx=80, pady=50, anchor="n")

        barkod_v = self._form_row(card, "Barkod No")
        ad_v     = self._form_row(card, "Ürün Adı")
        fiyat_v  = self._form_row(card, "Fiyat (₺)")
        stok_v   = self._form_row(card, "Stok Adedi")

        msg = tk.Label(card, text="Barkod girin ve 'Yükle' butonuna basın.",
                       font=FONTS["body"], bg=COLORS["bg_card"],
                       fg=COLORS["text_secondary"], wraplength=400)
        msg.pack(anchor="w", pady=8)
        

        def load():
            barkod = search_var.get().strip()
            p = self.store.products.get(barkod)
            if not p:
                msg.config(text="Ürün bulunamadı!", fg=COLORS["danger"])
                return
            barkod_v.set(p["barkod"])
            ad_v.set(p["ad"])
            fiyat_v.set(str(p["fiyat"]))
            stok_v.set(str(p["stok"]))
            msg.config(text="Ürün yüklendi. Düzenleyip kaydedin.", fg=COLORS["accent2"])

        def save():
            try:
                f = float(fiyat_v.get().replace(",", "."))
                s = int(stok_v.get())
            except ValueError:
                msg.config(text="Fiyat ve stok sayısal olmalıdır!", fg=COLORS["danger"])
                return
            r = self.store.update(barkod_v.get().strip(), ad_v.get().strip(), f, s)
            if r == "ok":
                msg.config(text="✔  Ürün başarıyla güncellendi.", fg=COLORS["accent2"])
            else:
                msg.config(text=f"✗  {r}", fg=COLORS["danger"])

    
        def pick_random_barcode():
            barkod = search_var.get().strip()
            products = self.store.get_all()
            if not products:
                messagebox.showinfo("Bilgi", "Kayıtlı ürün bulunamadı.")
                return
            secilen = random.choice(products)
            barkod.set(secilen["barkod"])        

        btn_row = tk.Frame(top, bg=COLORS["bg_dark"])
        btn_row.pack(side="left")
        self._action_btn(btn_row, "Yükle", COLORS["accent"], load)
        self._action_btn(btn_row, "Barkod Okut", COLORS["accent"], pick_random_barcode)

        btn_f = tk.Frame(card, bg=COLORS["bg_card"])
        btn_f.pack(anchor="w", pady=6)
        self._action_btn(btn_f, "Değişiklikleri Kaydet", COLORS["accent2"], save)
        

   
    def _show_delete(self):
        self._clear_content()
        self._set_active(self._show_delete)
        self._page_header("🗑  Ürün Sil")

        cols = ("Barkod", "Ürün Adı", "Fiyat (₺)", "Stok")

        msg = tk.Label(self.content, text="", font=FONTS["body"],
                       bg=COLORS["bg_dark"], fg=COLORS["danger"])
        msg.pack(side="bottom", anchor="w", padx=28, pady=(0, 14))

        btn_f = tk.Frame(self.content, bg=COLORS["bg_dark"])
        btn_f.pack(side="bottom", anchor="w", padx=28, pady=4)

        search_var = self._make_search(self.content,
                                       "Silmek istediğiniz ürünü arayın...",
                                       lambda q: self._populate_del(tree, q))
        tree = self._make_tree(self.content, cols, heights=15)
        for c, w in zip(cols, [160, 320, 110, 90]):
            tree.heading(c, text=c)
            tree.column(c, width=w, anchor="w" if c == "Ürün Adı" else "center")

        self._populate_del(tree, "")

        def delete_sel():
            sel = tree.selection()
            if not sel:
                msg.config(text="Lütfen silinecek ürünü seçin.", fg=COLORS["warning"])
                return
            barkod = tree.item(sel[0])["values"][0]
            ad     = tree.item(sel[0])["values"][1]
            if messagebox.askyesno("Sil", f"'{ad}' ürününü silmek istiyor musunuz?"):
                r = self.store.delete(str(barkod))
                if r == "ok":
                    msg.config(text=f"✔  '{ad}' silindi.", fg=COLORS["accent2"])
                    self._populate_del(tree, "")
                else:
                    msg.config(text=f"✗  {r}", fg=COLORS["danger"])

        self._action_btn(btn_f, "🗑  Seçili Ürünü Sil", COLORS["danger"], delete_sel)

    def _populate_del(self, tree, query):
        tree.delete(*tree.get_children())
        products = self.store.get_all()
        if query:
            q = query.lower()
            products = [p for p in products
                        if q in p["ad"].lower() or q in p["barkod"]]
        for i, p in enumerate(products):
            tag = "odd" if i % 2 else "even"
            tree.insert("", "end", values=(
                p["barkod"], p["ad"], f"{p['fiyat']:.2f} ₺", p["stok"]
            ), tags=(tag,))

    
    def _show_report(self):
        self._clear_content()
        self._set_active(self._show_report)
        self._page_header("📊  Satış Raporu")

        summary = tk.Frame(self.content, bg=COLORS["bg_dark"])
        summary.pack(fill="x", padx=28, pady=(0, 16))

        total_rev  = self.store.total_revenue()
        total_sale = len(self.store.sales)
        total_qty  = sum(s["adet"] for s in self.store.sales)

        for title, val, color in [
            ("💰  Toplam Ciro",   f"{total_rev:,.2f} ₺", COLORS["accent"]),
            ("🧾  Toplam İşlem",  str(total_sale),         COLORS["accent2"]),
            ("📦  Satılan Adet",  str(total_qty),           COLORS["warning"]),
        ]:
            c = tk.Frame(summary, bg=color, padx=24, pady=16)
            c.pack(side="left", padx=(0, 14))
            tk.Label(c, text=title, font=FONTS["body"],
                     bg=color, fg="white").pack(anchor="w")
            tk.Label(c, text=val, font=("Segoe UI", 20, "bold"),
                     bg=color, fg="white").pack(anchor="w")

        cols = ("Tarih", "Barkod", "Ürün Adı", "Adet", "Birim ₺", "Toplam ₺")
        tree = self._make_tree(self.content, cols, heights=16)
        for c, w in zip(cols, [155, 145, 240, 60, 90, 100]):
            tree.heading(c, text=c)
            tree.column(c, width=w,
                        anchor="w" if c == "Ürün Adı" else "center")

        for i, s in enumerate(reversed(self.store.sales)):
            tag = "odd" if i % 2 else "even"
            tree.insert("", "end", values=(
                s["tarih"], s["barkod"], s["ad"], s["adet"],
                f"{s['fiyat']:.2f} ₺", f"{s['toplam']:.2f} ₺"
            ), tags=(tag,))

   
    def _show_critical(self):
        self._clear_content()
        self._set_active(self._show_critical)
        criticals = self.store.critical_stock()
        self._page_header("⚠️  Kritik Stok",
                          f"Stok < {CRITICAL_LIMIT} olan {len(criticals)} ürün")

        if not criticals:
            tk.Label(self.content,
                     text="✅  Tüm ürünlerin stoğu yeterli düzeyde.",
                     font=FONTS["subtitle"],
                     bg=COLORS["bg_dark"], fg=COLORS["accent2"]).pack(pady=60)
            return

        cols = ("Barkod", "Ürün Adı", "Fiyat (₺)", "Stok", "Eksik")
        tree = self._make_tree(self.content, cols, heights=len(criticals) + 2)
        for c, w in zip(cols, [160, 300, 110, 80, 80]):
            tree.heading(c, text=c)
            tree.column(c, width=w, anchor="w" if c == "Ürün Adı" else "center")

        for p in sorted(criticals, key=lambda x: x["stok"]):
            tree.insert("", "end", values=(
                p["barkod"], p["ad"],
                f"{p['fiyat']:.2f} ₺", p["stok"],
                CRITICAL_LIMIT - p["stok"]
            ), tags=("critical",))



if __name__ == "__main__":
    app = App()
    app.mainloop()