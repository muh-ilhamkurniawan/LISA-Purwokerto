import streamlit as st
from streamlit_chat import message as st_message

# Definisikan pasangan pertanyaan dan jawaban
qa_pairs = {
    "halo": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei dan Pengaduan\n6. Selesai",

    "9": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei dan Pengaduan\n6. Selesai",

    "1": "Bank Indonesia (BI) adalah bank sentral Republik Indonesia yang bertanggung jawab dalam mengatur dan menjaga kestabilan nilai rupiah. BI juga memiliki peran penting dalam pengaturan kebijakan moneter untuk mencapai tujuan ekonomi nasional.\nSilakan pilih informasi lebih lanjut:\n1. Tugas dan Fungsi\n2. Sejarah BI\n3. Visi dan Misi\n4. Tujuan dan Tugas\n5. Kontak\n- Masukkan Angka 0 untuk kembali",
        "1.1": "Tugas dan Fungsi Bank Indonesia adalah menetapkan dan melaksanakan kebijakan moneter, mengatur dan menjaga kelancaran sistem pembayaran, serta mengatur dan mengawasi perbankan di Indonesia.",
        "1.2": "Sejarah Bank Indonesia dimulai pada tahun 1953, saat bank ini pertama kali didirikan sebagai bank sentral Republik Indonesia.",
        "1.3": "Visi dan Misi Bank Indonesia.",
        "1.4": "Tujuan dan Tugas Bank Indonesia.",
        "1.5": "Bank Indonesia\nJalan M.H. Thamrin No. 2, Jakarta 10350\nContact Center Bank Indonesia Bicara\nTelp. : 131 dan 1500131 (dari luar negeri)\nE-mail : bicara@bi.go.id\nChatbot LISA : 081 131 131 131.",

    "2": "Silakan pilih informasi lebih lanjut:\n1. Lokasi\n2. Jam Pelayanan\n3. Kontak\n- Masukkan Angka 0 untuk kembali",
        "2.1": "Berikut adalah alamat KPwBI Purwokerto :\nJl. Jend. Gatot Subroto No.98, Brubahan, Purwanegara, Kec. Purwokerto Tim., Kabupaten Banyumas, Jawa Tengah 53116\nGoogle Maps: https://g.co/kgs/qe14jYA",
        "2.2": "Jam Pelayanan KPwBI Purwokerto: Senin - Jumat, 08:00 - 16:00 WIB",
        "2.3": "Anda bisa menghubungi KPwBI Purwokerto di kontak berikut: \n- Instagram : https://www.instagram.com/bank_indonesia_purwokerto/\n- TikTok : https://www.tiktok.com/@bi.purwokerto\n- Twitter : https://twitter.com/BI_Purwokerto\n- Youtube : https://www.youtube.com/@bankindonesiapurwokerto702",

    "3": "Silakan pilih informasi lebih lanjut:\n1. Penukaran Uang dan Kas Keliling\n2. Emisi Uang\n- Masukkan Angka 0 untuk kembali",
        "3.1": "Penukaran Uang dapat dilakukan langsung di di KPw Bank Indonesia Purwokerto serta Mobil Kas Keliling yang informasi terkait jadwal dan lainnya bisa dilihat di :\n Instagram : https://www.instagram.com/bank_indonesia_purwokerto/",
        "3.2": "Informasi terkait Emisi Uang yang masih berlaku dapat di lihat pada tautan berikut : https://www.bi.go.id/id/rupiah/gambar-uang/default.aspx",
    
    "4": "PKL adalah kegiatan praktik kerja yang diberikan kepada mahasiswa/siswa yang difasilitasi oleh Bank Indonesia. Memberikan kesempatan bagi mahasiswa/sis​wa untuk belajar dan mengembangkan diri melalui keterlibatan langsung dalam pelaksanaan tugas di Bank Indonesia. Silahkan pilih informasi yang diinginkan:\n1. Persyaratan Umum Akademik\n2. Alur Pendaftaran\n3. Persyaratan Administrasi & Permohonan\n- Masukkan Angka 0 untuk kembali",
        "4.1": "Persyaratan Umum Akademik :\na. Jenjang pendidikan:\n- Peserta PKL: D3/D4/S1/S2\n- Peserta PKL: Sekolah Menengah Kejuruan (SMK)\n\nb. Tingkat pendidikan:\n- Peserta PKL, minimal semester 6\n- Peserta PKL, minimal kelas XI\n\nc. Bidang Studi:\n- Peserta PKL: Ekonomi (Manajemen, Akuntansi, Ilmu Ekonomi, Keuangan), Matematika, Statistika, Teknik Industri, Teknik Informatika, Ilmu Komputer, Sistem Informasi, Hukum, Administrasi Bisnis/Niaga, Psikologi.\n- Peserta PKL: Semua jurusan yang tersedia di SMK.\n\nd. Keahlian khusus antara lain:\n- Peserta PKL: Menguasai Microsoft Office (Word, Excel, PowerPoint); desain grafis; programmer;\n- Peserta PKL: komputer jaringan, multimedia; administrasi arsip; menguasai Microsoft Office (Word, Excel, PowerPoint).",
        "4.2": "Alur Pendaftaran :\n- Pengajuan Magang melalui surat pengantar dan proposal yang dikirimkan ke Kantor Perwakilan Bank Indonesia Purwokerto\n- Jangka waktu proses seleksi maksimal 1 bulan\nJika Lolos : Akan dihubungi pihak KPwBI Purwokerto\nJika Tidak Lolos : Informasi melalui telepon (0281) 631631 KPwBI\n\nCatatan :\n1. Jika mahasiswa lolos seleksi akan dihubungi oleh pihak Bank Indonesia Purwokerto\n2. Pengiriman surat pengantar dan proposal paling lambat 3 bulan sebelum periode magang yang dikehendaki\n3. Seluruh dokumen surat pengantar dan proposal adalah dokumen asli, dikirim ke Bank Indonesia Purwokerto (dalam bentuk hardcopy). Tidak melayani email.",
        "4.3": "Persyaratan Administrasi & Permohonan :\n- Surat Pengantar dari Universitas/Sekolah. Mencakup:\n  - Keterangan data mahasiswa/siswa (Nama, NIM/NIS, Fakultas/Program Studi/Jurusan, Semester/Kelas)\n  - Durasi dan Periode PKL\n- Fotokopi transkrip nilai semester terakhir\n- Proposal Individu. Mencakup:\n  - Data diri lengkap (CV)\n  - Motivation Letter (menjelaskan maksud dan tujuan PKL, harapan atau target yang akan dicapai).\n  - Bidang pekerjaan yang diminati (menceritakan passion atau minat terhadap salah satu bidang pekerjaan: moneter & makroprudensial, sistem pembayaran, pengelolaan uang rupiah, manajemen intern)\n  - Informasi bidang tugas dapat dilihat di tautan berikut ini.\n  - Fotokopi KTP\n  - Fotokopi NPWP\n  - Fotokopi buku rekening tabungan pribadi (khusus untuk peserta PKL).",

    "5": "Silakan pilih layanan lebih lanjut:\n1. Pengaduan\n2. Pengisian Survey Kepuasan\n- Masukkan Angka 0 untuk kembali",
        "5.1": "Silakan isi pengaduan pengguna pada tautan berikut : bit.ly/....",
        "5.2": "Silakan isi survey kepuasan pengguna pada tautan berikut : bit.ly/....",

    "menu": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei dan Pengaduan\n6. Selesai",

    "lanjutan": "Adakah hal lain yang bisa Lisa bantu lagi? Silakan ketik '9' untuk kembali ke menu utama atau ketik '00' untuk mengakhiri percakapan ini yaa 😊",

    "batal": "Adakah hal lain yang bisa Lisa bantu lagi? Silakan ketik 'Menu' untuk kembali ke menu utama atau ketik 'Selesai' untuk mengakhiri percakapan ini yaa 😊",

    "selesai": "Terimakasih sudah menggunakan layanan LISA. Jika ada yang mau ditanyakan silahkan ketik '9'😊"
}

