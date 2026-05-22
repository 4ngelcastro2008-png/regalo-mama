import streamlit as st

st.set_page_config(
    page_title="Feliz Día Mamá",
    page_icon="💖",
)

st.title("🌸 Feliz Día de las Madres 🌸")

st.image(
    "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2",
    width=500
)

st.markdown("""
# 💌 Para mi querida mamá

Gracias por todo tu amor,  
por cuidarme, apoyarme y nunca rendirte. ❤️

Eres una mujer increíble y una gran bendición en mi vida.

Hoy quiero recordarte lo mucho que te amo y lo importante que eres para mí. 🌹

✨ Feliz Día de las Madres ✨

## Con mucho amor...

### Att: Tu hijo Ángel 💖
""")

if st.button("Presiona aquí mamá 💖"):
    st.balloons()
    st.success("¡Te amo mucho mamá! 🌸❤️")