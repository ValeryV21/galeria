
import streamlit as st
# Заглавие
st.title("Галерия от любими животни")
# Списък със животни
if "animals" not in st.session_state: st.session_state.animals = []
# Добавяне
st.header("Добави ново животно")
name = st.text_input("Име на животното") description = st.text_area("Описание") image_url = st.text_input("URL на картинкa")
if st.button("Добави"):
if name and description and image_url:
st.session_state.animals.append({
})
"имe": name,
"описание": description,
"картинка": image url
st.success(f" {name} е добавено!")
else:
st.warning ("Попълнете всички полета!")


if st.session_state.animals:
st.header("Премахни животно")
names = []
for a in st.session_state.animals:
names.append(a["имe"])
remove_name = st.selectbox("Избери животно за премажване", names)
if st.button("Премаxни"):
for a in st.session_state.animals:
if a["ème"] == remove_name:
st.session_state.animals.remove(a)
break
st.success(f" {remove_name} e прeмаxнато!")
# Визуализация
st.header("Галерия")
if st.session_state.animals:
else:
cols = st.columns (3)
for idx, animal in enumerate(st.session_state.animals): with cols[idx % 3]:
st.subheader(animal["имe"])
st.image (animal["картинка"], use_column_width=True) st.write(animal["oписaниe"])
st.info("Галерията е празна. Добавете животни!")
