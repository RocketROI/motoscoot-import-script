# motoscoot-import-script

Este proyecto permite **automatizar** la transformación de datos de producto exportados desde Magento.  
El objetivo principal es convertir los SKUs de "Productos Relacionados" y "Venta por arriba" en sus correspondientes **handles** (URLs amigables para el frontend).

---

## ⚙️ Requisitos previos

- Tener **Python 3.8 o superior** instalado.
- Tener el archivo exportado desde Magento (ej: `magexport_simples.csv`).

📌 Si no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

---

## 🚀 ¿Cómo ejecutar el script?

### 1. Clona este repositorio

git clone https://github.com/RocketROI/motoscoot-import-script.git  
cd motoscoot-import-script

---

### 2. Asegúrate de que tienes pandas instalado

`pandas` es la librería de Python que usamos para trabajar con el CSV.

Instálalo ejecutando:

pip install pandas

---

### 3. Prepara tu archivo CSV

- El nombre del archivo debe ser `magexport_simples.csv`.
- Asegúrate de que el CSV incluya como mínimo estas columnas:
  - `SKU <sku>`
  - `URL Key <url_key> (admin)`
  - `Productos relacionados <relation>`
  - `Venta por arriba <up_sell>`

---

### 4. Ejecuta el script

📋 ¿Cómo usarlo?

- Coloca en la misma carpeta tu CSV original (`magexport_simples.csv` o como lo llames).
- Abre una terminal o consola de comandos en esa carpeta.
- Ejecuta:

python convert_skus_to_handles.py

✅ Y automáticamente tendrás un nuevo archivo llamado **magexport_simples_actualizado.csv**.

---
