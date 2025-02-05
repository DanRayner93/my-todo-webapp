import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def remove_todo(todo):
    todos.remove(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

# Display and handle each todo
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        remove_todo(todo)
        # Update session state to reflect the checkbox change
        del st.session_state[todo]  # Delete the todo from session state

# Text input to add a new todo
st.text_input(label="Enter a Todo", placeholder="Add new Todo",
              on_change=add_todo, key='new_todo')

