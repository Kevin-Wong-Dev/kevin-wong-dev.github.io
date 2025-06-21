html_str = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entradas & Sopas</title>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap"
        rel="stylesheet">
    <link rel="stylesheet" href="../assets/css/styles.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-4Q6Gf2aSP4eDXB8Miphtr37CMZZQ5oXLH2yaXMJ2w8e2ZtHTl7GptT4jmndRuHDT" crossorigin="anonymous">
</head>

<body>
    <!--cabecero-->
    <div>
        <img class=" fondo" src="../assets/img/fondo_menu.png" alt="">
        <a href="../index.html">

            <img class="logo" src="../assets/img/logo_glorias.png" alt="">

        </a>
    </div>

    <!--Menu-->
    <div class="container-md menu-mg-y">
        <!--Entradas-->
        <h1 class="carta-letra-titulo">Entradas</h1>
        <hr>
        

    </div>

    <!--boton-->
    <div class="container text-center btn-mg-y">
        <a class="btn btn-primary" href="../index.html" role="button">Regresar</a>
    </div>

    <!--redes-->
    <footer class="container bg-footer footer-pd-y">
        <div class="row ">
            <!--Contacto-->
            <div class="col text-center redes-letra">
                Eventos Las Gloriass<br> Tel. 668 885 85 40
            </div>

            <!--instagram-->
            <div class="col text-center">
                <a href="https://www.instagram.com/lasgloriasrestaurant/" target="_blank">
                    <img class="logos-redes" src="../assets/img/ig_logo.png" alt="">
                    <p class="redes-letra">lasgloriasrestaurant</p>
                </a>
            </div>

            <!--facebook-->
            <div class="col text-center">
                <a href="https://www.facebook.com/LasGloriasRestaurant" target="_blank">
                    <img class="logos-redes" src="../assets/img/fb_logo.png" alt="">
                    <p class="redes-letra">lasgloriasrestaurant</p>
                </a>
            </div>

            <!--tequila-->
            <div class="col text-center">

                <img class="logo-tequila" src="../assets/img/tequila_30-30.png" alt="">

            </div>

        </div>
    </footer>

</body>

</html>
"""

for x in range(7):
    with open(f"webs//{x}.html", "w", encoding="utf-8") as f:
        f.write(html_str)
