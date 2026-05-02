# =========================
# 1. Import Library
# =========================
import kagglehub
import pandas as pd
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

# =========================
# 2. Download Dataset
# =========================
path = kagglehub.dataset_download("sharmajicoder/gen-z-social-media-usage-dataset")
print("Path dataset:", path)

files = os.listdir(path)
print("Isi folder:", files)

# Ambil file CSV
file_path = os.path.join(path, files[0])

# =========================
# 3. Load Data (Sample 30)
# =========================
df = pd.read_csv(file_path, nrows=30)

print("\n=== DATA AWAL ===")
print(tabulate(df.head(), headers="keys", tablefmt="grid"))

# =========================
# 4. Validasi Data
# =========================
print("\nJumlah data:", df.shape)
print("Kolom:", df.columns)
print("\nInfo:")
df.info()

print("\nStatistik:")
print(df.describe())

# =========================
# 5. Distribusi Gender
# =========================
print("\nDistribusi Gender:")
print(df["gender"].value_counts())

# Contoh data per gender
df_tampil = df.groupby("gender").head(2)
print("\nContoh Data per Gender:")
print(tabulate(df_tampil, headers="keys", tablefmt="grid", showindex=False))

# =========================
# 6. Analisis Male per Negara
# =========================
df_male = df[df["gender"] == "Male"]

male_per_country = df_male["country"].value_counts()
print("\nMale per Country:")
print(male_per_country)

top_country = male_per_country.idxmax()
print("\nNegara dengan Male terbanyak:", top_country)

# =========================
# 7. Analisis Proporsi Male
# =========================
total_per_country = df["country"].value_counts()
male_count = df_male["country"].value_counts()

proporsi_male = (male_count / total_per_country).fillna(0)
print("\nProporsi Male per Negara:")
print(proporsi_male)

top_ratio_country = proporsi_male.idxmax()
print("\nNegara dengan proporsi Male tertinggi:", top_ratio_country)

# =========================
# 8. Visualisasi
# =========================
# proporsi_male.sort_values(ascending=False).plot(kind="bar")
# plt.title("Proporsi Male per Negara")
# plt.ylabel("Proporsi")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# =========================
# 9. (OPSIONAL) Profiling
# =========================
# ⚠️ DISARANKAN DIKOMENTARI jika pakai Python 3.13

"""
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Gen Z Social Media Report", explorative=True)
profile.to_file("profiling_report.html")
# """
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Gen Z Social Media Report", explorative=True)
profile.to_file("profiling_report.html")
