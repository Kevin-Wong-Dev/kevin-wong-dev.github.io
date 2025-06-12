import pandas as pd

ruta = "Menu_Las_Glorias_2025_Completo.xlsx"

xlsx = pd.ExcelFile(ruta)
hojasNombre = xlsx.sheet_names
hojas = len(xlsx.sheet_names)

for x in range(0, hojas):
    df = pd.read_excel(xlsx, sheet_name=x)
    platillo = df[["Platillo"]]
    precio = df[["Precio"]]
    print(df)


html_str = """
           <table>
                 <tr>
                   <th>A</th>
                   <th colspan="1">B</th>
                     <th rowspan="1">C</th>
                 </tr>
                <tr>
                     <td>a</td>
                     <td>b</td>
                   <td>c</td>
                 </tr>
            </table>
         """


with open("tmp.html", "w") as f:
    f.write(html_str)
