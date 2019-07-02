# inventory_test
Desde el admin de django se puede ingresar y actualizar datos al modelo Inventory y al modelo LoadFile.
Para la carga del archivo debe ser un archivo xlsx solo con datos para el model Inventory, ej:

A     | B     | C 
------| ------|-------
1     | 23    | 12.42
12    | 43    | 23.4  

A = serial number
B = Quantity(stock)
C = price

En el archivo de escel solo van los datos sin encabezados.
Cuando se carga el archivo se carga, se carga a la tabla inventario, si ya existe el serial number solo se aumenta la cantidad.

# Requerimientos:

para instalar el conector de mysqlclient

```
sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev
```

los requerimiento para el proyecto estan el archvio 

```
requirements.txt
```

## activar venv
  En la carpeta del proyecto:
```
source venv/bin/activate
```

## Migraciones:

```
python manage.py migrate
```

## correr el proyecto:
```
python manage.py runserver
```
