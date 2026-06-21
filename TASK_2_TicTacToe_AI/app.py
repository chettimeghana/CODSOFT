import streamlit as st

st.set_page_config(
    page_title="Tic Tac Toe AI",
    page_icon="⭕"
)

st.title("⭕ Tic Tac Toe AI")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

def make_move(index):
    if st.session_state.board[index] == "":
        st.session_state.board[index] = "X"

for row in range(3):

    cols = st.columns(3)

    for col in range(3):

        index = row * 3 + col

        with cols[col]:

            st.button(
                st.session_state.board[index] or " ",
                key=index,
                on_click=make_move,
                args=(index,)
            )