"""Nyoms Vegetasi Pantai — panduan interaktif mangrove Indonesia."""
from __future__ import annotations
import os
import sys
import tkinter as tk
from dataclasses import dataclass
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageOps, ImageStat, ImageTk

TRAITS = {
 "akar_tunjang":"Akar tunjang/akar udara besar dari batang",
 "akar_pensil":"Akar napas seperti pensil/asparagus",
 "akar_kerucut":"Akar napas kerucut dari tanah",
 "akar_papan":"Akar lutut atau akar papan melebar",
 "daun_kelapa":"Daun menyirip panjang seperti kelapa",
 "bawah_pucat":"Bawah daun sangat pucat/keabu-abuan",
 "propagul":"Kecambah/buah memanjang seperti pensil",
 "buah_bulat":"Buah bulat seperti bola",
 "buah_puzzle":"Buah besar seperti kelapa/bola berkayu",
 "bunga_merah":"Bunga atau benang sari dominan merah",
 "bunga_putih":"Bunga/benang sari dominan putih",
 "pasir_karang":"Lokasi pantai berpasir, batu, atau karang",
 "muara":"Lokasi muara/sungai pasang surut/payau",
 "lumpur":"Lumpur dalam, halus, sering tergenang",
}

@dataclass(frozen=True)
class Species:
 name:str; local:str; traits:tuple[str,...]; detail:str

def info(local, daun, bunga_buah, akar, habitat, pembeda, manfaat):
 return ("NAMA SETEMPAT\n"+local+"\n\nCIRI DAUN\n"+daun+"\n\nBUNGA DAN BUAH\n"+bunga_buah+
 "\n\nAKAR\n"+akar+"\n\nHABITAT DAN EKOLOGI\n"+habitat+"\n\nPEMBEDA LAPANGAN\n"+pembeda+
 "\n\nMANFAAT YANG DICATAT PEDOMAN\n"+manfaat+
 "\n\nSumber: Noor, Khazali & Suryadiputra, Panduan Pengenalan Mangrove di Indonesia (1999; cetak ulang 2006).")

