# Sptify-a-mp3

Spotd conversion de mp3
Spotdl es un libreria de python que su funcion es descargar musica en diferentes formatos, como mp3,mp4, letras de canciones etc. lo importante que tiene esta libreria es la funcion con spotify, ya que podemos realizar descargas sin la necesidad de arriesgarnos a un virus o ransomware. 

Mi objetivo principal fue convertir una playlist a mp3 desde spotify junto a spotdl, y se logro, a lo largo del proceso tuve preguntas: como lo hago?, como resuelvo el problema?, no comprendo esta libreria. No se si pueda hacerlo. Pero las cosas no fueron haci, a lo largo de este proceso logre identificar factores para poder lograr mi objetivo y usando la herramienta de la ia para dudas. 

# Fase 1 preparacion:

Durante esta fase tuve la tarea de lograr entender esta libreria y tener el conocimiento basico para obtener mi objetivo, sin embargo las cosas no fueron faciles, durante horas de leer y no encontrar un sentido a lo que leia fue dificil, ya que la libreria no tiene la suficiente claridad o tal vez el problema fui yo? Pero notando un apartado de ejemplos me base para alcanzar mi objetivo

# Fase 2 el desarrollo:
<-
Durante esta fase tuve complicaciones, ya que no tenia el suficiente conocimiento, pero que hay que hacer antes de codear?, mi respuesta fue una estructura o pseudocodigo, que para mi esto fue clave en el desarrollo, en el lenguaje python logre mi objetivo, tenia mi plano y entender mi idea mucho mejor pero ahora sigue el reto como empezar.

# Fase 3 ia:

Durante esta fase realice una estructura por mi cuenta, basandome en foros y documentación, haciendome preguntas de que hace este metodo?, que es esta funcion?, para que sirve esto? Que significa x?, en ese momento recurrir a la ia, solo dandome una repuesta y cambiando un parametro que yo no lo percibi por mi falta de conocimiento, ahora fue cuando logre mi objetivo. Y logre comprender lo que estaba haciendo.
# Errores: 
Durante las ejecuciones note que se acaba mis tokens ya que spotify me daba un limite, pero la solucion fue que mediante la terminal ingrese mis id_client y mi id_client-secret pero para esto necesitamos un comando sport query –client-id Client-ID y lo mismo que id secret en mi caso en el apartado de query seleccione mi misma client id y secret id por lo que funciono perfectamente, hasta el momento de hoy no he tenido un limite de descarga.

# Error en search y get_simple_song
Durante la fase de desarollo experimente diferentes errores ya que lo que hacia era obtener el track de la cancion y que hacia despues?, pues solamente buscaba y no descargaba, fue en eso que cambiando los parametros de dowlead = spotdl(id client, secret id ) solucione mi problema y cambie songs_query = download.serch() busca mi cancion con mis credenciales y mediante un ciclo de iteracion for song in songs_query realize un downloader.dowload(song)
 Y se realizo perfectamente la descarga


script :
> from spotdl import Spotdl
> from pathlib import Path
>
>downloader = Spotdl(
>    client_id='#client id',
>    client_secret='#client secret'
>)
>songs_query = downloader.search(['spotify/youtube'])
>
>for song in songs_query:
>    downloader.download(song)
