import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import replicate
import os
from dotenv import load_dotenv


load_dotenv()

# ========== CONFIG ==========
st.set_page_config(page_title="AI Insight Generator", layout="wide")
st.title("📊 AI Insight Generator for Excel Data")

def generate_insight_with_granite(prompt):
    try:
        output = replicate.run(
            "ibm-granite/granite-3.3-8b-instruct",
            input={"prompt": prompt, "max_new_tokens": 300, "temperature": 0.7}
        )
        return "".join(output)
    except Exception as e:
        return f"❌ Error saat memanggil Granite: {e}"

# ========== FILE UPLOAD ==========
uploaded_file = st.file_uploader("Upload Excel file (.xlsx) dengan kolom 'tanggal' dan 'penjualan'", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.subheader("📄 Data Preview")
        st.dataframe(df.head())

        # Validasi kolom
        if "tanggal" not in df.columns or "penjualan" not in df.columns:
            st.error("❌ File harus memiliki kolom: `tanggal` dan `penjualan`")
        else:
            df['tanggal'] = pd.to_datetime(df['tanggal'])
            df = df.sort_values("tanggal")

            # ========== GRAFIK ==========
            st.subheader("📈 Grafik Penjualan")
            fig, ax = plt.subplots()
            ax.plot(df["tanggal"], df["penjualan"], marker="o", linestyle="-")
            ax.set_xlabel("Tanggal")
            ax.set_ylabel("Penjualan")
            ax.set_title("Tren Penjualan")
            st.pyplot(fig)

            # ========== INSIGHT NUMERIK ==========
            st.subheader("📊 Insight Angka Otomatis")

            perubahan = df["penjualan"].pct_change().fillna(0)
            rata2 = perubahan.mean() * 100
            naik = df[df["penjualan"].diff() > 0]
            turun = df[df["penjualan"].diff() < 0]
            anomali = df[np.abs(df["penjualan"] - df["penjualan"].mean()) > 2 * df["penjualan"].std()]

            st.markdown(f"""
            - 📈 Rata-rata pertumbuhan bulanan: **{rata2:.2f}%**
            - 🔺 Jumlah bulan naik: **{len(naik)}**
            - 🔻 Jumlah bulan turun: **{len(turun)}**
            - 🚨 Anomali terdeteksi: **{len(anomali)} bulan**
            """)

            if not anomali.empty:
                st.markdown("🚨 **Detail Anomali Terdeteksi:**")
                st.dataframe(anomali[["tanggal", "penjualan"]])

            # ========== INSIGHT AI ==========
            st.subheader("🤖 Insight dari AI Granite")

            ringkasan = "\n".join([
                f"{row['tanggal'].strftime('%B %Y')}: {int(row['penjualan']):,}" for idx, row in df.iterrows()
            ])

            prompt = f"""
Berdasarkan data penjualan berikut:

{ringkasan}

Buatlah ringkasan tren penjualan dan rekomendasi strategi bisnis dalam bentuk paragraf singkat.
"""

            with st.spinner("🔍 AI sedang menganalisis..."):
                granite_result = generate_insight_with_granite(prompt)

            st.success("✅ Insight berhasil dibuat:")
            st.markdown(granite_result)

    except Exception as e:
        st.error(f"❌ Gagal memproses file: {e}")
