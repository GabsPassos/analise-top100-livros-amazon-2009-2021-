import pandas as pd
import streamlit as st
import plotly.express as px

# setando largura do layout
st.set_page_config(layout="wide")

# 1.Boa prática: carregando os datasets com cache performance (decorator do streamlit)
st.cache_data()
def load_data():
    df = pd.read_csv("datasets/Top-100 Trending Books.csv")
    return df

df_top100_books = load_data()

# 2.sidebar e filtros
st.sidebar.header("Filters")
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# filtragem do dataframe
df_filtered = df_top100_books[df_top100_books["book price"] <= max_price]

# 3. exibição do dataframe com título
st.title("Amazon Top 100 Best Selling Books")
st.dataframe(df_filtered, width="stretch")

# gráficos
col1, col2 = st.columns(2)

# gráfico de barras - qtde por ano
# ajustando nome dos eixos (resetando o index para o plotly renomear os eixos corretamente 
books_per_year = df_filtered["year of publication"].value_counts().reset_index()
books_per_year.columns = ["year", "qtde"]

fig = px.bar(books_per_year, x="year", y="qtde", title="books published by year")
col1.plotly_chart(fig, width="stretch")

# hitorograma de preços
fig02 = px.histogram(df_filtered,
                     x="book price",
                     labels={'book price': 'price', 'count': 'books quantity'})
col2.plotly_chart(fig02, width='stretch')