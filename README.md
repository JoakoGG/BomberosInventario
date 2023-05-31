# BomberosInventario

notas magicas:

- hay q arreglar el bug de busqueda despues de los botones
  - se deberia arreglar modificando la estructura de las tablas
- en las cajoneras agregar una especifica para techo (despues preocuparse de la bodega primero camiones)
- podriamos cambiar las tablas por camion a una sola tabla con objetos con attr inventario
- seria de utilidad colorear los objetos segun su estado (y colocar una leyenda)
- no es de utilidad marca ni modelo ni id ni objid (para lo que creen querer usar)

-- objetos:

- obj : agregar cantidad
- obj : estados => agregar (operativo, dado de baja, perdido)
- funcion : editar observacion despues de agregar
- funcion : editar estado despues de agregar (click derecho, u otra accion rapida)
- obj : el tipo de objetos se muestra en "nombre" no en un attr "tipo"
- funcion : mover de inventario los objetos (individual y en cantidad)

-- inventarios:

- funcion : dar de baja un camion completo (marcar objetos del camion)
- funcion : buscar por cajonera (sugerir usar codigos ej: "codcamion"||"cajonera"||"altura" r1as (camion r1, caj: a, compartimiento superior))

ARREGLAR:
CAMBIAR PALETA DE COLORES
CAMBIAR GET \* FROM DB (no funciona pq ta mal guardao la columna inv)