SPECIES=(
 Species("Avicennia alba","Api-api, mangi-mangi putih",("akar_pensil","bawah_pucat","pasir_karang"),
  info("Api-api, mangi-mangi putih","Sederhana berlawanan; atas hijau mengilap, bawah pucat; lanset hingga elips.","Bunga kuning dalam bulir; buah hijau muda kekuningan mirip kerucut/cabai.","Akar napas tipis seperti jari/asparagus.","Pionir di rawa terlindung, tepi sungai asin, dan garis pantai; membantu mengikat sedimen.","Daun lebih lanset dan buah lebih besar daripada A. marina.","Kayu bakar/bangunan mutu rendah; buah dapat dimakan.")),
 Species("Avicennia marina","Api-api putih, pejapi, nyapi",("akar_pensil","bawah_pucat","buah_bulat"),
  info("Api-api putih, pejapi, nyapi","Daun elips hingga bulat telur terbalik; bawah putih–abu muda, atas berbintik kelenjar.","Bunga kuning pucat–jingga; buah kecil hijau keabu-abuan, bertepung, berujung seperti paruh.","Akar napas tegak seperti pensil/asparagus.","Pionir pantai terlindung; toleran beragam habitat pasang-surut dan asin.","Cari bawah daun abu-putih dan buah kecil berparuh.","Kayu untuk kertas; buah dapat dimakan.")),
 Species("Bruguiera gymnorrhiza","Tancang, tumu, lindur, putut",("akar_papan","propagul","bunga_merah","muara"),
  info("Tancang, tumu, lindur, putut","Daun berkulit berlawanan, elips; bawah hijau kekuningan, kadang berbintik hitam.","Bunga besar menggantung, kelopak merah; propagul lurus tumpul hijau tua keunguan, 12–30 cm.","Akar papan di pangkal dan akar lutut.","Hutan mangrove tinggi, salinitas rendah, tepi daratan/tambak/sungai payau.","Bunga merah menggantung bersama akar lutut sangat khas.","Hipokotil dapat diolah sebagai manisan; kayu untuk arang.")),
 Species("Nypa fruticans","Nipah",("daun_kelapa","buah_bulat","muara"),
  info("Nipah, tangkal daon, buyuk","Daun sangat panjang seperti kelapa, 100–120 anak daun per pelepah.","Kepala bunga betina bulat; buah coklat kaku berserat membentuk kepala sampai ±45 cm.","Batang dan akar kuat berada di bawah tanah.","Tepi atas saluran air berlumpur halus, memerlukan masukan air tawar tinggi.","Satu-satunya kandidat berdaun menyirip seperti kelapa.","Nira untuk gula/alkohol; daun untuk atap dan anyaman.")),
 Species("Rhizophora apiculata","Bakau minyak, bakau kacang",("akar_tunjang","propagul","lumpur","muara"),
  info("Bakau minyak, bakau kacang","Daun berkulit elips menyempit; bawah dan gagang daun kemerahan.","Buah seperti pir; propagul silindris berbintil 18–38 cm, leher kotiledon merah saat matang.","Akar tunjang dapat mencapai ±5 m.","Lumpur halus dalam yang tergenang saat pasang normal; pengaruh air tawar kuat.","Akar tunjang + lumpur dalam + leher propagul merah.","Kayu, arang, tanin; pelindung pematang tambak.")),
 Species("Rhizophora mucronata","Bakau hitam, bakau korap",("akar_tunjang","propagul","muara","pasir_karang"),
  info("Bakau hitam, bakau korap","Daun berkulit elips lebar hingga lonjong, umumnya lebih besar daripada R. apiculata.","Buah lonjong 5–7 cm; propagul kasar berbintil 36–70 cm dengan leher kuning.","Akar tunjang dan akar udara dari cabang bawah.","Pematang sungai/muara; lebih toleran substrat keras atau berpasir.","Propagul jauh lebih panjang dan leher kuning, bukan merah.","Kayu bakar/arang; tanin kulit untuk pewarna.")),
 Species("Rhizophora stylosa","Bakau, bako-kurap",("akar_tunjang","propagul","pasir_karang"),
  info("Bakau, bako-kurap","Daun berkulit elips lebar dengan bintik teratur di bawah daun.","Kelompok bunga 8–16; buah seperti pir; propagul 20–35 cm, leher kuning kehijauan.","Akar tunjang sampai ±3 m, akar udara dari cabang bawah.","Lumpur, pasir, batu, juga tepian pulau/karang.","Habitat karang/pasir dan kelompok bunga banyak.","Kayu bangunan, kayu bakar, arang.")),
 Species("Sonneratia alba","Pedada, perepat, pidada",("akar_kerucut","bunga_putih","buah_bulat","pasir_karang"),
  info("Pedada, perepat, pidada","Daun berkulit berlawanan, bulat telur terbalik, ujung membundar.","Bunga putih cepat rontok dengan banyak benang sari putih berpangkal kuning; buah bulat 3,5–4,5 cm.","Akar napas kerucut tumpul hingga ±25 cm.","Pionir pantai terlindung, muara/pulau; lumpur-pasir, batu, atau karang.","Bunga putih dan akar napas kerucut pendek.","Buah asam dapat dimakan; akar napas dipakai sebagai pelampung lokal.")),
 Species("Sonneratia caseolaris","Pedada merah, perepat",("akar_kerucut","bunga_merah","buah_bulat","muara","lumpur"),
  info("Pedada merah, perepat","Daun berlawanan bulat memanjang; tangkai pendek kemerahan.","Mahkota merah dan benang sari berpangkal merah; buah bulat lebih besar, 6–8 cm.","Akar napas kerucut banyak dan kuat, dapat hingga ±1 m.","Bagian kurang asin, lumpur dalam, sungai kecil pasang-surut; bukan pematang karang.","Bunga merah dan akar napas tinggi membedakannya dari S. alba.","Buah asam untuk rujak; akar napas dapat mengganti gabus.")),
 Species("Xylocarpus granatum","Niri, nyiri",("akar_papan","buah_puzzle","muara"),
  info("Niri, nyiri","Daun majemuk berlawanan, biasanya dua pasang anak daun per tangkai; ujung membundar.","Buah besar seperti kelapa, diameter 10–20 cm, berisi biji berkayu seperti teka-teki.","Akar papan melebar, berliuk dan bercelah.","Pinggir sungai pasang, tepi daratan mangrove dan payau yang tidak terlalu asin.","Buah besar berkayu 'puzzle fruit' sangat diagnostik.","Kulit kaya tanin; kayu kecil kadang untuk perahu.")),
)

ASSET_NAMES={
 "Avicennia alba":"avicennia_alba.png", "Avicennia marina":"avicennia_marina.png",
 "Bruguiera gymnorrhiza":"bruguiera_gymnorrhiza.png", "Nypa fruticans":"nypa_fruticans.png",
 "Rhizophora apiculata":"rhizophora_apiculata.png", "Rhizophora mucronata":"rhizophora_mucronata.png",
 "Rhizophora stylosa":"rhizophora_stylosa.png", "Sonneratia alba":"sonneratia_alba.png",
 "Sonneratia caseolaris":"sonneratia_caseolaris.png", "Xylocarpus granatum":"xylocarpus_granatum.png",
}

