import pandas as pd
import streamlit as st

# configuração da página
st.set_page_config(layout="wide")

# 1.Carregamento e limpeza inicial (datasets)
df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv")

# padronizando colunas logo no início para evitar erros de busca
df_reviews.columns = [col.strip().lower().replace(" ", "_")
    for col in df_reviews.columns]
df_top100_books.columns = [col.strip().lower().replace(" ", "_")
    for col in df_top100_books.columns]

#2.Sidebar e seleção
books = df_top100_books["book_title"].unique()
book_selected = st.sidebar.selectbox("Choose a book", books)

#3.Filtros
df_book_info = df_top100_books[df_top100_books["book_title"] == book_selected]
df_reviews_f = df_reviews[df_reviews["book_name"] == book_selected]

#4.Destacando detalhes do livro
if not df_book_info.empty:
    info = df_book_info.iloc[0]

    st.title(info["book_title"])
    st.subheader(info["genre"])

    col1, col2, col3 = st.columns(3)
    col1.metric("Price", f"${info['book_price']}")
    col2.metric("Rating", info["rating"])
    col3.metric("Year", info["year_of_publication"])

    # fazendo um pequeno separador
    st.divider()

    # 5.Seção de reviews
    st.subheader("Reader Review")

    if df_reviews_f.empty:
        st.info("Ainda não temos avaliações detalhadas para este livro.")
    else:
        #2.Percorrendo as avaliações e exibindo no formato de chat       
        for index, row in df_reviews_f.iterrows():
            with st.chat_message(str(row["reviewer_rating"])):
                st.write(f"**{row['review_title']}**") # title em negrito
                st.write(row["review_description"]) # review