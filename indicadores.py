# primero necesito saber con que columnas cuento.
data.columns

# dado el requerimiento, puedo ordenar por volumen descendiente entonces
# en la posicion 0 voy a  tener el mayor volumen y como voy a tener la row tambien 
# la fecha, en un caso guardo en una variable y en el otro simplemente muestro por 
# pantalla

max_volumen_row = data.sort_values(by="Volume", ascending=False).iloc[0]
print(f"La fecha con mayor volumen fué, {max_volumen_row.name.date()}")
max_volumen = max_volumen_row.Volume
print(f"el volumen operado fue de {max_volumen}")
