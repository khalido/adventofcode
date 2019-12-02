import utils
from importlib import import_module
import streamlit as st
import os


# sidebar
st.sidebar.subheader("Choose day")
days = [f[:-3] for f in os.listdir() if f.startswith("day")]
selected_day = st.sidebar.radio("Choose day", days, key="choose_day")
day = import_module(selected_day)

st.sidebar.subheader("Input")
user_inp = st.sidebar.text_area('Copy paste your own input', "", key="user_inp")
inp = day.parse_input(user_inp)

def main():
    st.title("Advent of Code 2019")

    st.subheader("Input")
    st.code(inp)
    st.markdown("Mass Distribution")
    st.bar_chart(inp)

    st.subheader("Part 1")
    st.code(day.solve_1(inp))

    st.subheader("Part 2")
    st.code(day.solve_2(inp))
    


if __name__ == "__main__":
    main()