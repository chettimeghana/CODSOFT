import streamlit as st
from minimax import best_move
st.set_page_config(
    page_title="Tic Tac Toe AI",
    page_icon="⭕"
)

st.title("⭕ Tic Tac Toe AI")

# Initialize Board
if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "winner" not in st.session_state:
    st.session_state.winner = None


def check_winner():

    board = st.session_state.board

    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_combinations:

        a, b, c = combo

        if (
            board[a] != ""
            and board[a] == board[b] == board[c]
        ):
            return board[a]

    if "" not in board:
        return "Draw"

    return None


def make_move(index):

    if (
        st.session_state.board[index] == ""
        and st.session_state.winner is None
    ):

        # Human Move

        st.session_state.board[index] = "X"

        st.session_state.winner = check_winner()

        # AI Move

        if st.session_state.winner is None:

            ai_move = best_move(
                st.session_state.board
            )

            if ai_move is not None:

                st.session_state.board[
                    ai_move
                ] = "O"

            st.session_state.winner = check_winner()


def reset_game():

    st.session_state.board = [""] * 9
    st.session_state.winner = None


# Display Board

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

# Winner Message

if st.session_state.winner:

    if st.session_state.winner == "Draw":
        st.warning("It's a Draw!")

    else:
        st.success(
            f"{st.session_state.winner} Wins!"
        )

# Reset Button

st.button(
    "🔄 Reset Game",
    on_click=reset_game
)