# 📊 Sales Dashboard (Streamlit)

## Deskripsi
Project ini merupakan **dashboard penjualan interaktif** yang dibuat menggunakan **Python & Streamlit**.  
Dashboard ini membantu pengguna memahami performa penjualan melalui **KPI utama, visualisasi, dan filter dinamis**.

Cocok untuk kebutuhan:
- Data Analyst
- Business Analyst
- Junior Data Scientist
- Portfolio kerja remote

---

## Dataset
Menggunakan dataset *Superstore Sales* yang berisi informasi:
- Order Date
- Category & Sub-Category
- Region
- Sales
- Profit
- Quantity

---

## Fitur Dashboard
- 🔎 Filter interaktif berdasarkan **Region** dan **Category**
- 💰 KPI utama:
  - Total Sales
  - Total Profit
  - Total Orders
- 📊 Visualisasi:
  - Penjualan per Kategori
  - Penjualan per Region
  - Tren Penjualan dari waktu ke waktu
- 📄 Tampilan data mentah (raw data)

---

## Struktur Folder
sales-dashboard/ │ ├── data/ │   └── superstore_sales.csv ├── app/ │   └── dashboard.py ├── notebooks/ │   └── eda.ipynb ├── README.md └── requirements.txt

---

## Cara Menjalankan Project

1️⃣ Clone repository:
```bash
git clone https://github.com/rendhive/sales-dashboard.git
cd sales-dashboard

pip install -r requirements.txt

streamlit run app/dashboard.py


Insight yang Didapat
Kategori produk dengan penjualan tertinggi
Region dengan kontribusi sales terbesar
Pola tren penjualan dari waktu ke waktu
Perbandingan performa berdasarkan filter user
Tech Stack
Python
Pandas
Matplotlib
Streamlit
Jupyter Notebook


