import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Customer Analytics Dashboard")
df = pd.read_csv("customers.csv")
st.sidebar.header("Filter Data")
departments = st.sidebar.multiselect(
    "Pilih Departments",
    df["Department"].dropna().unique()
)
genders = st.sidebar.multiselect(
    "Pilih Gender",
    df["Gender"].dropna().unique()
)
st.sidebar.header("Filter Rentang Umur")
min_usia, max_usia = int(df["Age"].min()), int(df["Age"].max())
usia_range = st.sidebar.slider(
    "Usia",
    min_value=min_usia,
    max_value=max_usia,
    value=(min_usia, max_usia)
)
df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["Gender"].isin(genders)) &
    (df["Age"].between(usia_range[0], usia_range[1]))
]
st.subheader("Data Tabel")
st.dataframe(df_filtered)
st.subheader("Visualisasi Statistik")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Distribusi Gender")
    pie_gender = px.pie(
        df_filtered,
        names="Gender",
        color="Gender",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(pie_gender)

with col2:
    st.subheader("Gaji Rata-rata per Department")

    salary_dept = (
        df_filtered
        .groupby("Department")["AnnualSalary"]
        .mean()
        .reset_index()
    )

    bar_salary = px.bar(
        salary_dept,
        x="Department",
        y="AnnualSalary",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(bar_salary)
    
st.subheader("Rata-rata Gaji Berdasarkan Usia")
salary_age = (
    df_filtered
    .groupby("Age")["AnnualSalary"]
    .mean()
    .reset_index()
    .sort_values("Age")
)

line_age = px.line(
    salary_age,
    x="Age",
    y="AnnualSalary",
    markers=True
)

st.plotly_chart(line_age)


st.subheader("Jumlah Karyawan per Departemen")
count_dept = (
    df.groupby("Department")["EEID"]
    .count()
    .reset_index()
    .rename(columns={"EEID": "JumlahKaryawan"})
)
chart_dept = px.bar(
    count_dept,
    x="Department",
    y="JumlahKaryawan",
    color="Department",
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(chart_dept)


st.subheader("Rata-rata Gaji per Gender")
salary_gender = (
    df.groupby("Gender")["AnnualSalary"]
    .mean()
    .reset_index()
)
chart_salary_gender = px.bar(
    salary_gender,
    x="Gender",
    y="AnnualSalary",
    color="Gender",
    color_discrete_sequence=px.colors.qualitative.Pastel
)
st.plotly_chart(chart_salary_gender)


# === Chart 4: Distribusi Lokasi (Country) ===
st.subheader("Lokasi Karyawan per Country")
count_country = (
    df.groupby("Country")["EEID"]
    .count()
    .reset_index()
    .rename(columns={"EEID": "JumlahKaryawan"})
)
chart_country = px.bar(
    count_country,
    x="Country",
    y="JumlahKaryawan",
    color="Country",
    color_discrete_sequence=px.colors.qualitative.Set1
)
st.plotly_chart(chart_country)