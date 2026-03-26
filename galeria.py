
import streamlit as st

# Заглавие
st.title("Галерия от любими животни")

# Списък със животни
if "animals" not in st.session_state:
    st.session_state.animals = []

# Добавяне
st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area("Описание")
image_url = st.text_input("Image URL")

if st.button("Добави"):
    if name and description and image_url:
        st.session_state.animals.append({
            "име": name,
            "описание": description,
            "картинка": image_url
        })
        st.success(f"✅ {name} е добавено!")
    else:
        st.warning("Попълнете всички полета!")

if st.session_state.animals:
    st.header("Премахни животно")
    names = [a["име"] for a in st.session_state.animals]
    remove_name = st.selectbox("Избери животно за премахване", names)

    if st.button("Премахни"):
        for a in st.session_state.animals:
            if a["име"] == remove_name:
                st.session_state.animals.remove(a)
                break
        st.success(f"✅ {remove_name} е премахнато!")

# Визуализация
st.header("Галерия")
if st.session_state.animals:
    cols = st.columns(3)
    for idx, animal in enumerate(st.session_state.animals):
        with cols[idx % 3]:
            st.subheader(animal["име"])
            st.image(animal["картинка"], use_container_width=True)
            st.write(animal["описание"])
else:
    st.info("Галерията е празна. Добавете животни!")