def resource_path(*parts):
 base=getattr(sys,"_MEIPASS",os.path.dirname(os.path.abspath(__file__)))
 return os.path.join(base,*parts)

def rank(selected):
 rows=[]
 for s in SPECIES:
  hits=sorted(selected.intersection(s.traits))
  if not selected:
   percent=0
  else:
   precision=len(hits)/len(selected)
   recall=len(hits)/len(s.traits)
   percent=round((2*precision*recall/(precision+recall))*100) if hits else 0
  rows.append((s,percent,hits))
 return sorted(rows,key=lambda x:(-x[1],x[0].name))

def image_note(path):
 with Image.open(path) as raw:
  im=ImageOps.exif_transpose(raw).convert("RGB"); w,h=im.size
  small=im.copy(); small.thumbnail((160,160)); r,g,b=ImageStat.Stat(small).mean
 tone="hijau" if g>r*1.08 and g>b*1.08 else "campuran/non-hijau"
 quality="cukup" if max(w,h)>=700 else "rendah; ambil foto lebih dekat"
 return f"Foto {w}×{h}px; rona rata-rata {tone}; resolusi {quality}. Centang ciri yang benar-benar terlihat."

class App(tk.Tk):
 def __init__(self):
  super().__init__(); self.title("Nyoms Vegetasi Pantai — Identifikasi Mangrove"); self.geometry("1180x760"); self.minsize(980,650)
  self.vars={x:tk.BooleanVar() for x in TRAITS}; self.photo=None; self.build(); self.refresh()
 def build(self):
  style=ttk.Style(self); style.theme_use("clam"); style.configure("TLabel",font=("Segoe UI",10))
  top=ttk.Frame(self,padding=(20,14)); top.pack(fill="x")
  ttk.Label(top,text="Nyoms Vegetasi Pantai",font=("Segoe UI",18,"bold"),foreground="#0d5c48").pack(anchor="w")
  ttk.Label(top,text="Identifikasi dari foto + ciri lapangan • rujukan PDF Panduan Pengenalan Mangrove di Indonesia").pack(anchor="w")
  pane=ttk.PanedWindow(self,orient="horizontal"); pane.pack(fill="both",expand=True,padx=16,pady=(0,16))
  left_shell,right=ttk.Frame(pane),ttk.Frame(pane,padding=12); pane.add(left_shell,weight=1); pane.add(right,weight=2)
  left_canvas=tk.Canvas(left_shell,highlightthickness=0)
  left_scroll=ttk.Scrollbar(left_shell,orient="vertical",command=left_canvas.yview)
  left_canvas.configure(yscrollcommand=left_scroll.set)
  left_scroll.pack(side="right",fill="y"); left_canvas.pack(side="left",fill="both",expand=True)
  left=ttk.Frame(left_canvas,padding=12)
  left_window=left_canvas.create_window((0,0),window=left,anchor="nw")
  left.bind("<Configure>",lambda e:left_canvas.configure(scrollregion=left_canvas.bbox("all")))
  left_canvas.bind("<Configure>",lambda e:left_canvas.itemconfigure(left_window,width=e.width))
  left_canvas.bind_all("<MouseWheel>",lambda e:left_canvas.yview_scroll(int(-1*(e.delta/120)),"units"))
  ttk.Label(left,text="1. Tambahkan foto",font=("Segoe UI",12,"bold")).pack(anchor="w")
  ttk.Button(left,text="Pilih foto tanaman…",command=self.pick).pack(anchor="w",pady=6)
  self.preview=ttk.Label(left,text="Belum ada foto",anchor="center",relief="solid",width=34); self.preview.pack(fill="x",ipady=68)
  self.note=ttk.Label(left,text="Foto membantu dokumentasi. Konfirmasi ciri sebelum memakai hasil.",wraplength=300,justify="left"); self.note.pack(anchor="w",pady=(7,12))
  ttk.Label(left,text="2. Centang ciri yang terlihat",font=("Segoe UI",12,"bold")).pack(anchor="w")
  for k,v in TRAITS.items(): ttk.Checkbutton(left,text=v,variable=self.vars[k],command=self.refresh).pack(anchor="w")
  ttk.Button(left,text="Bersihkan pilihan",command=self.clear).pack(anchor="w",pady=10)
  ttk.Label(right,text="3. Kandidat dan pembeda",font=("Segoe UI",12,"bold")).pack(anchor="w")
  self.tree=ttk.Treeview(right,columns=("n","s","e"),show="headings",height=8)
  for col,label,width in (("n","Kandidat",220),("s","Cocok",70),("e","Ciri yang sesuai",430)):
   self.tree.heading(col,text=label); self.tree.column(col,width=width,anchor="center" if col=="s" else "w")
  self.tree.pack(fill="x",pady=6); self.tree.bind("<<TreeviewSelect>>",self.detail)
  compare=ttk.Frame(right); compare.pack(fill="both",expand=True)
  text_shell=ttk.Frame(compare); text_shell.pack(side="left",fill="both",expand=True)
  text_scroll=ttk.Scrollbar(text_shell,orient="vertical")
  self.text=tk.Text(text_shell,wrap="word",font=("Segoe UI",10),padx=12,pady=10,yscrollcommand=text_scroll.set)
  text_scroll.configure(command=self.text.yview); text_scroll.pack(side="right",fill="y"); self.text.pack(side="left",fill="both",expand=True)
  self.text.configure(state="disabled")
  image_shell=ttk.Frame(compare,padding=(10,0,0,0)); image_shell.pack(side="right",fill="y")
  ttk.Label(image_shell,text="Gambar pembanding pedoman",font=("Segoe UI",10,"bold")).pack(anchor="w")
  self.reference=ttk.Label(image_shell,text="Pilih kandidat",anchor="center",relief="solid",width=28)
  self.reference.pack(fill="x",pady=(6,0),ipady=70)
  self.reference_note=ttk.Label(image_shell,text="Ilustrasi dari PDF sumber.",wraplength=210,justify="left")
  self.reference_note.pack(anchor="w",pady=6)
  ttk.Label(right,text="Persentase = kesesuaian gabungan ciri dipilih dengan ciri spesies (bukan kepastian ilmiah). Hasil tinggi tetap perlu dibandingkan dengan gambar dan ciri lapangan.",wraplength=700,foreground="#764a00").pack(anchor="w",pady=8)
 def pick(self):
  path=filedialog.askopenfilename(filetypes=[("Gambar","*.jpg *.jpeg *.png *.webp *.bmp"),("Semua file","*.*")])
  if not path:return
  try:
   with Image.open(path) as raw:
    im=ImageOps.exif_transpose(raw).convert("RGB"); im.thumbnail((300,230)); self.photo=ImageTk.PhotoImage(im)
   self.preview.configure(image=self.photo,text=""); self.note.configure(text=image_note(path))
  except Exception as e: messagebox.showerror("Foto tidak dapat dibuka",str(e))
 def clear(self):
  for v in self.vars.values():v.set(False)
  self.refresh()
 def refresh(self):
  chosen={k for k,v in self.vars.items() if v.get()}
  for row in self.tree.get_children():self.tree.delete(row)
  for sp,score,hits in rank(chosen):
   evidence=", ".join(TRAITS[h] for h in hits) if hits else "Belum ada ciri dipilih"
   self.tree.insert("","end",iid=sp.name,values=(sp.name,f"{score}%",evidence))
  self.tree.selection_set(self.tree.get_children()[0]); self.detail()
 def detail(self,event=None):
  sel=self.tree.selection()
  if not sel:return
  sp=next(x for x in SPECIES if x.name==sel[0])
  self.text.configure(state="normal"); self.text.delete("1.0","end"); self.text.insert("1.0",sp.name+"\n\n"+sp.detail); self.text.configure(state="disabled")
  try:
   with Image.open(resource_path("assets",ASSET_NAMES[sp.name])) as raw:
    image=raw.convert("RGB"); image.thumbnail((220,300)); self.reference_image=ImageTk.PhotoImage(image)
   self.reference.configure(image=self.reference_image,text="")
   self.reference_note.configure(text="Ilustrasi pembanding dari PDF pedoman. Bandingkan daun, bunga/buah, akar, dan habitus.")
  except Exception:
   self.reference.configure(image="",text="Gambar pembanding tidak ditemukan")

def self_test():
 assert len(SPECIES)==10
 assert rank({"daun_kelapa"})[0][0].name=="Nypa fruticans"
 assert rank({"buah_puzzle"})[0][0].name=="Xylocarpus granatum"
 assert rank({"akar_kerucut","bunga_merah","muara"})[0][0].name=="Sonneratia caseolaris"
 assert rank({"akar_tunjang","propagul","lumpur"})[0][0].name=="Rhizophora apiculata"
 assert rank({"akar_tunjang","propagul","lumpur"})[0][1] == 86
 assert rank(set())[0][1] == 0
 print("6/6 pemeriksaan logika identifikasi lulus.")
if __name__=="__main__":
 if "--self-test" in sys.argv:self_test()
 else:App().mainloop()
