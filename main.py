import streamlit as st
from streamlit_chat import message as st_message

# CSS untuk mengatur jarak antara angka dalam daftar dan paragraf
st.markdown("""
<style>
    .stTextInput > div > div > input {
        padding: 10px;
    }
    ul {
        margin-left: 20px;
        padding-left: 10px;
        list-style-position: inside;
    }
    ul li {
        margin-bottom: 5px;
    }
    ul li::marker {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Definisikan pasangan pertanyaan dan jawaban, anda bisa memperbarui dan menambahkan sesuai dengan keinginan
qa_pairs = {
    "halo": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei, Pengaduan, dan Informasi Publik\n6. Selesai",

    "9": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei dan Pengaduan\n6. Selesai",

    "1": "Bank Indonesia (BI) adalah bank sentral Republik Indonesia yang bertanggung jawab dalam mengatur dan menjaga kestabilan nilai rupiah. BI juga memiliki peran penting dalam pengaturan kebijakan moneter untuk mencapai tujuan ekonomi nasional.\n\nUntuk Informasi lebih lanjut terkait Bank Indonesia dapat di liat pada tautan berikut : https://www.bi.go.id/id/tentang-bi/profil/Default.aspx\n\nSilakan pilih informasi lebih lanjut:\n1. Organisasi\n2. Kontak\n\nMasukkan Angka 0 untuk kembali",
        "1.1": "Struktur Organisasi Bank Indonesia dapat dilihat di tautan berikut : https://www.bi.go.id/id/tentang-bi/profil/organisasi/Default.aspx",
        "1.2": "Bank Indonesia\nJalan M.H. Thamrin No. 2, Jakarta 10350\nContact Center Bank Indonesia Bicara\nTelp. : 131 dan 1500131 (dari luar negeri)\nE-mail : bicara@bi.go.id\nChatbot LISA : 081 131 131 131.",

    "2": "Silakan pilih informasi lebih lanjut:\n1. Profil Pimpinan\n2. Lokasi\n3. Jam Pelayanan\n4. Kontak\n\nMasukkan Angka 0 untuk kembali",
        "2.1": "CHRISTOVENY\nDeputi Direktur – Kepala Perwakilan BI Purwokerto\n\nChristoveny lahir di Payakumbuh pada tahun 1976. Menyelesaikan pendidikan sarjana di Bidang Ekonomi Universitas Andalas pada tahun 1999. Christoveny melanjutkan Pendidikan di Universitas Indonesia dan mendapatkan gelar Master di Bidang Manajemen pada tahun 2010.\n\nMemulai kariernya di Bank Indonesia sejak tahun 2001, saat ini Christoveny menjabat sebagai Kepala Perwakilan Bank Indonesia Purwokerto sejak tahun 2024. Sebelumnya, Christoveny menjabat sebagai Deputi Kepala Perwakilan Perumusan & Implementasi KEKDA (2023-2024).​",
        "2.2": "Berikut adalah alamat KPwBI Purwokerto :\nJl. Jend. Gatot Subroto No.98, Brubahan, Purwanegara, Kec. Purwokerto Tim., Kabupaten Banyumas, Jawa Tengah 53116\nGoogle Maps: https://g.co/kgs/qe14jYA",
        "2.3": "Jam Pelayanan KPwBI Purwokerto:\nSenin - Jumat, 08:00 - 16:00 WIB",
        "2.4": "Anda bisa menghubungi KPwBI Purwokerto di kontak berikut:\n- No HP : (0281) 631632\n- Instagram : https://www.instagram.com/bank_indonesia_purwokerto/\n- TikTok : https://www.tiktok.com/@bi.purwokerto\n- Twitter : https://twitter.com/BI_Purwokerto\n- Youtube : https://www.youtube.com/@bankindonesiapurwokerto702",


    "3": "Silakan pilih informasi lebih lanjut:\n1. Penukaran Uang dan Kas Keliling\n2. Emisi Uang\n\nMasukkan Angka 0 untuk kembali",
        "3.1": "Penukaran Uang dapat dilakukan langsung di di KPw Bank Indonesia Purwokerto serta Kas Keliling yang informasi terkait jadwal dan lainnya bisa dilihat di :\n Instagram : https://www.instagram.com/bank_indonesia_purwokerto/ serta website https://pintar.bi.go.id/Order/KasKeliling\nSilahkan pilih informasi lebih lanjut:\n1. Syarat Penukaran Uang Rupiah Melalui Kas Keliling\n2. Uang Rupiah yang Dapat Ditukarkan\n\nMasukkan Angka 0 untuk kembali",
            "3.1.1": "Syarat Penukaran Uang Rupiah Melalui Kas Keliling adalah sebagai berikut :\n1. Penukar harus menunjukkan bukti pemesanan dalam bentuk digital/cetak.\n2. Uang Rupiah yang akan ditukarkan harus sesuai nominal yang tertera pada bukti pemesanan.\n3. Uang Rupiah yang akan ditukarkan harus dipilah, disusun menurut jenis pecahan dan tahun emisi, serta dipisahkan antara yang layak dan tidak layak edar.\n4. Tidak boleh menggunakan selotip, perekat, lakban, atau steples untuk mengelompokkan uang Rupiah.\n5. Bank Indonesia memberikan penggantian sesuai dengan nominal uang Rupiah yang ditukarkan, dalam pecahan dan tahun emisi yang sama atau berbeda.\n6. Penggantian uang Rupiah hanya diberikan jika ciri keasliannya dapat diidentifikasi.\n7. NIK-KTP tidak dapat digunakan untuk pemesanan baru setelah tanggal yang tertera pada bukti pemesanan, namun dapat digunakan kembali setelah tanggal tersebut untuk pemesanan selanjutnya.",
            "3.1.2": "Uang Rupiah yang Dapat Ditukarkan adalah sebagai berikut :\n1. Masyarakat bisa memilih jenis pecahan uang Rupiah yang tersedia di lokasi kas keliling saat melakukan pemesanan.\n2. Jumlah penukaran uang Rupiah kertas dan logam mengikuti alokasi ketersediaan di lokasi kas keliling yang dipilih.\n3. Penukaran uang Rupiah logam dapat dilakukan maksimal 250 keping per pecahan.\n4. Penukaran uang Rupiah kertas dilakukan dalam kelipatan setiap 100 lembar per pecahan, mengikuti alokasi yang ditetapkan oleh Bank Indonesia.\n5. Bank Indonesia dapat memberikan uang Rupiah dari berbagai jenis tahun emisi yang masih berlaku sebagai alat pembayaran yang sah.",

        "3.2": "Informasi terkait Emisi Uang yang masih berlaku dapat di lihat pada tautan berikut : https://www.bi.go.id/id/rupiah/gambar-uang/default.aspx",

    "4": "PKL adalah kegiatan praktik kerja yang diberikan kepada mahasiswa/siswa yang difasilitasi oleh Bank Indonesia. Memberikan kesempatan bagi mahasiswa/sis​wa untuk belajar dan mengembangkan diri melalui keterlibatan langsung dalam pelaksanaan tugas di Bank Indonesia. Silahkan pilih informasi yang diinginkan:\n1. Persyaratan Umum Akademik\n2. Alur Pendaftaran\n3. Persyaratan Administrasi & Permohonan\n\nMasukkan Angka 0 untuk kembali",
        "4.1": "Persyaratan Umum Akademik :\na. Jenjang pendidikan:\n- Peserta PKL: D3/D4/S1/S2\n- Peserta PKL: Sekolah Menengah Kejuruan (SMK)\n\nb. Tingkat pendidikan:\n- Peserta PKL, minimal semester 6\n- Peserta PKL, minimal kelas XI\n\nc. Bidang Studi:\n- Peserta PKL: Ekonomi (Manajemen, Akuntansi, Ilmu Ekonomi, Keuangan), Matematika, Statistika, Teknik Industri, Teknik Informatika, Ilmu Komputer, Sistem Informasi, Hukum, Administrasi Bisnis/Niaga, Psikologi.\n- Peserta PKL: Semua jurusan yang tersedia di SMK.\n\nd. Keahlian khusus antara lain:\n- Peserta PKL: Menguasai Microsoft Office (Word, Excel, PowerPoint); desain grafis; programmer;\n- Peserta PKL: komputer jaringan, multimedia; administrasi arsip; menguasai Microsoft Office (Word, Excel, PowerPoint).",
        "4.2": "Alur Pendaftaran :\n- Pengajuan Magang melalui surat pengantar dan proposal yang dikirimkan ke Kantor Perwakilan Bank Indonesia Purwokerto\n- Jangka waktu proses seleksi maksimal 1 bulan\nJika Lolos : Akan dihubungi pihak KPwBI Purwokerto\nJika Tidak Lolos : Informasi melalui telepon (0281) 631631 KPwBI\n\nCatatan :\n1. Jika mahasiswa lolos seleksi akan dihubungi oleh pihak Bank Indonesia Purwokerto\n2. Pengiriman surat pengantar dan proposal paling lambat 3 bulan sebelum periode magang yang dikehendaki\n3. Seluruh dokumen surat pengantar dan proposal adalah dokumen asli, dikirim ke Bank Indonesia Purwokerto (dalam bentuk hardcopy). Tidak melayani email.",
        "4.3": "Persyaratan Administrasi & Permohonan :\n- Surat Pengantar dari Universitas/Sekolah. Mencakup:\n  - Keterangan data mahasiswa/siswa (Nama, NIM/NIS, Fakultas/Program Studi/Jurusan, Semester/Kelas)\n  - Durasi dan Periode PKL\n- Fotokopi transkrip nilai semester terakhir\n- Proposal Individu. Mencakup:\n  - Data diri lengkap (CV)\n  - Motivation Letter (menjelaskan maksud dan tujuan PKL, harapan atau target yang akan dicapai).\n  - Bidang pekerjaan yang diminati (menceritakan passion atau minat terhadap salah satu bidang pekerjaan: moneter & makroprudensial, sistem pembayaran, pengelolaan uang rupiah, manajemen intern)\n  - Informasi bidang tugas dapat dilihat di tautan berikut ini.\n  - Fotokopi KTP\n  - Fotokopi NPWP\n  - Fotokopi buku rekening tabungan pribadi (khusus untuk peserta PKL).",

    "5": "Silakan pilih layanan lebih lanjut:\n1. Pengajuan Informasi Publik\n2. Pengaduan\n3. Pengisian Survey Kepuasan\n\nMasukkan Angka 0 untuk kembali",
        "5.1": "Informasi publik bisa diakses pada tautan berikut : https://www.bi.go.id/id/informasi-publik/informasi-publik/Default.aspx \natau jika ingin pengajuan informasi lain bisa lewat tautan berikut : https://www.bi.go.id/id/layanan/permintaan-informasi/default.aspx",
        "5.2": "Tata Cara Penyampaian Pengaduan, Tindak Lanjut dan Penyelesaian Sekilas Perlindungan Konsumen\n\nTelepon: 131​​\nEmail: bicara@bi.go.id\nTertulis: Surat disampaikan ke KPwDN terdekat dengan domisili Konsumen\n\n​Tata Cara Penyampaian Pengaduan, Tindak Lanjut, dan Penyelesaian Mekanisme Pengaduan Konsumen\nKonsumen dapat menyampaikan pengaduan ke Bank Indonesia, melalui:\n\n1. Contact Center Bank Indonesia (BI Bicara) Telp. 131 dan 1500131 (dari luar negeri)​\n2. Surat Elektronik atau E-mail ke bicara@bi.go.id;  \n3. Surat Tertulis kepada Kantor Perwakilan Bank Indonesia (KPw BI) yang terdekat dengan domisili Konsumen.\n4. Layanan Bicara Daring melalui aplikasi Webex dengan cara klik tautan berikut:\nhttps://bankindonesia.webex.com/join/bicara.\n5. Website Form ​​Pengaduan Konsumen ​dengan menggunakan form online Pengaduan Konsumen BI​",
        "5.3": "Silakan isi survey kepuasan pengguna pada tautan berikut : bit.ly/....",


    "menu": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei, Pengaduan, dan Informasi Publik\n6. Selesai",

    "lanjutan": "Adakah hal lain yang bisa Lisa bantu lagi? Silakan ketik '9' untuk kembali ke menu utama atau ketik '00' untuk mengakhiri percakapan ini yaa 😊",

    "batal": "Adakah hal lain yang bisa Lisa bantu lagi? Silakan ketik '9' untuk kembali ke menu utama atau ketik '00' untuk mengakhiri percakapan ini yaa 😊",

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

    # Tampilkan pesan selamat datang pada awal chat jika history belum ada atau website pertama kali dibuka
    st.session_state.history.append({"message": "Halo selamat datang di KPw Bank Indonesia Purwokerto, silahkan pilih informasi yang diinginkan:\n1. Tentang Bank Indonesia\n2. Informasi Kantor Perwakilan Bank Indonesia Purwokerto\n3. Layanan yang tersedia di Bank Indonesia Purwokerto\n4. Magang dan PKL\n5. Survei, Pengaduan, dan Informasi Publik\n6. Selesai", "is_user": False})


st.title("Hello Chatbot")

# Tampilkan riwayat chatbot di area utama (body) Streamlit
for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i))


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
                current_sequence = cek_node
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
        message_bot = qa_pairs.get(next_node, "Maaf, saya tidak mengerti pertanyaan Anda. Silakan ketik '9' untuk kembali ke menu utama atau jika error masih berlanjut silahkan refresh halaman ini")
    
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.history.append({"message": user_message, "is_user": True})
    # Tambahkan jawaban chatbot ke riwayat
    st.session_state.history.append({"message": message_bot, "is_user": False})
    
    # Tambahkan pesan lanjutan jika diperlukan
    if next_node in qa_pairs and next_node not in ["halo", "menu", "selesai", "1", "2", "3","3.1", "4", "5"]:
        st.session_state.history.append({"message": qa_pairs["lanjutan"], "is_user": False})
    
    # Update current node dan sequence di state
    st.session_state.current_node = next_node
    st.session_state.current_sequence = current_sequence if user_message != "selesai" else ""
    
    # Mengosongkan input text setelah tombol diklik
    st.session_state.input_text = ""

# Membuat area kosong untuk input teks
input_area = st.empty()
# Membuat kolom untuk input teks dan tombol di sampingnya
input_area = st.text_input("Talk to the bot (Input angka - masukkan angka disini)", key="input_text", on_change=generate_answer)
