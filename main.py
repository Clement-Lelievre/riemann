import matplotlib.pyplot as plt
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Riemann", # => Quick reference - Streamlit
    page_icon="➕",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed

st.sidebar.write(f'''<a href="#♾️ Riemann (1826-1866), explorateur de l'infini ♾️">♾️ Riemann (1826-1866), explorateur de l'infini ♾️</a>''', unsafe_allow_html=True)
st.write(f'''<a name="♾️ Riemann (1826-1866), explorateur de l'infini ♾️"></a>''', unsafe_allow_html=True)
'''# ♾️ Riemann (1826-1866), explorateur de l'infini ♾️'''

st.markdown("""\n

    ## Le théorème de réarrangement, un théorème profondément contre-intuitif \n

""")

st.markdown('''\n''')
st.markdown('''[Page Wikipédia du théorème](https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_de_r%C3%A9arrangement_de_Riemann) \n
''')

st.markdown('''##Illustration avec la série harmonique alternée:\n

''')

st.latex(r'''
    \sum_{k=1}^\infty \frac{(-1)^{k+1}}{k} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \xrightarrow{\enskip\\} ln(2)
    ''')

@st.cache
def riemann_sum(n:int):
    '''Takes an integer representing the index up to which the sum of the alternate harmonic series is computed
    '''
    s = 0
    for k in range(n):
        s += (-1)**k/(k+1)
    return s

x = [i for i in range(100)] # the indices
y = [riemann_sum(i) for i in x] # the sum values up to indice i_

plt.figure()
plt.plot(x,y)
plt.title('''Série harmonique alternée "à l'état naturel" (converge vers ln(2) )''')
plt.xlabel('Nombre de termes')
plt.ylabel('Valeur de la série')
st.pyplot()

st.markdown("""## Changer l'ordre des termes, c'est modifier la somme de la série! 🤩
## Mieux, on peut choisir la somme (n'importe quel réel, et même l'infini): il existera alors un "réarrangement" des termes menant à cette nouvelle limite\n
""")
st.markdown('''\n''')

st.sidebar.write(f'<a href="#Changer la somme de la série! 💪">Changer la somme de la série! 💪</a>', unsafe_allow_html=True)
st.write(f'<a name="Changer la somme de la série! 💪"></a>', unsafe_allow_html=True)
'# Changer la somme de la série! 💪'

st.markdown("""## Choisir la nouvelle limite de la série, le graphique s'actualisera 👇🏻\n

""")
st.markdown('''\n''')


st.sidebar.markdown("""

    ## Site codé en Python par 

    [Clément Lelièvre](https://www.linkedin.com/in/clem-data/) """)


new_sum = st.slider('Nouvelle limite de la série', 0.25, 5.0, 3.0, 0.25,help='Choisir le nombre vers lequel convergera la série après réarrangement de ses termes')


if new_sum:
    pos = [(-1)**k/(k+1) for k in range(1_000_000) if k%2 == 0]
    neg = [(-1)**k/(k+1) for k in range(1_000_000) if k%2 == 1]
    new_limit = new_sum
    s = 0
    index_pos = 0
    index_neg = 0
    series_values = []
    nb_cycles = 80
    cycle_size = []

    for i in range(nb_cycles): # this creates 80 "cycles"
        while s < new_limit:
            s += pos[index_pos]
            index_pos += 1
            series_values.append(s)
        cycle_size.append(index_pos)
        s += neg[index_neg]
        index_neg += 1
        series_values.append(s)
    cycle_size = [cycle_size[i+1] - cycle_size[i] for i in range(len(cycle_size)-1) ]
    
    plt.figure()
    plt.plot([indice for indice in range(len(series_values))], series_values)
    plt.title('La même série harmonique, réarrangée pour converger vers '+str(new_limit))
    plt.xlabel('Nombre de termes')
    plt.ylabel('Valeur de la série')
    st.pyplot()
    termes = 'terme' if cycle_size[-1]+1 == 1 else 'termes'
    st.info(f'Après quelques itérations, chaque "cycle"  contient {cycle_size[-1]+1} '+ termes+'! Autrement dit, le nombre de termes utilisés par "cycle" converge! 😲')



