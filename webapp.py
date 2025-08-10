import streamlit as st
from streamlit import rerun

import functions

todos = functions.get_todos("re_todo.txt")


def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, "re_todo.txt")


st.title("My To-Do App")
st.header("This is my todo app.")
st.text("This app is used to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, "re_todo.txt")
        del st.session_state[todo]
        rerun()

st.text_input(label="", placeholder="Add a new To do...",
              on_change=add_todo, key="new todo")
