# FastAPI Todo Enterprise

Proyek ini adalah implementasi RESTful API untuk Todo List berskala Enterprise menggunakan Python (FastAPI), SQLAlchemy, dan MySQL. Dibangun dengan praktik terbaik (best practices) pengembangan modern, termasuk arsitektur berlapis, validasi data yang ketat, dan manajemen migrasi database.

# Catatan Penting

Project ini adalah project pertama pengembang dimana sangat banyak atau 90% pengerjaan dibantu oleh AI Oleh karena itu jika ada kesalahan atau kekurangan dalam project ini mohon di maklumi hehe.

Yang saya lakukan pertama kali dalam belajar bahasa atau teknologi baru dengan Ai yaitu dengan mencari tahu terlebih dahulu tentang teknologi tersebut dengan AI lalu saya memintanya untuk membuatkan project sederhana menggunakan teknologi tersebut dan saya akan mempelajarinya sedikit demi sedikit. 

Dan di sini saya meminta AI untuk membuatkan project FastAPI Todo Enterprise dengan struktur yang baik dan benar serta menggunakan praktik terbaik (best practices) pengembangan modern, termasuk arsitektur berlapis, validasi data yang ketat, dan manajemen migrasi database.

Dan saya juga meminta AI untuk menjelaskan setiap baris kode yang dia buat agar saya bisa memahaminya dengan baik.

Dan yang sudah saya pelajari dari Project ini adalah saya telah menambahkan untuk fitur crud join table dan melakukan testing dan berhasil, sejauh ini saya telah memahami struktur project dan cara kerja dari project ini. dimana seperti biasa .env adalah tempat menyimpan credential dan database, lalu ada folder app yang berisi models, schemas, crud, main, dan api_routes, lalu ada folder alembic untuk migrasi database, dan ada requirements.txt untuk menyimpan dependencies. 

untuk skema cors nya juga saya telah mepelajari dasar " nya dan menggunakan ORM untuk query database.

untuk yang belum terlalu saya pahami adalah mengenai crud dengan ORM seperti sintax query nya karna selama ini saya hanya menggunakan query native sql. dan prisma  serta bahasa pemrograman javascrip mungkin butuh beberapa penyesuaian lagi untuk memahami sintax query nya.

Serta bahasa pemrograman python ini masih sedikit asing bagi saya karna saya lebih terbiasa dengan bahasa pemrograman javascrip atau PHP, namun saya memiliki fondasi yang saya rasa cukup kuat dalam relational database seperti mysql, dan microsoft sql server. seperti penggunaan join table, foreign key, dan lain lain. saya yakin dengan fondasi tersebut saya bisa dengan cepat beradaptasi dengan bahasa pemrograman python ini.


## Fitur Utama

**FastAPI Framework**: Performa tinggi dan validasi otomatis dengan Pydantic.
**SQLAlchemy ORM**: Interaksi database yang aman dan terstruktur.
**MySQL Database**: Penyimpanan data relasional yang handal.
**Alembic Migrations**: Manajemen versi skema database yang terorganisir.
**Enterprise Structure**: Pemisahan concern yang jelas (Models, Schemas, CRUD, API Route).
**CORS Middleware**: Konfigurasi keamanan siap produksi untuk integrasi Frontend.

## Prasyarat

Pastikan Anda telah menginstal:
- Python 3.8+
- MySQL Server

## Instalasi & Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek di komputer Anda:

1.  **Clone Repository**
    ```bash
    git clone <repository_url>
    cd fastapi-todo-enterprise
    ```

2.  **Buat Virtual Environment**
    ```bash
    python -m venv venv
    ```
    
    # Windows
    ```bash
    venv\Scripts\activate
    ```
    

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Environment**
    Buat file `.env` di root folder dan sesuaikan dengan konfigurasi database Anda:

    ```env
    DATABASE_URL=mysql+pymysql://user:password@localhost:3306/db_name
    ```

5.  **Jalankan Migrasi Database**
    ```bash
    alembic upgrade head
    ```

6.  **Jalankan Server**
    ```bash
    uvicorn app.main:app --reload
    ```
    Akses dokumentasi API di: [http://localhost:8000/docs](http://localhost:8000/docs)


## Pesan Pengembang & Refleksi AI

Berikut adalah catatan penting dan refleksi saya selama pengembangan proyek ini menggunakan bantuan teknologi AI (Agentic AI Assistant dari Antigravity & Gemini 3 Pro):

**Semua ini adalah murni pendapat saya pribadi dan mungkin masih memiliki kekeliruan dalam pemahaman saya**

1.  **AI sebagai Akselerator**: Fitur AI yang paling membantu adalah kemampuan integrasi Agentic AI yang mempercepat proses coding secara signifikan. Sarannya mudah dimengerti, relevan, dan sangat membantu dalam memecahkan masalah logika.

2.  **Keamanan & Privasi**: Meskipun AI sangat canggih, hal-hal sensitif seperti **Environment Variable**, **Credential**, kunci rahasia, atau data pribadi **TIDAK** boleh diserahkan kepada AI untuk menjaga keamanan dan kerahasiaan.

3.  **Pentingnya Review Manusia**: Hasil coding AI **WAJIB** direview. Tanpa verifikasi manusia, sering terjadi bias, inkonsistensi, atau kode yang membingungkan yang bisa menyulitkan perawatan (maintenance) di masa depan.

4.  **Keterbatasan AI**: Saya menyadari bahwa AI "pantang menyerah" dalam memberikan jawaban. Meskipun konteksnya mungkin sudah melenceng atau dia sebenarnya tidak tahu, AI cenderung tetap mencoba menjawab. Ini bisa menyesatkan jika kita tidak teliti.

5.  **Memahami Cara Kerja AI (Reward System)**: Karena dilatih dengan **Reinforcement Learning**, AI pada dasarnya ingin **dihadiahi** karena memberikan jawaban yang **terlihat benar**. Oleh karena itu, dia akan berusaha memberikan jawaban yang paling mungkin memuaskan user, meskipun secara fakta teknis mungkin kurang tepat.

6.  **Seni Prompt Engineering**: Kunci menggunakan AI yang efektif adalah **Prompt** yang baik. Kita harus memberikan batasan (constraints) yang jelas, konteks yang lengkap, dan instruksi spesifik agar AI tidak "berhalusinasi" atau melebar kemana-mana.

7.  **AI adalah Alat (Tool), Bukan Pengganti**: Kesimpulannya, AI adalah alat bantu yang luar biasa untuk **mempercepat** pekerjaan manusia, bukan untuk **menggantikan** manusia sepenuhnya. Pendampingan manusia mutlak diperlukan agar hasil akhirnya akurat, tidak bias, informatif, dan ringkas.
