from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    promedio = None
    estado = ""

    if request.method == 'POST':

        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        if asistencia < 0 or asistencia > 100:
            error = "La asistencia debe estar entre 0 y 100"

        elif (nota1 > 70 or nota2 > 70 or nota3 > 70):
            error = "La nota no puede ser mayor a 70"

        elif (nota1 < 10 or nota2 < 10 or nota3 < 10):
            error = "La nota no puede ser menor a 10"

        else:
            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"


    return render_template(
        'ejercicio1.html',
        promedio=promedio,
        estado=estado
    )


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    mensaje = ""

    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        longitud_max = max(len(nombre) for nombre in nombres)

        nombres_mayores = [
            nombre for nombre in nombres
            if len(nombre) == longitud_max
        ]

        if len(nombres_mayores) == 1:
            mensaje = (
                f"El nombre con mayor cantidad de caracteres es "
                f"{nombres_mayores[0]} y tiene {longitud_max} caracteres."
            )
        else:
            mensaje = (
                f"Los nombres con mayor cantidad de caracteres son: "
                f"{', '.join(nombres_mayores)}. "
                f"Todos tienen {longitud_max} caracteres."
            )

    return render_template(
        'ejercicio2.html',
        mensaje=mensaje
    )


if __name__ == '__main__':
    app.run(debug=True)