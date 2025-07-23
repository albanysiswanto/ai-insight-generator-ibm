# 📊 AI Insight Generator for Excel Data

A simple web-based tool that analyzes Excel data (sales, finance, etc.) and generates insights using IBM Granite AI via Replicate.com.

Alat berbasis web untuk menganalisis data Excel (seperti penjualan atau laporan keuangan) dan menghasilkan insight otomatis menggunakan IBM Granite AI melalui Replicate.com.

---

## 🌐 Features / Fitur

- 📁 Upload Excel file (.xlsx)
- 📈 Visualize sales trends
- 🔍 Detect anomalies in data
- 🤖 Generate natural language insights using Granite-IBM
- 💬 Dual-language interface ready (can be extended)

---

## 📦 Requirements / Persyaratan

- Python 3.8+
- Replicate account & API token
- Excel file with at least 2 columns:
  - `tanggal` (date)
  - `penjualan` (sales/amount)

---

## 🚀 Installation / Instalasi

```bash
# Install dependencies
pip install streamlit pandas openpyxl matplotlib replicate
````

---

## ▶️ Run the App / Jalankan Aplikasi

```bash
streamlit run app.py
```

---

## 📁 Sample Excel Format / Format Excel Contoh

| tanggal    | penjualan |
| ---------- | --------- |
| 2024-01-01 | 1200000   |
| 2024-02-01 | 1350000   |
| 2024-03-01 | 900000    |

---

## 🔐 Replicate API Setup / Pengaturan API Replicate

1. Register at [replicate.com](https://replicate.com)
2. Go to [Account Settings](https://replicate.com/account)
3. Get your API token
4. Add this line to your `app.py`:

```python
os.environ["REPLICATE_API_TOKEN"] = "your_token_here"
```

---

## 📌 Prompt Example / Contoh Prompt ke AI

```text
Berdasarkan data penjualan berikut:

Januari: 12 juta
Februari: 13.5 juta
Maret: 9 juta

Buatlah insight tren dan rekomendasi bisnis singkat.
```

---

## 📤 Output Example / Contoh Output Insight

> "Penjualan meningkat dari Januari ke Februari, namun turun tajam pada Maret. Disarankan untuk meninjau ulang strategi pemasaran di Q1."

---

## 🙌 Credits / Kredit

Built with:

* [Streamlit](https://streamlit.io/)
* [Replicate](https://replicate.com/)
* [IBM Granite Models](https://research.ibm.com/ai/granite)

---

> ✍️ Made with ❤️ by Albany Siswanto

