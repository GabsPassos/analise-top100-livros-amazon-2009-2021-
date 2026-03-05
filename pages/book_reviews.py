import pandas as pd
import streamlit as st

# setando largura do layout
st.set_page_config(layout="wide")

# carregando os datasets
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# LIMPEZA: removendo espaços extras nos nomes das colunas
df_top100_books.columns = df_top100_books.columns.str.strip()
df_reviews.columns = df_reviews.columns.str.strip()

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

# fazendo filtro
df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

# Destando algumas informações
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# organizando na tela
st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

# fazendo um pequeno separador
st.divider()

# iterando e selecionando o título e o comentário, inserindo também a nota do comentário
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}") #rating
    message.write(f"**{row[2]}**") #title
    message.write(row[5]) #review