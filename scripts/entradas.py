import pandas as pd

# definir dataframe
ruta = "Menu_Las_Glorias_2025_Completo.xlsx"

xlsx = pd.ExcelFile(ruta)
hojasNombre = xlsx.sheet_names
hojas = len(xlsx.sheet_names)


# ciclo para crear documentos
for x in range(0, hojas):
    df = pd.read_excel(xlsx, sheet_name=x)
    articulos = ""
    platillo = df[["Platillo"]]
    precio = df[["Precio"]]

    # consegir valores del precio y platillo
    for index, row in df.iterrows():

        platillo_actual = row["Platillo"]
        precio_actual = row["Precio"]
        articulos += f"""<meta charset="UTF-8"> <div class="row">
                <div class="col-9 carta-letra">☆ {platillo_actual}</div>
                <div class="col-3 text-end carta-letra">{precio_actual}.00</div>
            </div>"""

    # lista completada
    html_str = f"""

    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
</head>

<body>
    <div>
        <img class=" fondo" src="../assets/img/fondo_menu.png" alt="">
        <img class="logo" src="../assets/img/logo_glorias.png" alt="">
    </div>
   
        <div class="container-md">
            <h1 class="carta-letra-titulo">{hojasNombre[x]}</h1>
            <hr>
            {articulos}

        </div>

    </div>
</body>

</html>
            """
    # crear documento
    with open(f"seccionesGen//{hojasNombre[x]}.html", "w", encoding="utf-8") as f:
        f.write(html_str)
