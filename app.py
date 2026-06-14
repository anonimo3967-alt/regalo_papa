import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Benevolencia - Feliz Día Papá", page_icon="❤️", layout="centered")


hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)


custom_color = "#FFF4CB"


custom_html = f"""
<style>
/* Fondo animado sutil adaptado para DARK THEME */
body, .main-bg {{
    background: linear-gradient(-45deg, #0f0f13, #1a1a24, #141e30, #243b55);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    height: 100vh;
    position: fixed;
    width: 100vw;
    top: 0;
    left: 0;
    z-index: -1;
}}

@keyframes gradientBG {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}


.door-container {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    z-index: 99999;
    pointer-events: none;
}}

.door {{
    width: 50%;
    height: 100%;
    background: #111116; /* Color oscuro para las puertas */
    transition: transform 2.2s cubic-bezier(0.7, 0, 0.3, 1);
    display: flex;
    align-items: center;
    justify-content: center;
    color: {custom_color};
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 1.8rem;
    font-weight: bold;
    box-shadow: inset 0 0 80px rgba(0,0,0,0.8);
}}


.door.left {{ border-right: 2px solid {custom_color}; }}
.door.right {{ border-left: 2px solid {custom_color}; }}


.open .door.left {{ transform: translateX(-100%); }}
.open .door.right {{ transform: translateX(100%); }}
</style>

<div class="main-bg"></div>


<audio id="bg-music" src="https://www.myinstants.com/media/sounds/subnautica-new-blueprint-acquired.mp3" preload="auto"></audio>

<script>

window.parent.document.addEventListener('open_door', function() {{
    // 1. Reproducir el sonido/música al hacer clic
    var audio = document.getElementById('bg-music');
    if(audio) {{
        audio.volume = 0.4;
        audio.play().catch(function(e) {{ console.log("Audio bloqueado:", e); }});
    }}
    

    let mainDoc = window.parent.document.body;
    let container = window.parent.document.getElementById('gift-doors');
    
    if(!container) {{
        container = window.parent.document.createElement('div');
        container.id = 'gift-doors';
        container.className = 'door-container';
        container.innerHTML = `
            <div class="door left">🚪 Benevolencia...</div>
            <div class="door right">Para el mejor papá </div>
        `;
        mainDoc.appendChild(container);
        
        // Ejecutar animación de apertura
        setTimeout(() => {{ container.classList.add('open'); }}, 150);
        

        setTimeout(() => {{ container.remove(); }}, 2600);
    }}
}});
</script>
"""

components.html(custom_html, height=0, width=0)



st.image("Benevolence-sol.png")

st.markdown(
    f'<h1 style="color:{custom_color}; text-align:center;">Benevolencia</h1>', 
    unsafe_allow_html=True
)

st.markdown(
    f'<h3 style="color:{custom_color}; text-align:center;">¡Feliz día del padre!</h3>', 
    unsafe_allow_html=True
)



if "desbloqueado" not in st.session_state:
    st.session_state.desbloqueado = False

st.write("") # Espaciado
st.write("Introduce la clave secreta familiar para abrir tu regalo:")


password = st.text_input("Contraseña:", type="password", key="pwd_input")

if st.button("Descubre el regalo... cuando tengas la contraseña", use_container_width=True):

    if password.lower() == "merci": 
        st.session_state.desbloqueado = True
        
 
        trigger_js = """
        <script>
        const event = new Event('open_door');
        window.parent.document.dispatchEvent(event);
        </script>
        """
        components.html(trigger_js, height=0, width=0)
    else:
        st.error("Esa no es la clave...")



if st.session_state.desbloqueado:
    st.balloons() # Lluvia de globos nativa
    

    st.markdown(f"""
    <div style="background-color: #1e1e24; padding: 35px; border-radius: 15px; border: 1px solid {custom_color}; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); margin-top: 30px;">
        <h2 style="color: {custom_color}; text-align: center; font-family: 'Helvetica Neue', sans-serif;">Hola Pa,</h2>
        <br>
        <p style="font-size: 1.15rem; color: #e0e0e6; line-height: 1.8; text-align: justify; font-family: 'Georgia', serif;">
            Hola pa! si estas leyendo esto es porque adivinaste la contraseña o llegaste hasta el punto final en la bicicleta,
            te agradezco por el esfuerzo sea cual sea la forma por la que descubriste la contraseña. Te quería decir que muchas
            gracias por tenerme toda la paciencia del mundo y obviamente por algo puse ese simbolo arriba de la página... Es considerado
            como el simbolo de la benevolencia en un videojuego. <br><br>
            Te agradezco por ser un buen padre a pesar de todo por lo que tuviste que pasar en la vida. Espero poder agradecerte
            propiamente algún día, yo se que a veces he sido una decepción pero eso no significa que en el futuro lo siga siendo,
            seguramente con el paso del tiempo pueda agradecerte de verdad. <br><br>
            Muchas gracias por esforzarte para darnos lo mejor a mi mamá y a mi, lo aprecio y creo que mi mamá tambien.
            Y muchas gracias por quererme. Creo que hay cierto merito y valor en que haya amor en una familia, pues creo que es algo de lo que a
            veces el mundo carece. 
        </p>
        <br>
        <p style="text-align: right; font-weight: bold; color: {custom_color}; font-size: 1.2rem; font-family: 'Helvetica Neue', sans-serif;">
            Con toda mi admiración,<br>
            Jose Juan
        </p>
    </div>
    """, unsafe_allow_html=True)
