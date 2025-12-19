from django.shortcuts import render

#Paso 6: Crear las vistas usando variables
def inicio(request): #PASO 13: Reemplazo contenido para que se adapte a mi idea
    contexto = {
        'titulo': 'El Despertar del Héroe',
        'texto': 'Has despertado en los campos de Hyrule. Eres Link, un joven destinado a grandes aventuras. A lo lejos ves el Bosque Kokiri, hogar de tu infancia, y el majestuoso Castillo Hyrule. Una voz misteriosa te susurra: "El destino de Hyrule está en tus manos". ¿Qué camino elegirás?',
        'imagen': 'https://easycdn.es/1/imagenes/the-legend-of-zelda-breath-of-the-wild-nintendo-switch_344428.jpg',
        'opciones': [
            {'url': 'bosque', 'texto': 'Explorar el Bosque Kokiri'},
            {'url': 'castillo', 'texto': 'Dirigirse al Castillo de Hyrule'}
        ]
    } 
    return render(request, 'historia/pagina.html', contexto)

#Link en el bosque: Encuentra la Espada Kokiri
def bosque(request):
    contexto = {
        'titulo': 'El Bosque Kokiri',
        'texto': 'El bosque esta lleno de vida y miesterio. Los Kokiri, niños eternos del bosque, te saludan con curiosidad. En el Gran Árbol Deku encuentras la legendaria Espada Kokiri brillando con una luz mágica. El tomarla, sientes una energía ancestral recorrer tu cuerpo. Ahora puedes elegir: ¿explorar el antiguo Templo del Tiempo o aventurarte hacia el Lago Hylia?',
        'imagen': 'https://static.wikia.nocookie.net/smashbrosfanon/images/9/99/Bosque_Kokiri.jpg/revision/latest?cb=20141101002055&path-prefix=es', #Cambiar imagen 
        'opciones': [
            {'url': 'templo', 'texto': 'Entrar en el Templo del Tiempo'},
            {'url': 'lago', 'texto': 'Explorar el Lago Hylia'}
        ]
    }
    return render(request, 'historia/pagina.html', contexto)

#Link en el Castillo: Link conoce a la Princesa Zelda
def castillo(request):
    contexto = {
        'titulo': 'El Castillo de Hyrule',
        'texto': 'Logras inflirtarte dentro del castillo y conoces a la Princesa Zelda. Ella te revela una profecía: Ganondorf, el rey del desierto, planea apoderarse de la Trifuerza y sumir a Hyrule en la oscuridad. Zelda te pide que reúnas las tres Piedras Espirituales apra abrir la Puerta del Tiempo y detenerlo. Esta es una misión peligrosa... ¿Aceptarás el llamado del destino?',
        'imagen': 'https://preview.redd.it/hyrule-castle-what-could-be-added-or-improved-v0-xl14ome37re91.jpg?auto=webp&s=fe07e53caa2d03b15a8173e44627f572949a3f66', #Cambair imagen
        'opciones': [
            {'url': 'mision', 'texto': 'Aceptar la misión de Zelda'},
            {'url': 'final_malo', 'texto': 'Rechazar y huir del castillo'}
        ]
    }
    return render(request, 'historia/pagina.html', contexto)

def templo(request):
    contexto = {
        'titulo': 'El Templo del Tiempo',
        'texto': 'Entras al sagrado Templo del Tiempo. Al colocar el Espada Maestra en su pedestal, una luz cegadora te envuelve. Has viajado 7 años al futuro. Ahora eres el Héroe del Tiempo, destinado a enfrentar a Ganondorf. Con valentía y determinación restauras la paz en Hyrule.',
        'imagen': 'https://static.wikia.nocookie.net/zelda/images/e/eb/BotW_Plano_general_del_Templo_del_Tiempo.png/revision/latest/scale-to-width-down/220?cb=20160622205450&path-prefix=es', #Cambair imagen
    }
    return render(request, 'historia/final.html', contexto)

#Link conoce a los Zora
def lago(request):
    contexto = {
        'titulo': 'El Lago Hylia',
        'texto': 'Las aguas cristalinas del Lago Hylia te reciben con calma. Los Zora, seres acuáticos elegantes, emergen de las profundidades. Su princesa, Ruto, te entrega la Piedra Espiritual del Agua como muestra de gratitud por ayudar a su pueblo. Te conviertes en un aliado respetado de los Zora, guardián de las aguas sagradas de Hyrule.',
        'imagen': 'https://zelda.fandom.com/es/wiki/Lago_Hylia' #Cambiar imagen
    }
    return render(request, 'historia/final.html', contexto)

def mision(request):
    contexto = {
        'titulo': 'El Salvador de Hyrule',
        'texto': 'Aceptas la misión de Zelda con honor y valentía. Viajas por todo Hyrule: escalas la Montaña de la Muerte para obetener la Pidra Goron, nada en los dominios Zora por la Piedra del Agua, y despiertas al Gran Árbol Deju para conseguir la Piedra del Bosque. Con las tres piedras, abres la Puerta del Tiempo, tomas la Espada Mastra y derrotas a Ganondorf. ¡Hyrule está a salvo y tu leyenda vivirá por siempre!',
        'imagen': 'https://static1.thegamerimages.com/wordpress/wp-content/uploads/2021/06/breath-of-the-wild-2-links.jpeg' #Cambiar imagen
    }
    return render(request, 'historia/final.html', contexto)

#Final malo
def final_malo(request):
    contexto = {
        'titulo': 'La Oscuridad Prevalece',
        'texto': 'Decides que la responsabilidad es demasiado grande y huyes del castillo. Sin tu ayuda, Zelda es capturada por Ganondorf. El villano obtiene la Trifuerza y transforma Hyrule en un reino de sombras y desesperación. Los campos verdes se marchitan, el cielo se oscurece eternamente y el pueblo sufre bajo su tirnía. Tu cobardía ha condenado a Hyrule a una era de oscuridad infinita...',
        'imagen': 'https://i.blogs.es/38ab4a/ganon1366_2000--1-/375_375.jpeg' #Cambiar imagen
    }
    return render(request, 'historia/final.html', contexto)