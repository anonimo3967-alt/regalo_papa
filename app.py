import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página (¡Esencial poner esto al puro inicio!)
st.set_page_config(page_title="Benevolencia - Feliz Día Papá", page_icon="❤️", layout="centered")

# Ocultar menús nativos de Streamlit para mejorar la estética "super wow"
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# --- TU CONFIGURACIÓN DE COLOR ---
custom_color = "#FFF4CB"

# --- INYECCIÓN DE ANIMACIONES, FONDO OSCURO ANIMADO Y EFECTOS AUDIO/PUERTAS ---
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

/* Contenedor de las puertas que se abren */
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

/* Línea divisoria dorada en el centro */
.door.left {{ border-right: 2px solid {custom_color}; }}
.door.right {{ border-left: 2px solid {custom_color}; }}

/* Clases para activar la animación de apertura */
.open .door.left {{ transform: translateX(-100%); }}
.open .door.right {{ transform: translateX(100%); }}
</style>

<div class="main-bg"></div>

<!-- Link del archivo de audio (Reemplázalo por el .mp3 que gustes) -->
<audio id="bg-music" src="https://www.myinstants.com/media/sounds/subnautica-new-blueprint-acquired.mp3" preload="auto"></audio>

<script>
// Escuchador que activa Streamlit cuando la clave es correcta
window.parent.document.addEventListener('open_door', function() {{
    // 1. Reproducir el sonido/música al hacer clic
    var audio = document.getElementById('bg-music');
    if(audio) {{
        audio.volume = 0.4;
        audio.play().catch(function(e) {{ console.log("Audio bloqueado:", e); }});
    }}
    
    // 2. Inyectar las puertas en la interfaz
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
        
        // Remover del sistema tras terminar el efecto para recuperar clics nativos
        setTimeout(() => {{ container.remove(); }}, 2600);
    }}
}});
</script>
"""
# Mandamos el HTML base de forma invisible
components.html(custom_html, height=0, width=0)


# --- TU CÓDIGO INICIAL (Interfaz Principal) ---
st.image("Benevolence-sol.png")

st.markdown(
    f'<h1 style="color:{custom_color}; text-align:center;">Benevolencia</h1>', 
    unsafe_allow_html=True
)

st.markdown(
    f'<h3 style="color:{custom_color}; text-align:center;">¡Feliz día del padre!</h3>', 
    unsafe_allow_html=True
)


# --- SISTEMA DE VALIDACIÓN Y CONTRASEÑA ---
if "desbloqueado" not in st.session_state:
    st.session_state.desbloqueado = False

st.write("") # Espaciado
st.write("Introduce la clave secreta familiar para abrir tu regalo:")

# Input de clave
password = st.text_input("Contraseña:", type="password", key="pwd_input")

if st.button("Descubre el regalo... cuando tengas la contraseña", use_container_width=True):
    # Cambia "benevolencia2026" por la contraseña exacta que quieras usar
    if password.lower() == "merci": 
        st.session_state.desbloqueado = True
        
        # Disparador JavaScript para abrir las puertas físicas en el navegador y reproducir música
        trigger_js = """
        <script>
        const event = new Event('open_door');
        window.parent.document.dispatchEvent(event);
        </script>
        """
        components.html(trigger_js, height=0, width=0)
    else:
        st.error("Esa no es la clave...")


# --- CONTENIDO DE TU CARTA (Aparece al validar) ---
if st.session_state.desbloqueado:
    st.balloons() # Lluvia de globos nativa
    
    # Caja de texto elegante tipo tarjeta física que combina con tu color personalizado
    st.markdown(f"""
    <div style="background-color: #1e1e24; padding: 35px; border-radius: 15px; border: 1px solid {custom_color}; box-shadow: 0px 10px 30px rgba(0,0,0,0.5); margin-top: 30px;">
        <h2 style="color: {custom_color}; text-align: center; font-family: 'Helvetica Neue', sans-serif;">Querido Papá,</h2>
        <br>
        <p style="font-size: 1.15rem; color: #e0e0e6; line-height: 1.8; text-align: justify; font-family: 'Georgia', serif;">
            [Aquí borras este texto y redactas tu carta personalizada] <br><br>
            ¡Escribe aquí todo lo que significa la palabra 'Benevolencia' en tu vida gracias a él, 
            tus anécdotas o tus palabras de agradecimiento más profundas!
        </p>
        <br>
        <p style="text-align: right; font-weight: bold; color: {custom_color}; font-size: 1.2rem; font-family: 'Helvetica Neue', sans-serif;">
            Con toda mi admiración y amor,<br>
            [Tu Nombre] ❤️
        </p>
    </div>
    """, unsafe_allow_html=True)