# Menambahkan kunci-kunci lowercase yang sesuai
for key in list(qa_pairs.keys()):
    if key.lower() not in qa_pairs:
        qa_pairs[key.lower()] = qa_pairs[key]

if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.current_node = "halo"
    st.session_state.current_sequence = ""

    # Tampilkan pesan selamat datang pada awal chat jika history belum ada
    st.session_state.history.append({"message": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei dan Pengaduan\n6. Selesai", "is_user": False})


st.title("Hello Chatbot")

# Tampilkan riwayat chatbot di area utama (body) Streamlit
for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i))

# Membuat area kosong untuk input teks
input_area = st.empty()

def generate_answer():
    user_message = st.session_state.input_text.lower()  # Konversi ke lowercase
    current_node = st.session_state.current_node
    current_sequence = st.session_state.current_sequence

    if user_message in ["selesai", "6", "00"]:
        next_node = "selesai"  # Mengatur kembali ke awal
        current_sequence = ""  # Mengosongkan sequence
    elif user_message in ["menu", "kembali", "0", "9"]:
        next_node = "halo"  # Kembali ke menu utama
        current_sequence = ""  # Mengosongkan sequence
    else:
        # Update node berdasarkan input
        if user_message.isdigit() and current_sequence == "":
            current_sequence = user_message
            next_node = user_message
        elif user_message.isdigit() and current_sequence != "":
            cek_node = f"{current_sequence}.{user_message}"
            if cek_node in qa_pairs:
                next_node = cek_node
            else:
                next_node = "halo"
                current_sequence = ""
        else:
            next_node = user_message

    # Validasi bilangan bulat positif
    if next_node.isdigit() and int(next_node) <= 0:
        message_bot = "Silakan masukkan bilangan bulat positif yang lebih besar dari 0."
    else:
        # Cari jawaban berdasarkan pertanyaan yang telah didefinisikan
        message_bot = qa_pairs.get(next_node, "Maaf, saya tidak mengerti pertanyaan Anda. Jika error masih berlanjut silahkan refresh halaman ini")
    
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.history.append({"message": user_message, "is_user": True})
    # Tambahkan jawaban chatbot ke riwayat
    st.session_state.history.append({"message": message_bot, "is_user": False})
    
    # Tambahkan pesan lanjutan jika diperlukan
    if next_node in qa_pairs and next_node not in ["halo", "menu", "selesai", "1", "2", "3", "4", "5"]:
        st.session_state.history.append({"message": qa_pairs["lanjutan"], "is_user": False})
    
    # Update current node dan sequence di state
    st.session_state.current_node = next_node
    st.session_state.current_sequence = current_sequence if user_message != "selesai" else ""

# Menempatkan input teks
# Menempatkan input teks dengan tipe input "number"
st.markdown("""
    <style>
        @media (max-width: 768px) {
            input[type="text"]::-webkit-outer-spin-button,
            input[type="text"]::-webkit-inner-spin-button {
                -webkit-appearance: none;
                margin: 0;
            }
            input[type="text"] {
                -moz-appearance: textfield;
            }
        }
    </style>
""", unsafe_allow_html=True)

input_area.text_input("Talk to the bot (Input angka - masukkan angka disini)", key="input_text", on_change=generate_answer)
