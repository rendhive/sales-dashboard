import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================
# CONFIG
# =====================
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📊 Sales Dashboard")
st.markdown("Dashboard interaktif untuk analisis penjualan")

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data():
    df = pd.read_csv("data/superstore_sales.csv")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# =====================
# SIDEBAR FILTER
# =====================
st.sidebar.header("🔎 Filter Data")

region_filter = st.sidebar.multiselect(
    "Pilih Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Pilih Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region_filter)) &
    (df["Category"].isin(category_filter))
]

# =====================
# KPI METRICS
# =====================
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🧾 Total Orders", total_orders)

st.divider()

# =====================
# SALES BY CATEGORY
# =====================
st.subheader("Penjualan per Kategori")

sales_by_category = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots()
sales_by_category.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Total Sales")
ax1.set_xlabel("Category")
st.pyplot(fig1)

# =====================
# SALES BY REGION
# =====================
st.subheader("Penjualan per Region")

sales_by_region = (
    filtered_df
    .groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

fig2, ax2 = plt.subplots()
sales_by_region.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Total Sales")
ax2.set_xlabel("Region")
st.pyplot(fig2)

# =====================
# SALES TREND OVER TIME
# =====================
st.subheader("Tren Penjualan dari Waktu ke Waktu")

sales_trend = (
    filtered_df
    .set_index("Order Date")
    .resample("M")["Sales"]
    .sum()
)

fig3, ax3 = plt.subplots()
sales_trend.plot(ax=ax3)
ax3.set_ylabel("Total Sales")
ax3.set_xlabel("Order Date")
st.pyplot(fig3)

# =====================
# RAW DATA
# =====================
with st.expander("📄 Lihat Data Mentah"):
    st.dataframe(filtered_df)