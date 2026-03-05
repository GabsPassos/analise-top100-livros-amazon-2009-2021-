import pandas as pd
import streamlit as st
import plotly.express as px

# setando largura do layout
st.set_page_config(layout="wide")

# carregando os datasets
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# colocando numa variável o max e min do preço dos livros
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# usando o método slider do st para fazer um range dos preços max e min, e limitando esse range no valor max
max_price = st.sidebar.slider("Price Range", price_min,price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

# usando o gráfico de barras do plotly para mostrar a qtde de livros por ano
fig = px.bar(df_books["year of publication"].value_counts())

# usando o gráfico de historograma qtde de livros naquele range de preço
fig02 = px.histogram(df_books["book price"])

# ajustando os dois gráficos acima um ao lado do outro
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig02)