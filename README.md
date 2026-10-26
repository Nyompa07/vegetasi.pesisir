# Nyoms Vegetasi Pantai

Aplikasi desktop untuk membantu mengenali 10 mangrove Indonesia melalui foto dan ciri lapangan. Konten ciri, habitat, sebaran, serta manfaat diringkas dari PDF pengguna: Panduan Pengenalan Mangrove di Indonesia — Y. Rusila Noor, M. Khazali, I N.N. Suryadiputra (1999; cetak ulang 2006).

## Cara memakai

1. Pilih foto tanaman untuk mendokumentasikan spesimen.
2. Centang hanya ciri yang benar-benar tampak: akar, daun, bunga/buah, dan habitat.
3. Baca kandidat teratas serta pembeda lapangannya. Foto tambahan dari daun, akar, bunga/buah, dan lokasi memberi keputusan lebih kuat.

Skor sekarang berupa persentase 0–100% dari kesesuaian gabungan ciri yang dipilih dengan ciri spesies. Nilai itu bukan persentase kepastian ilmiah atau klaim pengenalan AI otomatis: nilai tinggi tetap harus dicek dengan ilustrasi pembanding yang tampil di aplikasi, serta dengan daun, akar, bunga/buah, dan habitat di lapangan. Panduan sumber sendiri menyatakan bahwa ia bukan edisi akhir untuk menjawab semua pertanyaan identifikasi; gunakan hasil untuk pembelajaran/penyaringan awal dan konfirmasi ke ahli untuk catatan ilmiah.

## Windows

Cepat: instal Python 3.10+ dari python.org lalu klik JALANKAN_WINDOWS.bat. Jika Pillow belum tersedia, jalankan: py -m pip install -r requirements.txt.

EXE portable: pada komputer Windows, klik build_portable_windows.bat. Hasilnya berada di dist\NyomsVegetasiPantai.exe dan dapat disalin ke komputer Windows lain tanpa memasang Python. Ilustrasi pembanding dari pedoman ikut disertakan. EXE Windows perlu dibangun di Windows karena PyInstaller membuat paket untuk sistem operasi tempat build dijalankan.

## Uji logika

Jalankan: python app.py --self-test

Uji mencakup empat pembeda kuat: nipah, nyiri, pedada merah, dan bakau minyak.

## Cakupan awal

Avicennia alba, A. marina, Bruguiera gymnorrhiza, Nypa fruticans, Rhizophora apiculata, R. mucronata, R. stylosa, Sonneratia alba, S. caseolaris, dan Xylocarpus granatum.

Tidak ada salinan foto/ilustrasi PDF disertakan agar distribusi aplikasi ringan dan menghormati hak cipta materi sumber.
