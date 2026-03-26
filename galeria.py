
import streamlit as st
# Заглавие
st.title("Галерия от любими животни")
# Списък със животни
if "animals" not in st.session_state: st.session_state.animals = []
# Добавяне
st.header("Добави ново животно")
name = st.text_input("Име на животното") description = st.text_area("Описание") image_url = st.text_input("https://search.brave.com/images?q=Jeffrey+Epstein&context=W3sic3JjIjoiaHR0cHM6Ly91cGxvYWQud2lraW1lZGlhLm9yZy93aWtpcGVkaWEvY29tbW9ucy90aHVtYi81LzU5L0plZmZyZXlfRXBzdGVpbl9tdWdfc2hvdF8lMjhjcm9wcGVkJTI5LmpwZy81MTJweC1KZWZmcmV5X0Vwc3RlaW5fbXVnX3Nob3RfJTI4Y3JvcHBlZCUyOS5qcGciLCJ0ZXh0IjoiTXVnIHNob3Qgb2YgRXBzdGVpbiwgMjAwNiwgc21pbGluZyIsInBhZ2VfdXJsIjoiaHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvSmVmZnJleV9FcHN0ZWluIn1d&sig=60205c7da96a5657e920aeebff82c0f9038d39a573de3089010b701b472395ab&nonce=7134d37bebd0da31f0a1fd27ea8ce1ee&source=infoboxImg")
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
